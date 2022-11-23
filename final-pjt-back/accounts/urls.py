from django.urls import path

from . import views

urlpatterns = [
    # path('follow/'),
    path('image/', views.addProfileImage),
]