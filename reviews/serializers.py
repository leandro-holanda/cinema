from rest_framework import serializers
from reviews.models import Review


class ReviewModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['movie', 'stars', 'comment',]