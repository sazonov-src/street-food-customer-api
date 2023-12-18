from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from app_menu.models import MenuItem
from app_menu.serializer import MenuItemSerializer


class MenuItemViewSet(ViewSet):
    def list(self, request):
        items_queryset = MenuItem.objects.all()
        serializer = MenuItemSerializer(items_queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        items_queryset = MenuItem.objects.get(pk=pk)
        serializer = MenuItemSerializer(items_queryset)
        return Response(serializer.data)


