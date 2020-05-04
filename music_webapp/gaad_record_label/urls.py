from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('artist/<int:artist_id>/', views.artist_details, name="artist_detail")
]
