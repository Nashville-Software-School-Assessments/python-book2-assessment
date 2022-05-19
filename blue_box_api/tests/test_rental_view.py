from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from blue_box_api.models import Rental, Movie
from blue_box_api.serializers import RentalSerializer
from blue_box_api.tests.helpers import check_for_assertion_error, format_message


class RentalViewTests(APITestCase):
    """Test Class for the RentalView - Do Not change this file"""

    fixtures = ['fixtures']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        return super().setUp()

    @check_for_assertion_error
    def test_get_all_rentals(self):
        """Test the list method on the RentalView
            Expects the length of the returned data to equal
            the count of Rental objects in the database
        """
        response = self.client.get("/rentals")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Rental.objects.count())

    @check_for_assertion_error
    def test_retrieve_single_rental(self):
        """Tests the retrieve method on RentalView
            Expects the data to be a dictionary of the rental object with the correct id
        """
        
        for rental in Rental.objects.all():
            expected = RentalSerializer(rental)
            response = self.client.get(f'/rentals/{rental.id}')
            self.assertEqual(
                status.HTTP_200_OK,
                response.status_code,
                format_message("HINT: RentalView retrieve does not return a 200. Check the method for errors")
            )
            self.assertEqual(
                expected.data,
                response.data,
                format_message("HINT: RentalView retrieve does not return the expected rental. Are you `get`-ing by the right id?")
            )

    @check_for_assertion_error
    def test_delete_rental(self):
        """Test the delete method on RentalView
            Expects the rental to be deleted from the database
        """
        rental_id = Rental.objects.first().id
        response = self.client.delete(f'/rentals/{rental_id}')
        self.assertEqual(
            status.HTTP_204_NO_CONTENT,
            response.status_code,
            format_message("HINT: RentalView destroy does not return the correct status either complete the code or check the status returned by the Response")
        )
        with self.assertRaises(
            Rental.DoesNotExist,
            msg=format_message("HINT: The Rental destroy method did not successfully delete the rental")
        ):
            Rental.objects.get(pk=rental_id)

    @check_for_assertion_error
    def test_create_rental(self):
        """Test the create method on RentalView
            Expects the status_code to be 201 and the rental object should be added to the database
        """
        rental_data = {
            "movie": Movie.objects.first().id
        }
        response = self.client.post('/rentals', rental_data, format='json')

        self.assertEqual(
            status.HTTP_201_CREATED,
            response.status_code,
            format_message("HINT: The create method did not return a 201. What is the status of the Response")
        )

        self.assertIsNotNone(response.data['id'])

        new_rental = Rental.objects.get(pk=response.data['id'])
        expected = RentalSerializer(new_rental)
        self.assertEqual(
            expected.data,
            response.data,
            format_message("HINT: The create method should return the serialized data for the new rental object")
        )

        self.assertEqual(
            rental_data['movie'],
            new_rental.movie_id,
            format_message("HINT: The movie added to the rental does not match the movie passed to the create method")
        )

    @check_for_assertion_error
    def test_my_rentals_in_expected_order(self):
        """Test that the my_rentals custom action returns the rentals for the logged in user"""
        for user in User.objects.all():
            token = Token.objects.get(user=user)
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

            response = self.client.get("/rentals/my_rentals")
            self.assertEqual(
                status.HTTP_200_OK,
                response.status_code,
                format_message("HINT: The custom action did not return a 200. Check the method decorator and method name for errors. This should not be a detail route")
            )

            filtered = Rental.objects.filter(user=user)
            expected = RentalSerializer(filtered, many=True)
            self.assertEqual(
                expected.data,
                response.data,
                format_message("HINT: Make sure the rentals being returned are only for the logged in user")
            )
