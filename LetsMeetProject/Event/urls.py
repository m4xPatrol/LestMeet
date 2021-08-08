from django.urls import path, include
from .views import *

app_name = 'event'
urlpatterns = [
    path('event/create/', EventCreateView.as_view()),
    path('all/', EventsListView.as_view()),
    path('event/detail/<int:pk>/', EventDetailView.as_view()),


]
