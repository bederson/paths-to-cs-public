from hw4_part2.simulator import *
import unittest
import StringIO
import sys
from random import randrange
import pprint
from test_assets import *

class TestDisplayWorld(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_display_random_world(self):
        for test_num in range(0, 100):
            new_world = []
            creature_row = randrange(0, WORLD_DIM)
            creature_col = randrange(0, WORLD_DIM)
            creature[0] = [creature_row, creature_col]

            total_food = 0
            for row in range(WORLD_DIM):
                current_row = []
                for col in range(WORLD_DIM):
                    cell_type = randrange(0, 2)
                    if cell_type == 0:
                        current_row.append(CELL_EMPTY)
                    else:
                        total_food += 1
                        current_row.append(CELL_FOOD)
                new_world.append(current_row)
            world[0:] = new_world
            hunger = randrange(1, total_food + 1)
            set_creature_hunger_level(hunger)
            state_before = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            eat_foods(world, creature)
            state_after = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            food_left = 0
            for index_row, row in enumerate(world):
                for index_col, cell in enumerate(row):
                    if cell == CELL_FOOD:
                        food_left += 1
            msg = "The world contains n foods, but the creature's hunger level is less than n. "+state_before+" After calling eat_foods(world,creature,n), the hunger level should be n-(remaining food)."+state_after
            self.assertEqual(food_left, total_food - hunger, msg)
            self.assertEqual(get_creature_hunger_level(), hunger - (total_food - food_left),msg)

unittest.main()
