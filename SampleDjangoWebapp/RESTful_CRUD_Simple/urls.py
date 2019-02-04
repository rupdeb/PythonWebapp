# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:53:31 2019

@author: user
"""

from django.urls import path
from .views import ListSongsView,HelloView


urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('hello/', HelloView.as_view(), name='hello')
]