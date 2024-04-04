from typing import Iterator, Tuple

from .cliff_redux_randomizer.defaultLogic import phantoon, ridley, blueTower, gt
from .cliff_redux_randomizer.game import Game
from .cliff_redux_randomizer.loadout import Loadout
from .cliff_redux_randomizer.logic_shortcut import LogicShortcut

from BaseClasses import CollectionState

from .item import name_to_id as item_name_to_id, id_to_cliff_item


can_win = LogicShortcut(lambda loadout: (
        (phantoon in loadout) and (ridley in loadout) and (blueTower in loadout) and (gt in loadout) #I guess
))

def item_counts(cs: CollectionState, p: int) -> Iterator[Tuple[str, int]]:
    """
    the items that player p has collected

    ((item_name, count), (item_name, count), ...)
    """
    return ((item_name, cs.count(item_name, p)) for item_name in item_name_to_id)


def cs_to_loadout(cr_game: Game, collection_state: CollectionState, player: int) -> Loadout:
    """ convert Archipelago CollectionState to cliff_redux_randomizer loadout state """
    loadout = Loadout(cr_game)
    for item_name, count in item_counts(collection_state, player):
        loadout.contents[id_to_cliff_item[item_name_to_id[item_name]]] += count
    return loadout
