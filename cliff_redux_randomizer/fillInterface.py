import abc
from typing import Optional

from .item import Item
from .loadout import Loadout
from .location import Location


class FillAlgorithm(abc.ABC):
    @abc.abstractmethod
    def __init__(self) -> None:
        """ setup, build item pool, etc. """

    @abc.abstractmethod
    def choose_placement(self, availableLocations: list[Location],
                         loadout: Loadout) -> Optional[tuple[Location, Item]]:
        """ returns (location to place an item, which item to place there) """

    @abc.abstractmethod
    def count_items_remaining(self) -> int:
        """ how many items left to place """

    @abc.abstractmethod
    def remove_from_pool(self, item: Item) -> None:
        """ removes this item from the item pool """
