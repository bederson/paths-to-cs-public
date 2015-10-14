import unittest
import StringIO
import sys
from random import randrange

from hw6.creature import Creature
from hw6.world import World
from hw6.constants import *


class TestWander(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_wander_basic(self):
        world = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY], ]
        test_world = World(6, 1)
        test_world.grid = world
        creature_row = randrange(0, WORLD_DIM)
        creature_col = randrange(0, WORLD_DIM)
        test_creature = Creature([creature_row, creature_col], 0)
        old_location = test_creature.get_location()
        test_creature.wander(test_world)
        new_location = test_creature.get_location()
        self.assertTrue(abs(old_location[0] - new_location[0]) <= 1 and abs(old_location[1] - new_location[1]) <= 1, "creature.wander() method moves the creature to an adjacent cell. The total difference of x and y coordinates (before and after wander()) should be equal or less than 1. ")



unittest.main()