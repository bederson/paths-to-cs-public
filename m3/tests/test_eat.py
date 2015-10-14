import unittest
import StringIO
import sys
from util import *
import pprint
from test_assets import *
from hw3.simulator import *


class TestMoveToLocation(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_eat_when_hungy_and_food_present(self):
        set_world([CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD, CELL_EMPTY])
        proper_output = ' ---  ME(8)  ---   ---   ---   ---  FOOD   ---  FOOD   ---  \n ---   ---  ME(8)  ---   ---   ---  FOOD   ---  FOOD   ---  \n'
        set_creature_hunger_level(9)
        set_creature_location(1)
        eat()
        move_to_location(2)
        submission_output = self.contained_output.getvalue()
        submission_output = submission_output.replace("_", "-")
        if unws(proper_output) != unws(submission_output):
            msg = "\nThis test places a hungry creature at a cell in the world which contains food, " \
                  "and lets it eat the food. \nThen the creature moves right one cell. " \
                  "The cell previously containing food should now be empty and the creature's hunger level should have decreased by one.\n" \
                  "Expected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
            self.assertEqual(proper_output, submission_output, msg)

    def test_eat_when_hungry_and_at_empty_cell_cell_hunger_level_unchanged(self):
        set_world([CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD, CELL_EMPTY])
        set_creature_location(0)
        set_creature_hunger_level(9)
        eat()
        move_to_location(1)
        msg = "\nThis test places the creature at an empty cell, containing no food, " \
              "and attempts to eat. \nThe creature then moves right by one cell. The creature's hunger level should remain unchanged."
        self.assertEqual(get_creature_hunger_level(), 9, msg)

    def test_eat_when_hungry_and_at_empty_cell_cell_still_empty(self):
        set_world([CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD, CELL_EMPTY])
        set_creature_location(0)
        set_creature_hunger_level(9)
        eat()
        move_to_location(1)
        msg = "\nThis test places the creature at an empty cell, containing no food, " \
              "and attempts to eat. \nThe creature then moves right by one cell. The cell at the previous location should remain empty and " \
              "not contain any food."
        self.assertEqual(get_world()[0], CELL_EMPTY, msg)

    def test_eat_when_not_hungry_and_food_present_hunger_level_unchanged(self):
        set_world([CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD, CELL_EMPTY])
        set_creature_hunger_level(0)
        set_creature_location(1)
        eat()
        move_to_location(2)
        msg = "\nThis test places the creature with hunger level equal to 0 (not hungry) at a cell containging food, " \
              "and attempts to eat. The creature then moves right one cell and its hunger level should remain 0."
        self.assertEqual(get_creature_hunger_level(), 0, msg)

    def test_eat_when_not_hungry_and_food_present_cell_type_unchanged(self):
        set_world([CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD, CELL_EMPTY])
        set_creature_hunger_level(0)
        set_creature_location(1)
        eat()
        move_to_location(2)
        msg = "\nThis test places the creature with hunger level equal to 0 (not hungry) at a cell containging food, " \
              "and attempts to eat. The creature then moves right one cell and the cell at the previous locations should" \
              "still contain food."
        self.assertEqual(get_world()[1], CELL_FOOD, msg)

    def test_standard_eat_cell_now_empty(self):
        set_world([CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD, CELL_EMPTY])
        set_creature_hunger_level(9)
        set_creature_location(1)
        eat()
        move_to_location(2)
        msg = "\nA hungry creature is at a cell containing food and it eats the food. It then moves to the right one cell. \nThe cell at the " \
              "previous location should now be empty."
        self.assertEqual(get_world()[1], CELL_EMPTY, msg)


    def test_standard_eat_hunger_level_reduced_by_one(self):
        set_world([CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD, CELL_EMPTY])
        set_creature_hunger_level(9)
        set_creature_location(1)
        eat()
        move_to_location(2)
        msg = "\nA hungry creature is at a cell containing food and it eats the food. It then moves to the right one cell. \nThe hunger level " \
              "of the creauture should now be reduced by 1."
        self.assertEqual(get_creature_hunger_level(), 8, msg)


unittest.main()