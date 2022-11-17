import datetime
from pprint import pprint

import requests
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

from .models import Comment, Genre, Movie
from .serializers import CommentSerializer, MovieSerializer

API_KEY = '550af897681babc49f34957fa75cbee8'
# Create your views here.

def dbInitialize():
    for gen in requests.get(f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR').json()['genres']:
        genre = Genre()
        genre.id = gen['id']
        genre.name = gen['name']
        genre.save()
    print('get genre finished')
    for idx in range(1, 51):
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page={idx}&region=kr'
        response = requests.get(url).json()['results']
        for res in response:
            # for crew in requests.get(f'https://api.themoviedb.org/3/movie/{res["id"]}/credits?api_key={API_KEY}&language=ko-KR').json()['crew']:
            #     if crew['job'] == 'Director':
            #         director = crew['name']
            movie = Movie()
            movie.title = res['title']
            movie.overview = res['overview']
            movie.rate = int(res['vote_average'] * 10)
            movie.popularity = res['popularity'] * 1000
            movie.release_date = datetime.datetime.strptime(res['release_date'], '%Y-%m-%d').date()
            movie.poster_path = res['poster_path']
            movie.tmdb_id = res['id']
            movie.trailer = 'None'
            # movie.director = director
            movie.save()
            for j in res['genre_ids']:
                movie.genre.add(Genre.objects.get(id=j))
        print(idx)
    print('get movie finished')
            
    return 

# if not Movie.objects.all().count():
#     print('start API')
#     dbInitialize()
#     print('end API')

@api_view(["GET",])
def getMovieList(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def getMovieDetail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    trailer_url = f'https://api.themoviedb.org/3/movie/{movie.tmdb_id}/videos?api_key={API_KEY}&language=ko-KR'
    for video in requests.get(trailer_url).json()['results']:
        if video['type'] == 'Trailer':
            movie.trailer = video['key']
            break
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def getComments(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == "GET":
        comments = Comment.objects.all().filter(movie=movie)
        serializer = CommentSerializer(comments)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        comment = Commnet()
        comment.movie = movie
        comment.user = request.user
        print(request.data)
        return redirect(f'api/v1/movies/{movie_id}')
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
