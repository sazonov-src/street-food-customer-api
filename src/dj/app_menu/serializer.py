from dj.serializers import BaseModelSerializer
from app_menu.models import MenuItem

class MenuItemSerializer(BaseModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
