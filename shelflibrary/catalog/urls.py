# This is where we will add our urls as we develop our application
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index')
]