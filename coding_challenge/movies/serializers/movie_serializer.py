from rest_framework import serializers
from .review_serializer import ReviewSerializer 

from movies.models import Movie, Review


class MovieSerializer(serializers.ModelSerializer):
    runtime_formatted = serializers.SerializerMethodField()
    reviewers = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "release_date",
            "runtime_formatted",
            "reviewers",
            "avg_rating"
        )
    
    def get_runtime_formatted(self, obj):
        hours, minutes = divmod(obj.runtime, 60)
        return f"{hours}:{minutes}"
    
    def get_reviewers(self, obj):
        reviews = Review.objects.filter(movie=obj.id)
        serializer = ReviewSerializer(reviews, many=True)    
        return serializer.data
    
    def get_avg_rating(self, obj):
        ratings = list(Review.objects.filter(movie=obj.id).values_list("rating", flat=True))
        if len(ratings) == 0:
            return None
        avg_rating = sum(ratings)/len(ratings)
        return round(avg_rating, 2)