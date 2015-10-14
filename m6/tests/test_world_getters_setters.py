import unittest
import StringIO
import sys

from hw6.world import World
from hw6.constants import *


class TestWorldGettersAndSetters(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_get_cell(self):
        world = [[CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY], ]
        test_world = World(WORLD_DIM, NUM_FOODS)
        test_world.grid = world
        self.assertEqual(test_world.get_cell(0, 0), 'FOOD', "Testing get_cell() method on CELL_FODD.")
        self.assertEqual(test_world.get_cell(0, 1), '', "Testing get_cell() method on CELL_EMPTY")

    def test_set_cell(self):
        world = [[CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY], ]
        test_world = World(WORLD_DIM, NUM_FOODS)
        test_world.grid = world
        test_world.set_cell(0, 0, CELL_EMPTY)
        self.assertEqual(test_world.get_cell(0, 0), '', "Testing set_cell() method.")
        test_world.set_cell(0, 0, CELL_FOOD)
        self.assertEqual(test_world.get_cell(0, 0), 'FOOD', "Testing set_cell() method.")

    def test_get_dim(self):
        test_world = World(6, 10)
        self.assertEqual(test_world.get_dim(), 6, "Testing world.get_dim() method.")
        test_world = World(10, 10)
        self.assertEqual(test_world.get_dim(), 10, "Testing world.get_dim() method.")

    def test_get_food_level_empty_cell(self):
        world = [[CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY], ]
        test_world = World(WORLD_DIM, NUM_FOODS)
        test_world.grid = world
        food_level = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0]]
        test_world.food_level = food_level
        self.assertEqual(test_world.get_food_level(0, 0), 0, "Testing get_food_level() method on an empty cell.")


unittest.main()