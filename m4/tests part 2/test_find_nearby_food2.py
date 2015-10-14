from hw4_part2.simulator import *
import unittest
from random import randrange
from random import choice
import pprint
from test_assets import *

class TestFindNearbyFoodAndInBounds(unittest.TestCase):
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
            state_before= "\nworld=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            submission_output = find_nearby_food(world, creature)
            self.assertEqual(proper_output, submission_output, state_before+"This test creates random cases where there is a food next to the creature, and tests find_nearby_food() method."+"\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output))

unittest.main()