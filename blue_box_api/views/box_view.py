from rest_framework.viewsets import ViewSet


class BoxView(ViewSet):
    """Box View - includes list and retrieve views"""

    def list(self, request):
        """Get a list of all boxes"""
        # TODO: Complete the list method
