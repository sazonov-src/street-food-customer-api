from collections.abc import Iterable, MutableMapping

import items

LINE = tuple[items.Item, int]

class BaseCart:
    def __init__(self, *args: LINE):
        items = ((item, self._get_valid_count(count)) for item, count in args)
        self._lines = dict(items)

    def __len__(self):
        return len(self._lines)

    def __getitem__(self, item: items.Item):
        return self._lines[item]

    def __iter__(self):
        return iter(self._lines)

    @staticmethod
    def _get_valid_count(count: int):
        try:
            count = int(count)
            assert count > 0
        except:
            raise ValueError("Count is not valide")
        return count


class BaseCartView(BaseCart):
    @property
    def total_count(self):
        return sum(self._lines.values())

    @property
    def total_price(self):
        return sum(i.price * c for i, c in self._lines.items())

    @property
    def lines(self) -> Iterable[LINE]:
        return self._lines.items()


class BaseCartMutable(BaseCartView, MutableMapping):
    def __setitem__(self, item, count):
        count = int(count)
        self._lines[item] = count

    def __delitem__(self, item):
        del self._lines[item]
 




class CartNotNutable(BaseCartView):
    pass

class CartMutable(BaseCartMutable):
    pass
