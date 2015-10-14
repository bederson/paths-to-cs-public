import unittest
import StringIO
import sys

from hw6.world import World
from hw6.constants import *


class TestResetFoodLevel(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_reset_food_level(self):
        world = [[CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY], ]
        food_level = [[-1, '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', '']]
        test_world = World(WORLD_DIM, NUM_FOODS)
        test_world.grid = world
        test_world.food_level = food_level
        test_world.grow_all_food_level()
        test_world.reset_food_level(0, 0)
        self.assertEqual(test_world.get_food_level(0, 0), FOOD_DEFAULT, "reset_food_level(0,0) will set the food level at (0,0) to the default level.")

    def test_reset_food_level_then_grow(self):
        world = [[CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY], ]
        food_level = [[-1, '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', ''],
                      ['', '', '', '', '', '']]
        test_world = World(WORLD_DIM, NUM_FOODS)
        test_world.grid = world
        test_world.food_level = food_level
        test_world.grow_all_food_level()
        test_world.reset_food_level(0, 0)
        self.assertEqual(test_world.get_food_level(0, 0), FOOD_DEFAULT, "reset_food_level(0,0) will set the food level at (0,0) to the default level.")
        test_world.grow_all_food_level()
        self.assertEqual(test_world.get_food_level(0, 0), FOOD_DEFAULT+FOOD_GROWTH, "grow_all_food_level method will reset the food level at (0,0) to the default level and then increase it by FOOD_GROWTH.")
        test_world.reset_food_level(0, 0)
        self.assertEqual(test_world.get_food_level(0, 0), FOOD_DEFAULT, "reset_food_level(0,0) will set the food level at (0,0) to the default level.")



unittest.main()