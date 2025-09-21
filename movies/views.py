from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from app.permissions import DefaultPermissions
from .models import Movie
from .serializers import MovieModelSerializer, MovieListDetailSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    permission_classes = [DefaultPermissions,]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    permission_classes = [DefaultPermissions,]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer