from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from app.permissions import DefaultPermissions
from .serializers import GenreModelSerializer
from .models import Genre


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer
    permission_classes = [DefaultPermissions,]

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer
    permission_classes = [DefaultPermissions,]
