from rest_framework import serializers
from genres.serializers import GenreModelSerializer
from actors.serializers import ActorModelSerializer
from .models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

    
    def validate_duration_minutes(self, value):
        if value <= 0:
            raise serializers.ValidationError("A duração deve ser maior que zero.")
        if value > 600:
            raise serializers.ValidationError("A duração não pode ultrapassar 600 minutos.")
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorModelSerializer(many=True)
    genre = GenreModelSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'duration_minutes',
        'resume', 'poster',]

    