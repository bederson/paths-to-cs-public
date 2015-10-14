import unittest
import StringIO
import sys
from util import *
from test_assets import *
from hw3.simulator import *
import pprint

class TestDisplayWorld(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confused with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_display_standard_world(self):
        set_world([CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD, CELL_EMPTY])
        proper_output = 'ME(9) FOOD   ---   ---   ---   ---  FOOD   ---  FOOD   ---  \n'
        set_creature_location(0)
        display_world()
        submission_output = self.contained_output.getvalue()
        submission_output = submission_output.replace("_", "-")
        msg = "\nTest for standard display_world(). Make sure both outputs are exactly same. \nExpected output: "+proper_output+"\nSubmitted output: "+submission_output
        self.assertEqual(unws(proper_output), unws(submission_output), msg)

    def test_display_creature_out_of_lower_bound(self):
        set_world(
            [CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD,
            CELL_EMPTY])
        proper_output = ' ---  FOOD   ---   ---   ---   ---  FOOD   ---  FOOD   ---  \n'
        set_creature_location(-1)
        display_world()
        submission_output = self.contained_output.getvalue()
        submission_output = submission_output.replace("_", "-")
        if unws(proper_output) != unws(submission_output):
            msg = "\nWhen the creature's location is out of bounds, it should not appear in the displayed world.\n"\
                  "Testing if you place the creature outside of lower bound for its position in the world.\n" \
                  "Expected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
            self.assertEqual(proper_output, submission_output,msg)

    def test_display_creature_out_of_upper_bound(self):
        set_world(
            [CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD,
             CELL_EMPTY])
        proper_output = ' ---  FOOD   ---   ---   ---   ---  FOOD   ---  FOOD   ---  \n'
        set_creature_location(10)
        display_world()
        submission_output = self.contained_output.getvalue()
        submission_output = submission_output.replace("_", "-")
        if unws(proper_output) != unws(submission_output):
            msg = "\nWhen the creature's location is out of bounds, it should not appear in the displayed world.\n" \
                  "Testing if you place the creature outside of the upper bound for its position in the world.\n" \
                  "Expected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
            self.assertEqual(proper_output, submission_output,msg)

    def test_display_world_multiple_times(self):
        set_world(
            [CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD,
             CELL_EMPTY])
        proper_output = 'ME(9) FOOD   ---   ---   ---   ---  FOOD   ---  FOOD   ---  \n'
        initial_output = 'ME(9) FOOD   ---   ---   ---   ---  FOOD   ---  FOOD   ---  \n'
        set_creature_location(0)
        set_creature_hunger_level(9)
        for i in range(1, 11):
            display_world()
            submission_output = self.contained_output.getvalue()
            submission_output = submission_output.replace("_", "-")
            if unws(proper_output) != unws(submission_output):
                msg = "\nThis test calls display_world() multiple times in a row.\n" \
                      "Calling the function should not modify the world.\nTesting to make sure the " \
                      "world is not changed no matter how many times the display_world() function is called.\n" \
                      "Expected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
                self.assertEqual(proper_output, submission_output,msg)
            proper_output += initial_output


unittest.main()