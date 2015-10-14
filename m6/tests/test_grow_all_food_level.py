import unittest
import StringIO
import sys

from hw6.world import World
from hw6.constants import *


class TestGrowAllFoodLevel(unittest.TestCase):
    def test_grow_all_food_level_once(self):
        world = [[CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY], ]
        food_level = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0]]
        test_world = World(WORLD_DIM, NUM_FOODS)
        test_world.grid = world
        test_world.food_level = food_level
        test_world.grow_all_food_level()
        self.assertEqual(test_world.get_food_level(0, 0), FOOD_GROWTH,  "Testing grow_all_food_level method with one food(level:-1) placed at [0,0].")



unittest.main()