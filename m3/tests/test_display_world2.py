import unittest
import StringIO
import sys
from random import randrange
from util import *
import pprint
from test_assets import *
from hw3.simulator import *



class TestReleaseDisplay(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_display_alternate_sized_empty_worlds(self):
        set_creature_location(None)
        for size in range(0, 100):
            new_world = [CELL_EMPTY] * size
            proper_output = " ---  " * size
            proper_output += '\n'
            set_world(new_world)
            display_world()
            submission_output = self.contained_output.getvalue()
            submission_output = submission_output.replace("_", "-")
            if unws(proper_output) != unws(submission_output):
                msg = "\nThis test creates very small and very big empty worlds and checks whether the display_world() method prints them correctly.\n" \
                      "Expected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
                self.assertEqual(proper_output, submission_output,msg)
            self.contained_output.truncate(0)

    def test_display_alternate_sized_food_worlds(self):
        set_creature_location(None)
        for size in range(0, 100):
            new_world = [CELL_FOOD] * size
            proper_output = "FOOD  " * size
            proper_output += "\n"
            set_world(new_world)
            display_world()
            submission_output = self.contained_output.getvalue()
            if unws(proper_output) != unws(submission_output):
                msg = "\nThis test creates very small and very big worlds competely full of food and checks whether the display_world() method prints it correctly.\n" \
                      "Expected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
                self.assertEqual(proper_output, submission_output,msg)
            self.contained_output.truncate(0)

    def test_display_alternate_sized_random_worlds(self):
        new_world = []
        set_creature_location(None)
        proper_output = ""
        for size in range(0, 100):
            cell_type = randrange(0, 2)
            proper_output = proper_output.rstrip('\n')
            if cell_type == 0:
                new_world.append(CELL_EMPTY)
                proper_output += " ---  "
            else:
                new_world.append(CELL_FOOD)
                proper_output += "FOOD  "
            proper_output += "\n"
            set_world(new_world)
            display_world()
            submission_output = self.contained_output.getvalue()
            submission_output = submission_output.replace("_", "-")
            if unws(proper_output) != unws(submission_output):
                msg = "\nThis test creates very small and very big worlds containing randomply placed food and checks whether the display_world() method prints it correctly.\n" \
                      "Expected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
                self.assertEqual(proper_output, submission_output, msg)
            self.contained_output.truncate(0)


unittest.main()