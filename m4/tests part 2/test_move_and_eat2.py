from hw4_part2.simulator import *
import unittest
import StringIO
import sys
import pprint
from random import randrange
from test_assets import *

class TestMoveAndEat(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_move_and_eat_random_locations(self):
        for test_num in range(0, 100):
            world[0:] = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY]]
            creature_row = randrange(0, WORLD_DIM)
            creature_col = randrange(0, WORLD_DIM)
            food_row = randrange(0, WORLD_DIM)
            food_col = randrange(0, WORLD_DIM)
            if([creature_row,creature_col]==[food_row,food_col]):
                continue
            creature[0] = [creature_row, creature_col]
            creature[1] = 1

            set_cell(food_row, food_col, CELL_FOOD)
            state_before = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            move_and_eat(world, creature, [food_row, food_col])
            state_after = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            food_left = 0
            for index_row, row in enumerate(world):
                for index_col, cell in enumerate(row):
                    if cell == CELL_FOOD:
                        food_left += 1
            if abs(creature_row - food_row) + abs(creature_col - food_col) <= 1:
                msg = "The creature (hunger==1) is placed in a random world with one food at an adjacent cell."+state_before+"\n After calling move_and_eat() with the location of that food, the food must be gone and the hunger level should be 0."+state_after
                self.assertEqual(food_left, 0, msg)
                self.assertEqual(get_creature_hunger_level(), 0, msg)
            else:
                msg = "The creature (hunger==1) is placed in a random world with one food at a far cell."+state_before+"\n After calling move_and_eat() with the location of that food, the food must stay there and the hunger level also should stay 1."+ state_after
                self.assertEqual(food_left, 1, msg)
                self.assertEqual(get_creature_hunger_level(), 1, msg)

unittest.main()