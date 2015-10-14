import unittest
import StringIO
import sys
from random import randint
from test_assets import *
from hw3.simulator import *

class TestEatAllFood(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_eat__all_the_food_in_random_world(self):
        for world_size in range(10, 100):
            new_world = []
            amount_of_food = 0
            for location in range(world_size):
                cell_type = randint(0, 1)
                if cell_type == 0:
                    new_world.append(CELL_EMPTY)
                else:
                    new_world.append(CELL_FOOD)
                    amount_of_food += 1
            set_world(new_world)
            creature_location = randint(0, world_size-1)
            set_creature_location(creature_location)
            starting_hunger = randint(0, amount_of_food)
            set_creature_hunger_level(starting_hunger)
            state_before = "\n[BEFORE] world=\n" + str(get_world()) + "\ncreature=" + str(creature) +"\n"
            eat_all_food()
            state_after = "\n[AFTER] world=\n" + str(get_world()) + "\ncreature=" + str(creature) +"\n"
            food_left = 0
            for index, cell in enumerate(get_world()):
                if cell == CELL_FOOD:
                    food_left += 1
            msg = "\nThis test generates very small and very large worlds and randomy places food in each of them. It then calls the eat_all_food() method.\n" \
                  " When the creature is done eating, this test verifies that the hunger level is reduced exactly by the same amount as the food eaten."
            vars = "world size = " + str(world_size)
            vars += ", starting location = " + str(creature_location)
            vars += ", starting hunger = " + str(starting_hunger)
            vars += ", amount of food = " + str(amount_of_food)
            vars += ", food left = " + str(food_left)
            vars += ", creature hunger level = " + str(get_creature_hunger_level())
            self.assertEqual(starting_hunger-(amount_of_food-food_left), get_creature_hunger_level(),msg+state_before+state_after+vars)
            self.assertEqual(amount_of_food-starting_hunger, food_left, msg+state_before+state_after+vars)


unittest.main()