from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from blue_box_api.models import Rental, Movie
from blue_box_api.serializers import RentalSerializer


class RentalViewTests(APITestCase):
    """Test Class for the RentalView - Do Not change this file"""

    fixtures = ['fixtures']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        return super().setUp()

    def test_get_all_rentals(self):
        """Test the list method on the RentalView
            Expects the length of the returned data to equal
            the count of Rental objects in the database
        """
        response = self.client.get("/rentals")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Rental.objects.count())

    def test_retrieve_single_rental(self):
        """Tests the retrieve method on RentalView
            Expects the data to be a dictionary of the rental object with the correct id
        """
        rental_id = 1
        rental = Rental.objects.get(pk=rental_id)
        actual = RentalSerializer(rental)
        response = self.client.get(f'/rentals/{rental_id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, actual.data)

    def test_delete_rental(self):
        """Test the delete method on RentalView
            Expects the rental to be deleted from the database
        """
        rental_id = Rental.objects.first().id
        response = self.client.delete(f'/rentals/{rental_id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Rental.DoesNotExist):
            Rental.objects.get(pk=rental_id)

    def test_create_rental(self):
        """Test the create method on RentalView
            Expects the status_code to be 201 and the rental object should be added to the database
        """
        rental_data = {
            "movie": Movie.objects.first().id
        }
        response = self.client.post('/rentals', rental_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['id'])

        new_rental = Rental.objects.get(pk=response.data['id'])
        actual = RentalSerializer(new_rental)
        self.assertEqual(response.data, actual.data)
