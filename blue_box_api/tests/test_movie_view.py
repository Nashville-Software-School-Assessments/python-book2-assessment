# movie view: R
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from blue_box_api.models import Movie, Box
from blue_box_api.tests.helpers import check_for_assertion_error, format_message


class MovieViewTests(APITestCase):
    """Test Class for the MovieView - Do Not change this file"""

    fixtures = ['fixtures']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        return super().setUp()

    @check_for_assertion_error
    def test_get_all_movies(self):
        """Test the list method on the MovieView
            Expects the length of the returned data to equal
            the count of Movie objects in the database
        """
        response = self.client.get("/movies")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data),
            Movie.objects.count(),
            format_message("HINT: If the query parameter is not in the url, the method should return all movies")
        )

    @check_for_assertion_error
    def test_get_movies_by_box(self):
        """Test to filter movies by the box id"""
        for box in Box.objects.all():
            response = self.client.get(f"/movies?box_id={box.id}")
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(
                len(response.data),
                Movie.objects.filter(boxes__id=box.id).count(),
                format_message("HINT: Make sure the list is correctly filtering by the box id")
            )
