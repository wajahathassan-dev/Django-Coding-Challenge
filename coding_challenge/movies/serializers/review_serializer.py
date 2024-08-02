from rest_framework import serializers
from movies.models import Review, Movie

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'movie', 'name', 'rating')