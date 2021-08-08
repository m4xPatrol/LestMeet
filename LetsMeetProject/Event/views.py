from django.shortcuts import render
from .serializer import *
from rest_framework import generics
from .models import EventClass
from .permissions import IsOwnerOrReadOnly


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventDetailSerializer


class EventsListView(generics.ListAPIView):
    serializer_class = EventsListSerializer
    queryset = EventClass.objects.all()


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = EventClass.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
