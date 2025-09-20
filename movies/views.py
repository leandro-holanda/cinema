from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from app.permissions import DefaultPermissions
from .models import Movie
from .serializers import MovieModelSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    permission_classes = [DefaultPermissions,]

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    permission_classes = [DefaultPermissions,]
