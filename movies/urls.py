from django.urls import path
from .views import MovieCreateListView, MovieRetrieveUpdateDestroyView


urlpatterns = [
    path('movies/', MovieCreateListView.as_view(), name='movie_create_list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie_update_destroy'),
]