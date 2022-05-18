from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from blue_box_api.models import Movie
from blue_box_api.serializers import MovieSerializer


class MovieView(ViewSet):
    """Movie view includes list"""
    def list(self, request):
        """Get list of movies"""
        movies = Movie.objects.all()
        # TODO: Add a filter for the box_id
        
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
