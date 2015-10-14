import unittest, pprint
from util import *
from test_assets import *
from hw3.simulator import *


class TestFindAllFood(unittest.TestCase):
    def test_find_all_food_standard(self):
        set_world(
            [CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD,
             CELL_EMPTY])
        proper_output = [1, 6, 8]
        set_cell(1, CELL_FOOD)
        set_cell(6, CELL_FOOD)
        set_cell(8, CELL_FOOD)
        submission_output = find_all_food()
        msg = "\nThis test checks whether the find_all_food() method returns the correct list of locations of all the food " \
              "in a world that contains food.\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
        self.assertEqual(proper_output, submission_output,msg)

    def test_find_all_food_no_food_in_world(self):
        set_world([CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD, CELL_EMPTY])
        proper_output = []
        set_cell(1, CELL_EMPTY)
        set_cell(6, CELL_EMPTY)
        set_cell(8, CELL_EMPTY)
        submission_output = find_all_food()
        msg = "\nThis test checks whether the find_all_food() method properly returns an empty list when the world contains " \
              "no food.\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
        self.assertEqual(proper_output, submission_output,msg)


    def test_find_all_food_food_everywhere_in_world(self):
        set_world([CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD, CELL_EMPTY])
        proper_output = [0,1,2,3,4,5,6,7,8,9]
        set_cell(0, CELL_FOOD)
        set_cell(2, CELL_FOOD)
        set_cell(3, CELL_FOOD)
        set_cell(4, CELL_FOOD)
        set_cell(5, CELL_FOOD)
        set_cell(7, CELL_FOOD)
        set_cell(9, CELL_FOOD)

        submission_output = find_all_food()
        msg = "\nThis test checks whether the find_all_food() method properly returns a list containing every location in the\n" \
              "world when the world contains food everywhere.\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
        self.assertEqual(proper_output, submission_output,msg)


unittest.main()