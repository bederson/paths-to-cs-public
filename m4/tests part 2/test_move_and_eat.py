from hw4_part2.simulator import *
import unittest
import StringIO
import sys
from random import randrange
import pprint
from test_assets import *

class TestMoveAndEat(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_move_and_eat_hungry(self):
        world[0:] = [[CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY]]
        creature[0] = [0, 0]
        creature[1] = 1
        state_before= "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
        move_and_eat(world, creature, [0, 1])
        state_after= "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
        food_left = 0
        for index_row, row in enumerate(world):
            for index_col, cell in enumerate(row):
                if cell == CELL_FOOD:
                    food_left += 1
        msg = "The creature (hunger==1) moves to the nearby food (the only food in the world) and eats it by using move_and_eat()."+state_before+" After eating the food, there's no food left in the world and the hunger level becomes 0."+state_after
        self.assertEqual(food_left, 0, msg)
        self.assertEqual(get_creature_hunger_level(), 0, msg)

    def test_move_and_eat_not_hungry(self):
        world[0:] = [[CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY]]
        creature[0] = [0, 0]
        creature[1] = 0
        state_before= "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
        move_and_eat(world, creature, [0, 1])
        state_after= "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
        food_left = 0
        for index_row, row in enumerate(world):
            for index_col, cell in enumerate(row):
                if cell == CELL_FOOD:
                    food_left += 1
        msg = "The creature (hunger==0) moves to the nearby food (the only food in the world) and tries to eat it by using move_and_eat(). "+state_before+"After that, the food is still there in the world and the hunger level stays 0."+state_after
        self.assertEqual(food_left, 1, msg)
        self.assertEqual(get_creature_hunger_level(), 0, msg)

    def test_move_and_eat_no_food_near(self):
        world[0:] = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD]]
        creature[0] = [0, 0]
        creature[1] = 1
        state_before= "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
        move_and_eat(world, creature, [0, 1])
        state_after= "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
        food_left = 0
        for index_row, row in enumerate(world):
            for index_col, cell in enumerate(row):
                if cell == CELL_FOOD:
                    food_left += 1
        self.assertEqual(food_left, 1, "Before move_and_eat(): "+state_before+"\nAfter move_and_eat():"+state_after)
        self.assertEqual(get_creature_hunger_level(), 1)

    def test_move_and_eat_out_of_bounds_location(self):
        world[0:] = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD]]
        creature[0] = [0, 0]
        creature[1] = 1
        state_before= "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
        result = move_and_eat(world, creature, [2, 2])
        state_after= "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
        # TODO: This is a bad test as there is no requirement that the code returns None if it doesn't eat
        # some students returned False. In any case, clean up requirements and check this outcome better.
        self.assertEqual(result, None, state_before+"move_and_eat() is called with the location([2,2]) of an empty cell, so it should return None. But the result is"+state_after)

unittest.main()