# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""



""" Imports """
from django.urls import path, re_path
from apps.home import views



""" urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    
    #path("/ready", views.ready_chat, name='ready'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

] """



""" Patterns """
home_patterns = ([
    # The home page
    path('', views.index, name='home'),
    
    path("ready/", views.ready_chat, name='ready'),
    
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    
], 'home_patterns')

