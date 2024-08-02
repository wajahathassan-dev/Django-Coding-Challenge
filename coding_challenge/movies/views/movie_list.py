from rest_framework.generics import ListCreateAPIView
from rest_framework.exceptions import ValidationError

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.order_by("id")
        runtime_filter = self.request.query_params.get('runtime', None)
        filter_type = self.request.query_params.get('filter_type', 'exact')
        if runtime_filter:
            try:
                runtime = int(runtime_filter)
                if filter_type == 'greater':
                    queryset = queryset.filter(runtime__gt=runtime)
                elif filter_type == 'less':
                    queryset = queryset.filter(runtime__lt=runtime)
                elif filter_type == 'exact':
                    queryset = queryset.filter(runtime=runtime)
                else:
                    # Handle invalid filter_type
                    raise ValidationError("Invalid filter type. Must be 'greater', 'less', or 'exact'.")
            except ValueError:
                # Handle invalid runtime_filter value
                raise ValidationError("Invalid runtime value. Must be an integer.")
        return queryset