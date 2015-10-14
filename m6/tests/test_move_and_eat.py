import unittest
import StringIO
import sys
from random import randrange

from hw6.creature import Creature
from hw6.world import World
from hw6.constants import *


class TestMoveAndEat(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_move_and_eat_hungry(self):
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
        test_creature = Creature([0, 1], 0)
        test_creature.set_hunger_level(1)
        test_creature.move_and_eat(test_world, [0, 0])
        creature_hunger = test_creature.get_hunger_level()
        creature_location = test_creature.get_location()
        food_level = test_world.get_food_level(0, 0)
        self.assertEqual(0, creature_hunger, "The creature (hunger level:1) moves and eats a food. Then its hunger level becomes 0.")
        self.assertEqual([0, 0], creature_location, "After move_and_eat(world,[0,0]) executed, the creature should be at [0,0].")
        self.assertEqual(FOOD_DEFAULT, food_level, "After move_and_eat(world,[0,0]) executed, the food at [0,0]'s level becomes the default value(-1).")

    def test_move_and_eat_not_hungry(self):
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
        test_creature = Creature([0, 1], 0)
        test_creature.set_hunger_level(0)
        test_creature.move_and_eat(test_world, [0, 0])
        creature_hunger = test_creature.get_hunger_level()
        creature_location = test_creature.get_location()
        food_level = test_world.get_food_level(0, 0)
        self.assertEqual(0, creature_hunger, "The creature (hunger level:0) moves and eats a food. Then its hunger level stays 0.")
        self.assertEqual([0, 1], creature_location, "If not hungry, after move_and_eat(world,[0,0]) executed, the creature should stay at [0,1].")
        self.assertEqual(1, food_level, "If not hungry, the creature does not move and eat the food. Thus the food level stays same (1).")

    def test_move_and_eat_no_food(self):
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
        test_world = World(6, 0)
        test_world.grid = world
        test_world.food_level = food_level
        test_creature = Creature([0, 1], 0)
        test_creature.set_hunger_level(1)
        test_creature.move_and_eat(test_world, [0, 0])
        creature_hunger = test_creature.get_hunger_level()
        creature_location = test_creature.get_location()
        food_level = test_world.get_food_level(0, 0)
        self.assertEqual(1, creature_hunger, "If there's no food at the destination, move_and_eat method does not change the hunger level of the creature.")
        self.assertEqual([0, 1], creature_location, "If there's no food at the destination, move_and_eat method does not change the location of the creature.")
        self.assertEqual('', food_level, "If there's not food at the destination, get_food_level(destination) should return ''.")

unittest.main()