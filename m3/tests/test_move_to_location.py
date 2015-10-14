import unittest, pprint
import StringIO
import sys
from util import *
from test_assets import *
from hw3.simulator import *


class TestMoveToLocation(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_move_from_zero_to_one(self):
        set_world(
            [CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD,
             CELL_EMPTY])
        proper_output = ' ---  ME(9)  ---   ---   ---   ---  FOOD   ---  FOOD   ---  \n'
        set_creature_location(0)
        set_creature_hunger_level(9)
        move_to_location(1)
        submission_output = self.contained_output.getvalue()
        submission_output = submission_output.replace("_", "-")
        if unws(proper_output) != unws(submission_output):
            msg = "\nThis test moves the creature from the first cell in the world to the second cell. After it has moved to the second cell, display_world() " \
                  "must create the proper output.\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
            self.assertEqual(proper_output, submission_output, msg)

    def test_move_right_two_cells_then_left_two_cells(self):
        set_world(
            [CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD,
             CELL_EMPTY])
        proper_output = ' ---  ME(9)  ---   ---   ---   ---  FOOD   ---  FOOD   ---  \n ---  FOOD  ME(9)  ---   ---   ---  FOOD   ---  FOOD   ---  \n ---  ME(9)  ---   ---   ---   ---  FOOD   ---  FOOD   ---  \nME(9) FOOD   ---   ---   ---   ---  FOOD   ---  FOOD   ---  \n'
        set_creature_location(0)
        set_creature_hunger_level(9)
        move_to_location(2)
        move_to_location(0)
        submission_output = self.contained_output.getvalue()
        submission_output = submission_output.replace("_", "-")
        if unws(proper_output) != unws(submission_output):
            msg = "\nThis test moves the creature to the right 2 cells from its original location and then back 2 cells to the left, returning it " \
                  "to its original location.\nThe test verifies the creature does not eat any food while moving.\n" \
                  "Expected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
            self.assertEqual(proper_output, submission_output, msg)

    def test_move_from_end_to_end(self):
        set_world(
            [CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD,
             CELL_EMPTY])
        proper_output = ' ---  ME(9)  ---   ---   ---   ---  FOOD   ---  FOOD   ---  \n ---  FOOD  ME(9)  ---   ---   ---  FOOD   ---  FOOD   ---  \n ---  FOOD   ---  ME(9)  ---   ---  FOOD   ---  FOOD   ---  \n ---  FOOD   ---   ---  ME(9)  ---  FOOD   ---  FOOD   ---  \n ---  FOOD   ---   ---   ---  ME(9) FOOD   ---  FOOD   ---  \n ---  FOOD   ---   ---   ---   ---  ME(9)  ---  FOOD   ---  \n ---  FOOD   ---   ---   ---   ---  FOOD  ME(9) FOOD   ---  \n ---  FOOD   ---   ---   ---   ---  FOOD   ---  ME(9)  ---  \n ---  FOOD   ---   ---   ---   ---  FOOD   ---  FOOD  ME(9) \n'
        set_creature_location(0)
        set_creature_hunger_level(9)
        move_to_location(9)
        submission_output = self.contained_output.getvalue()
        submission_output = submission_output.replace("_", "-")
        if unws(proper_output) != unws(submission_output):
            msg = "\nThis test moves the creature from left-most cell to the right-most cell in the world. The test verifies\n" \
                  "that the creature does not eat any food while moving.\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
            self.assertEqual(proper_output, submission_output,msg)

    def test_move_nowhere(self):
        set_world(
            [CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_FOOD,
             CELL_EMPTY])
        proper_output = ''
        set_creature_location(0)
        move_to_location(0)
        submission_output = self.contained_output.getvalue()
        submission_output = submission_output.replace("_", "-")
        if unws(proper_output) != unws(submission_output):
            msg = "\nThis test calls the move_to_location() method, using the creature's current location as the parameter. This \n" \
                  "causes the creature not to move at all and should result in no output to the console.\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
            self.assertEqual(proper_output, submission_output, msg)

unittest.main()