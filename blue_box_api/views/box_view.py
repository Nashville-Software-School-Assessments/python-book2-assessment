# box view: R
# get list of movies by box
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from blue_box_api.models import Box
from blue_box_api.serializers import BoxSerializer


class BoxView(ViewSet):
    """Box View - includes list and retrieve views"""
    def list(self, request):
        """Get a list of all boxes"""
        boxes = Box.objects.all()
        serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Get a single box"""
        try:
            box = Box.objects.get(pk=pk)
            serializer = BoxSerializer(box)
            return Response(serializer.data)
        except Box.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
