from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests

from .models import Movie, Genre
from .serializers import MovieSerializer

import datetime
from pprint import pprint
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
            # trailer_url = f'https://api.themoviedb.org/3/movie/{res["id"]}/videos?api_key={API_KEY}&language=ko-KR'
            # for video in requests.get(trailer_url).json()['results']:
            #     if video['type'] == 'Trailer':
            #         trailer = video['key']
            #         break
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
            # movie.trailer = trailer
            # movie.director = director
            movie.save()
            for j in res['genre_ids']:
                movie.genre.add(Genre.objects.get(id=j))
        print(idx)
    print('get movie finished')
            
    return redirect('http://127.0.0.1:8000/movie/api/v1/')

# if not Movie.objects.all().count():
#     print('start API')
#     dbInitialize()
#     print('end API')

@api_view(["GET",])
def getMovieList(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)