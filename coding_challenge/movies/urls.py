from django.urls import path

from movies.views import MovieListView, MovieDetailView, ReviewListView, ReviewDetailView

urlpatterns = [
    path("", MovieListView.as_view(), name="MovieListView"),
    path("<int:pk>", MovieDetailView.as_view(), name="MovieDetailView"),

    path("review/", ReviewListView.as_view(), name="ReviewListView"),
    path("review/<int:pk>", ReviewDetailView.as_view(), name="ReviewDetailView"),
]
