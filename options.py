from typing import Union

from .cliff_redux_randomizer.defaultLogic import Default
from .cliff_redux_randomizer.game import Game

from worlds.cliffredux.location import location_data


def make_cliff_game(seed: Union[int, None])-> Game:
    seed = seed or 0
    cr_game = Game(Default,location_data,seed)
    return cr_game
