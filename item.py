from collections import defaultdict
from typing import Dict, Iterator

from BaseClasses import Item, ItemClassification as IC

from .config import base_id

from .cliff_redux_randomizer.item import Item as CliffItem, Items
from .cliff_redux_randomizer.fillAssumed import FillAssumed

classifications: Dict[str, IC] = defaultdict(lambda: IC.progression)
classifications.update({
    Items.Reserve[0]: IC.useful,
    Items.PowerBomb[0]: IC.useful,
    Items.Energy[0]: IC.useful,  # 12 progression set by create_items
    Items.Super[0]: IC.useful,  # 5 progression set by create_items
    Items.Missile[0]: IC.useful  # 1 progression set by create_items
})


class CliffReduxItem(Item):
    game = "Cliffhanger Redux"
    __slots__ = ("cliff_item",)
    cliff_item: CliffItem

    def __init__(self, name: str, player: int) -> None:
        classification = classifications[name]
        code = name_to_id[name]
        super().__init__(name, classification, code, player)
        self.cliff_item = id_to_cliff_item[code]


local_id_to_cliff_item: Dict[int, CliffItem] = {
    0x00: Items.Missile,
    0x01: Items.Super,
    0x02: Items.PowerBomb,
    0x03: Items.Morph,
    0x04: Items.Springball,
    0x05: Items.Bombs,
    0x06: Items.HiJump,
    0x07: Items.GravitySuit,
    0x08: Items.Varia,
    0x09: Items.Wave,
    0x0a: Items.SpeedBooster,
    0x0b: Items.Spazer,
    0x0c: Items.Ice,
    0x0d: Items.Grapple,
    0x0e: Items.Plasma,
    0x0f: Items.Screw,
    0x10: Items.Charge,
    0x11: Items.SpaceJump,
    0x12: Items.Energy,
    0x13: Items.Reserve,
    0x14: Items.Xray
}


id_to_cliff_item = {
    id_ + base_id: item
    for id_, item in local_id_to_cliff_item.items()
}

name_to_id = {
    item[0]: id_
    for id_, item in id_to_cliff_item.items()
}


def names_for_item_pool() -> Iterator[str]:
    cliff_fill = FillAssumed()
    for cliff_item in cliff_fill.prog_items:
        yield cliff_item[0]
    for cliff_item in cliff_fill.extra_items:
        yield cliff_item[0]
