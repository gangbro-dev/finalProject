from django.urls import path

from . import views

urlpatterns = [
    path('follow/', views.follow),
    path('follow/<str:username>', views.isFollow),
    path('image/', views.addProfileImage),
    path('image/<str:username>', views.getProfileImage),
]