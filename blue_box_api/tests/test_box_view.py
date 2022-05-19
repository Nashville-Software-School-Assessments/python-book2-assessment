from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from blue_box_api.models import Box
from blue_box_api.tests.helpers import check_for_assertion_error, format_message


class BoxViewTests(APITestCase):
    """Test Class for the BoxView - Do Not change this file"""

    fixtures = ['fixtures']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        return super().setUp()

    @check_for_assertion_error
    def test_get_all_boxes(self):
        """Test the list method on the BoxView
            Expects the length of the returned data to equal
            the count of Box objects in the database
        """
        response = self.client.get("/boxes")
        self.assertEqual(
            status.HTTP_200_OK,
            response.status_code,
            format_message("HINT: Boxview list method did not return a 200 status. Are you able to get the list in postman?")
        )

        self.assertEqual(
            Box.objects.count(),
            len(response.data),
            format_message("HINT: BoxView list method did not return the expected number of objects. Are you getting all of the boxes?")
        )

        self.assertTrue(
            all('movies' in box for box in response.data),
            format_message("HINT: BoxView list method did not include the list of movies associated with each box")
        )
