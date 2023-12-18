from app_order.repository import RepositoryOrder
from app_order.models import CartLine
from app_order.serializer import CartLineSerializer

from .utils import validate

class ServiceOrderCart:
    def __init__(self, order: RepositoryOrder) -> None:
        self._order_repo = order

    @property
    def _lines_queryset(self):
        return CartLine.objects.filter(order=self._order_repo.model)

    @validate
    def cart_info(self):
        serializer = CartLineSerializer(
                self._lines_queryset, many=True)
        order = self._order_repo.get()
        return {
            "total_count": order.cart.total_count,
            "total_price": order.cart.total_price,
            "lines": serializer.data,}
