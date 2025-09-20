from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Movie
from .serializers import MovieModelSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated,]
        else:
            permission_classes = [IsAdminUser,]
        return [permission() for permission in permission_classes]

