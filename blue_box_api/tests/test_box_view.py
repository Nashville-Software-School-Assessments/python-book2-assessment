from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from blue_box_api.models import Box
from blue_box_api.serializers import BoxSerializer


class BoxViewTests(APITestCase):
    """Test Class for the BoxView - Do Not change this file"""

    fixtures = ['fixtures']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        return super().setUp()

    def test_get_all_boxes(self):
        """Test the list method on the BoxView
            Expects the length of the returned data to equal
            the count of Box objects in the database
        """
        response = self.client.get("/boxes")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Box.objects.count())

    def test_retrieve_single_box(self):
        """Tests the retrieve method on BoxView
            Expects the data to be a dictionary of the box object with the correct id
        """
        box_id = 1
        box = Box.objects.get(pk=box_id)
        actual = BoxSerializer(box)
        response = self.client.get(f'/boxes/{box_id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, actual.data)
