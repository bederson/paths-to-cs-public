from hw4_part2.simulator import *
import unittest
import StringIO
import sys
from random import randrange
import pprint
from test_assets import *

class TestWander(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_wander_basic(self):
        world[0:] = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],]
        creature_row = randrange(0, WORLD_DIM)
        creature_col = randrange(0, WORLD_DIM)
        creature[0] = [creature_row, creature_col]
        creature[1] = 0
        old_location = get_creature_location()
        state_before = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
        wander(world, creature)
        state_after = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
        new_location = get_creature_location()
        msg = "When wander(words,creature) is called, the creature will move to one of adjacent cells. before wander():"+state_before+"after wander():"+state_after
        self.assertTrue(abs(old_location[0] - new_location[0]) <= 1 and abs(old_location[1] - new_location[1]) <= 1, msg)

unittest.main()