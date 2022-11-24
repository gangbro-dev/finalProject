import datetime
import json
from itertools import combinations
from pprint import pprint

import requests
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Comment, Genre, Movie
from .serializers import CommentSerializer, MovieSerializer

API_KEY = '550af897681babc49f34957fa75cbee8'
# Create your views here.


# def dbInitialize():
#     PAGE_NUM = 100
#     for gen in requests.get(f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR').json()['genres']:
#         genre = Genre()
#         genre.id = gen['id']
#         genre.name = gen['name']
#         genre.save()
#     print('get genre finished')
#     print(f'get movie startd')
#     for idx in range(1, PAGE_NUM + 1):
#         url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page={idx}&region=kr'
#         response = requests.get(url).json()['results']
#         for res in response:
#             credit = requests.get(f'https://api.themoviedb.org/3/movie/{res["id"]}/credits?api_key={API_KEY}&language=ko-KR').json()
#             actors = []
#             for actor in credit['cast'][:5]:
#                 actors.append({'name': actor['name'], 'id': actor['id']})
#             for crew in credit['crew']:
#                 if crew['job'] == 'Director':
#                     director = crew['name']
#             trailer = 'No_Trailer'
#             trailer_url = f'https://api.themoviedb.org/3/movie/{res["id"]}/videos?api_key={API_KEY}&language=ko-KR'
#             for video in requests.get(trailer_url).json()['results']:
#                 if video['type'] == "Trailer":
#                     trailer = video["key"]
#                     break
#             movie = Movie()
#             movie.title = res['title']
#             movie.overview = res['overview']
#             movie.rate = int(res['vote_average'] * 10)
#             movie.popularity = res['popularity'] * 1000
#             movie.release_date = datetime.datetime.strptime(res['release_date'], '%Y-%m-%d').date()
#             movie.poster_path = res['poster_path']
#             movie.tmdb_id = res['id']
#             movie.trailer = trailer
#             movie.actors = json.dumps(actors)
#             movie.director = director
#             movie.save()
#             for j in res['genre_ids']:
#                 movie.genre.add(Genre.objects.get(id=j))
#         print(f'{idx}/{PAGE_NUM}')
#     print('get movie finished')
            
#     return 


