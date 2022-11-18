from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.articlesList),
    path('/new/', views.createArticle),
    path('/<int:article_pk>/', views.article),
]