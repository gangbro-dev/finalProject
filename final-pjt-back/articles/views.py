import datetime
from pprint import pprint

# import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from accounts.models import User

# Create your views here.


@api_view(["GET",])
def articlesList(request):
    articles = Article().objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(["POST"])
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

