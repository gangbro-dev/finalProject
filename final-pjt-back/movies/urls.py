from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.getMovieList),
    path('<int:movie_id>/', views.getMovieDetail),
    path('<int:movie_id>/comment/', views.comments),
    path('<int:movie_id>/is_liked/', views.clickLikeButton),
    path('like_movies/<str:username>/', views.getLikeMovie),
    path('recommend/', views.get_recommend_list),
]