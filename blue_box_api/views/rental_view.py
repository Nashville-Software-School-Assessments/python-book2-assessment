from datetime import date, timedelta
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from blue_box_api.models import Rental, Movie
from blue_box_api.serializers import RentalSerializer


class RentalView(ViewSet):
    """Rental View includes list, retrieve, create, and delete"""
    def create(self, request):
        """Create a new rental, due date is always 2 weeks out"""
        try:
            rental = Rental.objects.create(
                due_date= date.today() + timedelta(days=14),
                movie=Movie.objects.get(pk=request.data['movie']),
                user=request.auth.user
            )
            serializer = RentalSerializer(rental)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        """Get a single rental object"""
        try:
            rental = Rental.objects.get(pk=pk)
            serializer = RentalSerializer(rental)
            return Response(serializer.data)
        except Rental.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """List of the rentals"""
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        """Delete a single rental"""
        try:
            rental = Rental.objects.get(pk=pk)
            rental.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Rental.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
