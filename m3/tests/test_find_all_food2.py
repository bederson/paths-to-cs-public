import unittest, pprint
from random import randrange
from util import *
from test_assets import *
from hw3.simulator import *


class TestFindAllFood(unittest.TestCase):
    def test_find_all_food_in_a_random_world(self):
        new_world = []
        proper_result = []
        for size in range(0, 100):
            cell_type = randrange(0, 2)
            if cell_type == 0:
                new_world.append(CELL_EMPTY)
            else:
                new_world.append(CELL_FOOD)
                proper_result.append(size)
            set_world(new_world)
            submission_result = find_all_food()
            msg = "\nThis test checks whether the find_all_food() method returns the correct list of locations of food " \
                  "for small \nand large worlds with food placed at random locations.\nExpected: "+pprint.pformat(proper_result)+"\nSubmitted:"+pprint.pformat(submission_result)
            self.assertEqual(proper_result, submission_result, msg)


unittest.main()