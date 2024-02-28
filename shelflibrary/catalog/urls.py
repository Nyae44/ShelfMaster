# This is where we will add our urls as we develop our application
from django.urls import path
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('',views.index, name='index'),
    path('books/', views.BookListView.as_view(),name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name = 'book-detail'),
    path('authors/', views.AuthorsListView.as_view(), name = 'authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(),name = 'author-detail'),
    
    
    #repath(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail')

]