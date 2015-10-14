import unittest
import StringIO
import sys
from util import *
from test_assets import *
from hw3.simulator import *
import pprint

class TestEatAllFood(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confused with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_standard_eat_all_food(self):
        set_world(
            [CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD,
             CELL_EMPTY])
        set_creature_location(0)
        set_creature_hunger_level(9)
        proper_output = 'ME(9) FOOD   ---   ---   ---   ---  FOOD   ---  FOOD   ---  \n ---  ME(9)  ---   ---   ---   ---  FOOD   ---  FOOD   ---  \n ---  ME(8)  ---   ---   ---   ---  FOOD   ---  FOOD   ---  \n ---   ---  ME(8)  ---   ---   ---  FOOD   ---  FOOD   ---  \n ---   ---   ---  ME(8)  ---   ---  FOOD   ---  FOOD   ---  \n ---   ---   ---   ---  ME(8)  ---  FOOD   ---  FOOD   ---  \n ---   ---   ---   ---   ---  ME(8) FOOD   ---  FOOD   ---  \n ---   ---   ---   ---   ---   ---  ME(8)  ---  FOOD   ---  \n ---   ---   ---   ---   ---   ---  ME(7)  ---  FOOD   ---  \n ---   ---   ---   ---   ---   ---   ---  ME(7) FOOD   ---  \n ---   ---   ---   ---   ---   ---   ---   ---  ME(7)  ---  \n ---   ---   ---   ---   ---   ---   ---   ---  ME(6)  ---  \n'
        eat_all_food()
        submission_output = self.contained_output.getvalue()
        submission_output = submission_output.replace("_", "-")
        if unws(proper_output) != unws(submission_output):
            msg = "\nThe creature starts at the left-most cell in the world and eats all the food in the world using the eat_all_food() method. Your display_world() \n" \
                  "method should be called as required in the specifications, resulting in it being called multiple times.\n" \
                  "Expected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
            self.assertEqual(proper_output, submission_output, msg)

    def test_eat_all_food_no_food_in_world(self):
        set_world(
            [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY,
             CELL_EMPTY])
        set_creature_location(0)
        set_creature_hunger_level(9)
        proper_output = 'ME(9)  ---   ---   ---   ---   ---   ---   ---   ---   ---  \n'
        eat_all_food()
        submission_output = self.contained_output.getvalue()
        submission_output = submission_output.replace("_", "-")
        if unws(proper_output) != unws(submission_output):
            msg = "\nThe creature is placed in a world not containing any food. After calling the eat_all_food() method, the creature should remain " \
                  "in its original position.\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
            self.assertEqual(proper_output, submission_output,msg)

    def test_eat_all_food_with_more_food_than_hunger(self):
        set_world([CELL_FOOD]*12)
        set_creature_location(0)
        set_creature_hunger_level(9)
        proper_output = 'ME(9) FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  \nME(8) FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  \n ---  ME(8) FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  \n ---  ME(7) FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  \n ---   ---  ME(7) FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  \n ---   ---  ME(6) FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  \n ---   ---   ---  ME(6) FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  \n ---   ---   ---  ME(5) FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  \n ---   ---   ---   ---  ME(5) FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  \n ---   ---   ---   ---  ME(4) FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  \n ---   ---   ---   ---   ---  ME(4) FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  \n ---   ---   ---   ---   ---  ME(3) FOOD  FOOD  FOOD  FOOD  FOOD  FOOD  \n ---   ---   ---   ---   ---   ---  ME(3) FOOD  FOOD  FOOD  FOOD  FOOD  \n ---   ---   ---   ---   ---   ---  ME(2) FOOD  FOOD  FOOD  FOOD  FOOD  \n ---   ---   ---   ---   ---   ---   ---  ME(2) FOOD  FOOD  FOOD  FOOD  \n ---   ---   ---   ---   ---   ---   ---  ME(1) FOOD  FOOD  FOOD  FOOD  \n ---   ---   ---   ---   ---   ---   ---   ---  ME(1) FOOD  FOOD  FOOD  \n ---   ---   ---   ---   ---   ---   ---   ---  ME(0) FOOD  FOOD  FOOD'
        eat_all_food()
        submission_output = self.contained_output.getvalue()
        submission_output = submission_output.replace("_", "-")
        if unws(proper_output).find(unws(submission_output)) == -1:
            msg = "\nThe creature is placed in a world that has more food than its hunger level. After calling the eat_all_food() method, \n" \
                  "he creature should stop eating when its hunger level reaches 0.\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
            self.assertIn(proper_output, submission_output, msg)



unittest.main()