import datetime
from pprint import pprint

from accounts.models import User
# import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer

# Create your views here.

# if len(Article.objects.all()) < 100:
#     for i in range(1, 101):
#         article = Article(title=i, content=i, user=User.objects.get(pk=1))
#         article.save()


@api_view(["GET",])
def articlesList(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@ login_required
def createArticle(request):
    article = Article()
    article.title = request.data['title']
    article.content = request.data['content']
    article.user = request.user
    article.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE",])
def article(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        if article.user == request.user:
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        if article.user == request.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET",])
def CommentsList(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = Comment.objects.all().filter(article=article)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@ login_required
def createComment(request, article_pk):
    print(request.user)
    article = Article.objects.get(pk=article_pk)
    comment = Comment()
    comment.content = request.data['comment']
    comment.article = article
    comment.user = request.user
    comment.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(["PUT", "DELETE",])
def comment(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'PUT':
        if comment.user == request.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        print(comment.user)
        print(request.user)
        if comment.user == request.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)