# try:
#     if Movie.objects.all().count() < 2000:
#         print('start API')
#         dbInitialize()
#         print('end API')
# except:
#     print('migrate first')


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


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
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
        return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        comment = Comment.objects.get(pk=request.data['commentId'])
        if request.user == comment.user:
            comment.content = request.data['comment']
            comment.save()
            return Response(status=status.HTTP_201_CREATED)
        else: 
            return Response(status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        comment = Comment.objects.get(pk=request.data['commentId'])
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


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


@api_view(['GET',])
def getLikeMovie(request, username):
    data = User.objects.get(username=username).like_movies.all()
    serializer = MovieSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def 응애_대표작찾아줘(id, 요청횟수):
    request_url = f'https://api.themoviedb.org/3/person/{id}/movie_credits?api_key={API_KEY}&language=ko-KR'
    response = requests.get(request_url).json()['cast']
    try:
        video = sorted(response, key=lambda x: x['popularity'])[-요청횟수]
        while not video['poster_path']:
            요청횟수 += 1
            video = sorted(response, key=lambda x: x['popularity'])[-요청횟수]
    except:
        return False
    return video


def 대표작이_디비에_있을까요_없을까요(video):
    try:
        return Movie.objects.get(tmdb_id=video['id']).id
    except:
        request_url = f'https://api.themoviedb.org/3/movie/{video["id"]}?api_key={API_KEY}&language=ko-KR'
        res = requests.get(request_url).json()
        print('db 추가 영화 생성')
        credit = requests.get(f'https://api.themoviedb.org/3/movie/{res["id"]}/credits?api_key={API_KEY}&language=ko-KR').json()
        actors = []
        for actor in credit['cast'][:5]:
            actors.append({'name': actor['name'], 'id': actor['id']})
        director = 'not Found'
        for crew in credit['crew']:
            if crew['job'] == 'Director':
                director = crew['name']
        movie = Movie()
        movie.title = res['title']
        movie.overview = res['overview']
        movie.rate = int(res['vote_average'] * 10)
        movie.popularity = res['popularity'] * 1000
        movie.release_date = datetime.datetime.strptime(res['release_date'], '%Y-%m-%d').date()
        movie.poster_path = res['poster_path']
        movie.tmdb_id = video['id']
        movie.trailer = 'None'
        movie.actors = json.dumps(actors)
        movie.director = director
        movie.save()
        for genre in res['genres']:
            movie.genre.add(Genre.objects.get(id=genre['id']))

        return movie.pk

@ api_view(['post',])
def get_recommend_list(request):
    like_movie_list = request.user.like_movies.all()
    recommended_list = list()
    for movie in request.data['recommended']['movies']:
        recommended_list.append(movie['id'])
    if like_movie_list:
        like_actors_count = dict()
        genre_count = dict()
        for like_movie in like_movie_list:
            # 좋아하는 장르 추출
            for like_genre in like_movie.genre.all():
                if like_genre.name in genre_count.keys():
                    genre_count[like_genre.name] += 1
                else:
                    genre_count[like_genre.name] = 1
            # 좋아하는 배우 추출(우선 간판 1명만 써보자)
            for like_actor_object in json.loads(like_movie.actors):
                like_actor = like_actor_object['id']
                if like_actor in like_actors_count.keys():
                    like_actors_count[like_actor] += 1
                else:
                    like_actors_count[like_actor] = 1
            # 확인한 영화 추천안함목록에 추가
            recommended_list.append(like_movie.pk)
        genre_count = sorted(genre_count.items(), key=lambda x: x[1])
        like_actors_count = sorted(like_actors_count.items(), key=lambda x: x[1])
        
        recommend_querySet = Movie.objects.none()
        # -------------- 추천 알고리즘 어케 뽑지 --------------------------
        # 목표: 추천 대기열 N개 만들기
        # 일단, 가장 좋아하는 장르를 찾자(여러개 일 수 도 있다! 왜냐 좋아요 표시한 영화가 액션 5개 로멘스 5개 일 수 있음)
        # 그러므로 우선 vue에서 좋아하는 장르를 선택하게 할 것 (request.data.fav_genre)에 넣어두자(이름으로)
        # 근데? 너무 많은 장르를 선택하면 영화가 하나도 없을 수 가 있다(최대 3개)
        # 그럼 그 장르의 영화들을 뽑자 어떻게? and연산으로 어디서? 밑에서 (1.)
        # 여기서 5개 보여줌
        # 이제 배우 기반으로 영화 찾아보자 (2.)
        # --------------------------------------------------------------
        # 1. 장르별 추천
        # fav_genres = ['액션']
        fav_genres = list()
        while genre_count:
            fav_genres.append(genre_count.pop()[0])
        cnt = 0
        for fav_genres_set in combinations(fav_genres, 3):
            rst = Movie.objects.all()
            for fav_genre in fav_genres_set:
                rst = rst.filter(Q(genre=Genre.objects.get(name=fav_genre)))
            for movie in rst:
                if movie.id not in recommended_list and movie.rate > 60 and movie.overview:
                    recommend_querySet = recommend_querySet.union(Movie.objects.filter(pk=movie.id))
                    recommended_list.append(movie.id)
                    cnt += 1
                if (cnt >= 5):
                    break
        # pprint('1. done')
        # pprint(recommend_querySet)
        # 2. 배우별 추천
        pprint(like_actors_count)
        cnt = 0
        while (cnt < 3) & bool(fav_genres):
            if like_actors_count:
                best_actor = like_actors_count.pop()[0]
            else:
                break
            idx = 1
            while True:
                cast_data = 응애_대표작찾아줘(best_actor, idx)
                if not cast_data:
                    break
                movie_pk = 대표작이_디비에_있을까요_없을까요(cast_data)
                movie = Movie.objects.get(pk=movie_pk)
                if movie.id not in recommended_list and movie.rate > 60 and movie.overview:
                        recommend_querySet = recommend_querySet.union(Movie.objects.filter(pk=movie.id))
                        recommended_list.append(movie.id)
                        cnt += 1
                        print('추가햇지롱')
                        break
                else:
                    # print('못추가햇지롱')
                    idx += 1
            if (cnt >= 5):
                break
        # print(recommend_querySet)
    else:
        cnt = len(recommended_list)
        recommend_querySet = Movie.objects.all()[cnt:cnt + 8]
    result = MovieSerializer(recommend_querySet, many=True)
    return Response(result.data, status=status.HTTP_200_OK)