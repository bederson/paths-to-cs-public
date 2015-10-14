import unittest
import StringIO
import sys
from random import randrange

from hw6.creature import Creature
from hw6.world import World
from hw6.constants import *


class TestLegalMoveFindNearbyFood(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_legal_move(self):
        world = [[CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY], ]
        test_world = World(WORLD_DIM, NUM_FOODS)
        test_world.grid = world
        test_creature = Creature([0, 0], 0)
        self.assertTrue(test_creature.legal_move(test_world, (0, 0)), "Testing legal_move method for (0,0) - legal.")
        self.assertTrue(test_creature.legal_move(test_world, (5, 5)), "Testing legal_move method for (5,5) - legal.")
        self.assertFalse(test_creature.legal_move(test_world, (-1, -1)), "Testing legal_move method for (-1,-1) - illegal.")
        self.assertFalse(test_creature.legal_move(test_world, (6, 6)), "Testing legal_move method for (6,6) - illegal.")

    def test_find_single_nearby_food_(self):
        world = [[CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY], ]
        food_level = [[1, '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', '']]
        test_world = World(WORLD_DIM, NUM_FOODS)
        test_world.grid = world
        test_world.food_level = food_level
        test_creature = Creature((0, 1), 0)
        proper_output = [0, 0]
        submission_output = test_creature.find_nearby_food(test_world)
        self.assertEqual(proper_output, submission_output, "When creature is at (0,1) and food is on (0,0), find_nearby_food should return [0,0].")

    def test_cant_find_far_food_(self):
        world = [[CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY], ]
        food_level = [[1, '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', '']]
        test_world = World(6, 1)
        test_world.grid = world
        test_world.food_level = food_level
        test_creature = Creature([4, 4], 0)
        proper_output = None
        submission_output = test_creature.find_nearby_food(test_world)
        self.assertEqual(proper_output, submission_output, "When the food is far away from the creature, find_nearby_food should return None.")

unittest.main()