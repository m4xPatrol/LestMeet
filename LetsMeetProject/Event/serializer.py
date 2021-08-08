from rest_framework import serializers
from .models import EventClass


class EventDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = EventClass
        fields = '__all__'


class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventClass
        fields = ('id', 'heading', 'image', 'user')

