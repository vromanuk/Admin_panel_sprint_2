from api.v1 import views
from django.urls import path

urlpatterns = [
    path("movies/", views.Movies.as_view(), name="movies_list"),
    path("movies/<uuid:uuid>", views.MoviesDetailApi.as_view(), name="movie_detail"),
]
