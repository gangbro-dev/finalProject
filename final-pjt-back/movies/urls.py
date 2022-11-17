from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getMovieList),
    path('<int:movie_id>/', views.getMovieDetail),
]