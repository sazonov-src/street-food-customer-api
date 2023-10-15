
from dataclasses import dataclass


@dataclass(frozen=True)
class OrderLine:
    item: int
    count: int
