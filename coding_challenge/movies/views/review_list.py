from rest_framework.generics import ListCreateAPIView

from movies.models import Review
from movies.serializers import ReviewSerializer


class ReviewListView(ListCreateAPIView):
    queryset = Review.objects.order_by("id")
    serializer_class = ReviewSerializer
