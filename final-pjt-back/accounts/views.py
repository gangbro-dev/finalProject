import base64
import os

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User


# Create your views here.
@api_view(['GET'])
def getProfileImage(request, username):
    data = User.objects.get(username=username).profile_image
    return Response(str(data), status=status.HTTP_200_OK)


@api_view(['PUT',])
def addProfileImage(request):
    user = request.user
    if str(request.data['image']) == 'undefined':
        return Response(status=status.HTTP_404_NOT_FOUND)
    user.profile_image = request.data['image']
    user.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(["GET"])
def isFollow(request, username):
    profile_user = User.objects.get(username=username)
    followerCount = len(profile_user.followers.all())
    followingCount = len(profile_user.followings.all())
    if request.user in profile_user.followings.all():
        isFollowed = True
    else:
        isFollowed = False
    data = {
        'followerCount': followerCount,
        'followingCount': followingCount,
        "isFollowed": isFollowed,
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(["POST",])
def follow(request):
    if request.method == "POST":
        profile_user = User.objects.get(username=request.data['user'])
        if request.user == profile_user:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if request.user in profile_user.followings.all():
            profile_user.followings.remove(request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            profile_user.followings.add(request.user)
            return Response(status=status.HTTP_201_CREATED)