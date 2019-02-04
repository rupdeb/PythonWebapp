from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(["POST"])
def IdealWeight(heightdata):
    try:
        height=json.loads(heightdata.body)
        weight=str(height*10)
        return JsonResponse("Ideal weight should be:"+weight+" kg",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

# Create your views here.

class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, version):
        print(version)
        content = {'message': 'Hello, World!'}
        return Response(content)