from rest_framework.generics import RetrieveUpdateDestroyAPIView

from movies.models import Review
from movies.serializers import ReviewSerializer


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer