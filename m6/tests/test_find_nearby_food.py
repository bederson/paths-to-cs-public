import unittest
from random import randrange, choice

from hw6.creature import Creature
from hw6.world import World
from hw6.constants import *


class ReleaseTestFindNearbyFoodAndInBounds(unittest.TestCase):

    def test_find_single_nearby_food_(self):
        for test_num in range(0, 100):
            world = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY], ]
            food_level = [['', '', '', '', '', ''],
                          ['', '', '', '', '', ''],
                          ['', '', '', '', '', ''],
                          ['', '', '', '', '', ''],
                          ['', '', '', '', '', ''],
                          ['', '', '', '', '', '']]
            test_world = World(WORLD_DIM, NUM_FOODS)
            test_world.grid = world
            test_world.food_level = food_level
            creature_row = randrange(0, WORLD_DIM - 1)
            creature_col = randrange(0, WORLD_DIM - 1)
            test_creature = Creature((creature_row, creature_col), 0)
            food_location = [-1, -1]
            while not test_creature.legal_move(test_world, food_location):
                food_direction = choice([[1, 0], [-1, 0], [0, 1], [0, -1]])
                food_location = [creature_row - food_direction[0], creature_col - food_direction[1]]
                test_world.set_cell(food_location[0], food_location[1], CELL_FOOD)
                test_world.reset_food_level(food_location[0], food_location[1])
            test_world.grow_all_food_level()
            submission_output = test_creature.find_nearby_food(test_world)
            proper_output = food_location
            self.assertEqual(proper_output, submission_output, "The test randomly places a food on one of the cells adjacent to the creature. Then test find_nearby_food method.")




unittest.main()