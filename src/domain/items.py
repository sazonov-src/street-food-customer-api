from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Item:
    title: str
    description: str
    price: float
