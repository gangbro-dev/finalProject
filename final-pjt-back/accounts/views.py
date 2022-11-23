import base64
import os

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['PUT',])
def addProfileImage(request):
    user = request.user
    print(request.data)
    user.profile_image = request.data['image']
    user.save()
    return Response(status=status.HTTP_201_CREATED)