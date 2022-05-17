# movie view: R
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from blue_box_api.models import Movie
from blue_box_api.serializers import MovieSerializer


class MovieViewTests(APITestCase):
    """Test Class for the MovieView - Do Not change this file"""

    fixtures = ['fixtures']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        return super().setUp()

    def test_get_all_movies(self):
        """Test the list method on the MovieView
            Expects the length of the returned data to equal
            the count of Movie objects in the database
        """
        response = self.client.get("/movies")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Movie.objects.count())

    def test_retrieve_single_movie(self):
        """Tests the retrieve method on MovieView
            Expects the data to be a dictionary of the movie object with the correct id
        """
        movie_id = 1
        movie = Movie.objects.get(pk=movie_id)
        actual = MovieSerializer(movie)
        response = self.client.get(f'/movies/{movie_id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, actual.data)

