from hw4_part2.simulator import *
import unittest
from random import randrange
from random import choice
import pprint
from test_assets import *

class TestFindNearbyFoodAndInBounds(unittest.TestCase):
    def test_find_single_nearby_food_(self):
        world[0:] = [[CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY]]
        set_creature_location([0, 0])
        proper_output = [0, 1]
        state_before= "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
        submission_output = find_nearby_food(world, creature)
        comparison = "\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
        msg = state_before+"The creature is at (0,0), and the food is at (0,1). find_nearby_food(world) should return the correct location of the food (0,1)."+comparison
        self.assertEqual(proper_output, submission_output, msg)

    def test_find_single_far_food(self):
        world[0:] = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD]]

        set_creature_location([0, 0])
        proper_output = None
        state_before = "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
        submission_output = find_nearby_food(world, creature)
        comparison = "\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
        msg = state_before+"The creature is at (0,0), and the food is at (5,5). find_nearby_food(world) cannot find the food, and should return None."+comparison
        self.assertEqual(proper_output, submission_output, msg)

    def test_in_bounds(self):
        world[0:] = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                     [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD]]
        msg = "For a 5x5 world, tests in_bounds() to ensure that [0, 0] is in the world."
        self.assertTrue(in_bounds(world, [0, 0]), msg)
        msg = "For a 5x5 world, tests in_bounds() to ensure that [-1, -1] is NOT in the world."
        self.assertFalse(in_bounds(world, [-1, -1]), msg)
        msg = "For a 5x5 world, tests in_bounds() to ensure that [5, 5] is NOT in the world."
        self.assertFalse(in_bounds(world, [5, 5]), msg)

    def test_find_food_in_a_random_world(self):
        for test_num in range(0, 100):
            world[0:] = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                         [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY]]
            creature_row = randrange(0, WORLD_DIM)
            creature_col = randrange(0, WORLD_DIM)
            set_creature_location([creature_row, creature_col])
            food_location = [-1, -1]
            while not in_bounds(world, food_location):
                food_direction = choice([[1, 0], [-1, 0], [0, 1], [0, -1]])
                food_location = creature_row - food_direction[0], creature_col - food_direction[1]
            set_cell(food_location[0], food_location[1], CELL_FOOD)
            proper_output = list(food_location)
            submission_output = find_nearby_food(world, creature)
            self.assertEqual(proper_output, submission_output,"find_nearby_food() method is tested in many random settings."+"\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output))

unittest.main()