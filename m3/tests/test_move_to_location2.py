import unittest, pprint
import StringIO
import sys
from random import randrange
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

    def test_move_to_random_locations_in_random_world(self):
        for world_size in range(2, 102):
            set_creature_location(0)
            next_creature_location = randrange(0, world_size - 1)
            proper_output = ""
            new_world = []
            current_location = 1
            for location in range(world_size):
                cell_type = randrange(0, 2)
                if location == next_creature_location:
                    new_world.append(CELL_EMPTY)
                else:
                    if cell_type == 0:
                        new_world.append(CELL_EMPTY)
                    else:
                        new_world.append(CELL_FOOD)
            while current_location != next_creature_location + 1:
                for index, cell in enumerate(new_world):
                    if index == current_location:
                        proper_output += "ME("+str(get_creature_hunger_level())+") "
                    elif cell == CELL_EMPTY:
                        proper_output += " ---  "
                    else:
                        proper_output += "FOOD  "
                proper_output += "\n"
                current_location += 1
            set_world(new_world)
            move_to_location(next_creature_location)
            submission_output = self.contained_output.getvalue()
            submission_output = submission_output.replace("_", "-")
            if unws(proper_output) != unws(submission_output):
                msg = "This test generates random worlds, both small and large. It then moves the creature in random directions " \
                      "within those worlds and verifies the creature is moveing properly.\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
                self.assertEqual(proper_output, submission_output, msg)
            self.contained_output.truncate(0)


unittest.main()