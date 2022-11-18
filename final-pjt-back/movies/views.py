import datetime
from pprint import pprint

import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Comment, Genre, Movie
from .serializers import CommentSerializer, MovieSerializer

API_KEY = '550af897681babc49f34957fa75cbee8'
# Create your views here.


def dbInitialize():
    PAGE_NUM = 50
    for gen in requests.get(f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR').json()['genres']:
        genre = Genre()
        genre.id = gen['id']
        genre.name = gen['name']
        genre.save()
    print('get genre finished')
    print(f'get movie startd (1 to {PAGE_NUM})')
    for idx in range(1, PAGE_NUM + 1):
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
        print(f'{idx}/{PAGE_NUM}')
    print('get movie finished')
            
    return 


try:
    if not Movie.objects.all().count():
        print('start API')
        dbInitialize()
        print('end API')
except:
    print('migrate first')


@api_view(["GET",])
def getMovieList(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET','DELETE'])
def getMovieDetail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'GET':
        trailer_url = f'https://api.themoviedb.org/3/movie/{movie.tmdb_id}/videos?api_key={API_KEY}&language=ko-KR'
        for video in requests.get(trailer_url).json()['results']:
            if video['type'] == 'Trailer':
                movie.trailer = video['key']
                break
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'DELETE'])
def comments(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == "GET":
        comments = Comment.objects.all().filter(movie=movie)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        comment = Comment()
        comment.movie = movie
        comment.user = request.user
        comment.content = request.data['comment']
        comment.save()
    elif request.method == 'DELETE':
        comment = Comment.objects.get(pk=request.data['commentId'])
        print(comment)
        comment.delete()
    return redirect(f'../../{movie_id}')


@api_view(['GET', 'POST'])
@login_required
def clickLikeButton(request, movie_id):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_id)
        if request.user in movie.like_users.all():
            return Response({'like': True}, status=status.HTTP_200_OK)
        else:
            return Response({'like': False}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        if request.user in movie.like_users.all():
            movie.like_users.remove(request.user)
            return Response({'like': False}, status=status.HTTP_201_CREATED)
        else:
            movie.like_users.add(request.user)
            return Response({'like': True}, status=status.HTTP_200_OK)