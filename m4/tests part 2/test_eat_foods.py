from hw4_part2.simulator  import *
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

    def test_eat_foods_one_food_one_hunger(self):
        for test_num in range(0, 100):
            world[0:] = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY]]
            creature_row = randrange(0, WORLD_DIM)
            creature_col = randrange(0, WORLD_DIM)
            creature[0] = [creature_row, creature_col]
            creature[1] = 1
            food_row = randrange(0, WORLD_DIM)
            food_col = randrange(0, WORLD_DIM)
            set_cell(food_row, food_col, CELL_FOOD)
            import pprint
            state_before = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            eat_foods(world, creature)
            state_after = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            food_left = 0
            for index_row, row in enumerate(world):
                for index_col, cell in enumerate(row):
                    if cell == CELL_FOOD:
                        food_left += 1
            msg = "The world contains only one food, and the creature (hunger==1) is placed at a random cell. "+state_before+"After calling eat_foods(world,creature,1), there must be no food in the world and the creature should not be hungry any more."+state_after
            self.assertEqual(food_left, 0, msg)
            self.assertEqual(get_creature_hunger_level(), 0, msg)

    def test_eat_foods_five_food_five_hunger(self):
        for test_num in range(0, 100):
            world[0:] = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY]]
            creature_row = randrange(0, WORLD_DIM)
            creature_col = randrange(0, WORLD_DIM)
            creature[0] = [creature_row, creature_col]
            creature[1] = 5

            set_cell(0, 0, CELL_FOOD)
            set_cell(1, 1, CELL_FOOD)
            set_cell(2, 2, CELL_FOOD)
            set_cell(3, 3, CELL_FOOD)
            set_cell(4, 4, CELL_FOOD)
            state_before = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            eat_foods(world, creature)
            state_after = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            food_left = 0
            for index_row, row in enumerate(world):
                for index_col, cell in enumerate(row):
                    if cell == CELL_FOOD:
                        food_left += 1
            msg = "The world contains five foods, and the creature (hunger==5) is placed at a random cell. "+state_before+"After calling eat_foods(world,creature,5), there must be no food in the world and the creature should not be hungry any more."+state_after
            self.assertEqual(food_left, 0, msg)
            self.assertEqual(get_creature_hunger_level(), 0, msg)

    def test_eat_foods_all_food_all_hunger(self):
        for test_num in range(0, 100):
            world[0:] = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY]]
            creature_row = randrange(0, WORLD_DIM)
            creature_col = randrange(0, WORLD_DIM)
            creature[0] = [creature_row, creature_col]
            creature[1] = 25

            for row in range(0, 5):
                for col in range(0, 5):
                    set_cell(row, col, CELL_FOOD)
            state_before = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            eat_foods(world, creature)
            state_after = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            food_left = 0
            for index_row, row in enumerate(world):
                for index_col, cell in enumerate(row):
                    if cell == CELL_FOOD:
                        food_left += 1
            msg = "The world (with 25 cells) is completely full of foods, and the creature (hunger==25) is placed at a random cell. "+state_before+"After calling eat_foods(world,creature,25), there must be no food in the world and the creature should not be hungry any more."+state_after
            self.assertEqual(food_left, 0, msg)
            self.assertEqual(get_creature_hunger_level(), 0, msg)

    def test_eat_foods_more_hunger_than_food(self):
        for test_num in range(0, 100):
            world[0:] = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY]]
            creature_row = randrange(0, WORLD_DIM)
            creature_col = randrange(0, WORLD_DIM)
            creature[0] = [creature_row, creature_col]
            creature[1] = 30

            for row in range(0, 5):
                for col in range(0, 5):
                    set_cell(row, col, CELL_FOOD)
            state_before = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            eat_foods(world, creature)
            state_after = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            food_left = 0
            for index_row, row in enumerate(world):
                for index_col, cell in enumerate(row):
                    if cell == CELL_FOOD:
                        food_left += 1
            msg = "The world (with 25 cells) is full of foods, and the creature (hunger==30) is placed at a random cell. "+state_before+"After calling eat_foods(world,creature,25), there must be no food in the world and the hunger level should be 5."+state_after
            self.assertEqual(food_left, 0, msg)
            self.assertEqual(get_creature_hunger_level(), 5, msg)

    def test_eat_foods_more_food_than_hunger(self):
        for test_num in range(0, 100):
            world[0:] = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY]]
            creature_row = randrange(0, WORLD_DIM)
            creature_col = randrange(0, WORLD_DIM)
            creature[0] = [creature_row, creature_col]
            creature[1] = 5

            for row in range(0, 5):
                for col in range(0, 5):
                    set_cell(row, col, CELL_FOOD)
            state_before = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            eat_foods(world, creature)
            state_after = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            food_left = 0
            for index_row, row in enumerate(world):
                for index_col, cell in enumerate(row):
                    if cell == CELL_FOOD:
                        food_left += 1
            msg = "The world (with 25 cells) is full of foods, but the creature (hunger==5) is not hungry enough to eat all food. "+state_before+" After calling eat_foods(world,creature,25), 20 foods should remain in the world and the hunger level should be 0."+state_after
            self.assertEqual(food_left, 20, msg)
            self.assertEqual(get_creature_hunger_level(), 0, msg)


unittest.main()
