from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.articlesList),
    path('new/', views.createArticle),
    path('<int:article_pk>/', views.article),
    path('<int:article_pk>/comment/', views.CommentsList),
    path('<int:article_pk>/comment/new/', views.createComment),
    path('<int:article_pk>/comment/<int:comment_pk>/', views.comment),
]