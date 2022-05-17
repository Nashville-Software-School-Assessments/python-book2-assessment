from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from blue_box_api.models import Movie
from blue_box_api.serializers import MovieSerializer


class MovieView(ViewSet):
    """Movie view includes list and retrieve"""
    def retrieve(self, request, pk):
        """Retrieve a single movie object"""
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Get list of movies"""
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
