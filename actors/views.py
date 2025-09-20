from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from app.permissions import DefaultPermissions
from .serializers import ActorModelSerializer
from .models import Actor


class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer
    permission_classes = [DefaultPermissions,]


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer
    permission_classes = [DefaultPermissions,]