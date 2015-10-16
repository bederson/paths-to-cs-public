import unittest
from random import randrange

from hw6.creature import Creature
from hw6.world import World
from hw6.constants import *


class ReleaseTestMoveAndEat(unittest.TestCase):

    def test_move_and_eat_random_locations_hungry(self):
        for test_num in range(0, 100):
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
            creature_row = randrange(0, WORLD_DIM - 1)
            creature_col = randrange(0, WORLD_DIM - 1)
            test_creature = Creature((creature_row, creature_col), 1)
            food_row = randrange(0, WORLD_DIM - 1)
            food_col = randrange(0, WORLD_DIM - 1)
            food_location = [food_row, food_col]
            test_world.set_cell(food_location[0], food_location[1], CELL_FOOD)
            food_level[food_row][food_col] = FOOD_GROWTH
            test_creature.move_and_eat(test_world, food_location)
            self.assertEqual(test_creature.get_hunger_level(), 1 - FOOD_GROWTH,"A creature (hunger level:1) at a random position moves and eat a food (level:0.025). Then the creature's hunger level becomes 1-0.025")
            self.assertEqual(test_world.get_food_level(food_row, food_col), FOOD_DEFAULT, "After being eaten, the food level goes back to the FOOD_DEFAULT value.")

    def test_move_and_eat_random_locations_not_hungry(self):
        for test_num in range(0, 100):
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
            creature_row = randrange(0, WORLD_DIM - 1)
            creature_col = randrange(0, WORLD_DIM - 1)
            test_creature = Creature((creature_row, creature_col), 0)
            food_row = randrange(0, WORLD_DIM - 1)
            food_col = randrange(0, WORLD_DIM - 1)
            food_location = [food_row, food_col]
            test_world.set_cell(food_location[0], food_location[1], CELL_FOOD)
            food_level[food_row][food_col] = FOOD_GROWTH
            test_creature.move_and_eat(test_world, food_location)
            self.assertEqual(test_creature.get_hunger_level(), 0, "If the creature is not hungry, move_and_eat method does not change its hunger level.")
            self.assertEqual(test_world.get_food_level(food_row, food_col), FOOD_GROWTH, "If the creature is not hungry, move_and_eat method does not change the level of the food.")


unittest.main()