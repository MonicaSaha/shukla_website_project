from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def index(request):
    context = {}
    return render(request, 'polls/index.html', context)


def projects(request):
    context = {}
    return render(request, 'polls/projects.html', context)


def languages(request):
    context = {}
    return render(request, 'polls/languages.html', context)


def about_us(request):
    context = {}
    return render(request, 'about_us__page/about.html', context)