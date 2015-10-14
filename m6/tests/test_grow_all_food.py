import unittest
from random import randrange
from hw6.world import World
from hw6.constants import *


class TestWorld(unittest.TestCase):
    def test_grow_all_food_level_one_food_random_worlds(self):
        world = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
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
        food_row = randrange(0, WORLD_DIM - 1)
        food_col = randrange(0, WORLD_DIM - 1)
        test_world.set_cell(food_row, food_col, CELL_FOOD)
        test_world.food_level[food_row][food_col] = FOOD_DEFAULT
        test_world.grow_all_food_level()
        for row_index, row in enumerate(test_world.grid):
            for cell_index, cell in enumerate(row):
                if cell == CELL_FOOD:
                    self.assertEqual(test_world.get_food_level(row_index, cell_index), FOOD_GROWTH, "Testing grow_all_food_level method.")
                else:
                    self.assertEqual(test_world.get_food_level(row_index, cell_index), 0, "Testing grow_all_food_level method - if the cell does not have food, get_food_level method returns 0.")

    def test_grow_all_food_level_random_worlds_more_food(self):
        world = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
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

        for test_num in range(100):
            food_row = randrange(0, WORLD_DIM - 1)
            food_col = randrange(0, WORLD_DIM - 1)
            test_world.set_cell(food_row, food_col, CELL_FOOD)
            test_world.food_level[food_row][food_col] = FOOD_DEFAULT

            prev_food_level = []
            for row in test_world.food_level:
                prev_food_level.append(list(row))

            test_world.grow_all_food_level()

            for row_index, row in enumerate(test_world.grid):
                for cell_index, cell in enumerate(row):
                    if cell == CELL_FOOD:
                        prev_val = prev_food_level[row_index][cell_index]
                        self.assertEqual(test_world.get_food_level(row_index, cell_index), prev_val + FOOD_GROWTH, "Testing grow_all_food_level method.")
                    else:
                        self.assertEqual(test_world.get_food_level(row_index, cell_index), 0, "Testing grow_all_food_level method - if the cell does not have food, get_food_level method returns 0.")

unittest.main()
