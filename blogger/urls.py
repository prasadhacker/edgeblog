from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('postComment', views.postComment, name='postComment'),
    path('', views.blog, name='blogpost'),
    path('<str:slug>', views.blogpost, name='blogpost')
]