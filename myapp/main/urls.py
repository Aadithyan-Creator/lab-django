from django.urls import path
from .views import create_user
from django.shortcuts import render, redirect

urlpatterns = [
    path("", create_user, name='register'),
    path("sucess/", lambda request: render(request, "success.html"), name="success_page"),
]
