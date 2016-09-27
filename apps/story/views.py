from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

def index(request):

    return render(request, 'story/index.html')


def map(request):

    return render(request, 'story/map.html')

def add_story(request):

    return render(request, 'story/add_story.html')
