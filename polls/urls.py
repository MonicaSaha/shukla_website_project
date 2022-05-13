from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('about/', views.about_us, name='about'),
    path('languages/', views.languages, name='languages'),
    path('projects/', views.projects, name='projects'),
    path('', views.index, name='index')

]
