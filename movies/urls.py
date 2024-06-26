from django.urls import path

from . import views

urlpatterns = [
    path('',views.moviesList,name='movies_list'),
    path('movie/<int:pk>/',views.movieDetail,name='movie_detail'),
]