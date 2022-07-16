from django.contrib import admin
from django.urls import path
from host import views
urlpatterns = [
    path("" , views.index, name = "host")
]
