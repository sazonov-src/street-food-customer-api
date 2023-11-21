from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class MenuItemViewSet(ViewSet):
    def list(self, request):
        return Response({"massage": "hello world"})

