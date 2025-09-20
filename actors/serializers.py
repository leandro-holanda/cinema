from rest_framework import serializers
from datetime import date
from .models import Actor


class ActorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


    def validate_birthday(self, value):
        today = date.today()
        age = today.year - value.year

        if value > date.today():
            raise serializers.ValidationError("A data de nascimento não pode ser no futuro.")
        return value