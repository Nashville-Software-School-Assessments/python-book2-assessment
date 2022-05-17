from rest_framework import serializers
from blue_box_api.models import Box
class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'
        depth = 1
