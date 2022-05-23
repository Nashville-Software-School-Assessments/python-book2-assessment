from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from blue_box_api.models import Rental
from blue_box_api.serializers import RentalSerializer


class RentalView(ViewSet):
    """Rental View includes list, retrieve, create, and delete"""
    def create(self, request):
        """Create a new rental, due date is always 2 weeks out"""
        # TODO: Complete the create method

    def retrieve(self, request, pk):
        """Get a single rental object"""
        # TODO: Complete the retrieve method

    def list(self, request):
        """List of the rentals"""
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Delete a single rental"""
        # TODO: Complete the destroy method

    
    # TODO: Add a custom GET action named my_rentals that gets the rentals for the current user
