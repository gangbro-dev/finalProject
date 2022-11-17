from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.getMovieList),
    path('<int:movie_id>/', views.getMovieDetail),
    path('<int:movie_id>/comment/', views.getComments),
]