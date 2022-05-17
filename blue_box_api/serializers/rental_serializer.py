from rest_framework import serializers
from blue_box_api.models import Rental


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'
        depth = 1
