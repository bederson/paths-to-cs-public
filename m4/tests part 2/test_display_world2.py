from hw4_part2.simulator import *
import unittest, pprint
import StringIO
import sys
from util import *
from random import randrange
from test_assets import *

class TestDisplayWorld(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_display_random_world(self):
        for test_num in range(0, 100):
            new_world = []
            proper_output = ""
            set_creature_location([0,0])
            set_creature_hunger_level(1)
            for row in range(WORLD_DIM):
                current_row = []
                for index, col in enumerate(range(WORLD_DIM)):
                    cell_type = randrange(0, 2)
                    if cell_type == 0:
                        current_row.append(CELL_EMPTY)
                        if get_creature_location() == [row, col]:
                            cell_str = "ME(" + str(get_creature_hunger_level()) + ")"
                        else:
                            cell_str = " --  "
                    else:
                        current_row.append(CELL_FOOD)
                        if get_creature_location() == [row, col]:
                            cell_str = "ME(" + str(get_creature_hunger_level()) + ")"
                        else:
                            cell_str = "FOOD "
                    proper_output += cell_str + " "
                new_world.append(current_row)
                proper_output += "\n"
            world[0:] = new_world
            proper_output += "\n"
            display_world(new_world, creature)
            submission_output = self.contained_output.getvalue()
            if unws(proper_output) != unws(submission_output):
                msg = "This test makes a world of a randomly chosen size and fills it with random locations of food and the creature, and checks whether display_world() method works correctly.\nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
                self.assertEqual(proper_output, submission_output, msg)
            self.contained_output.truncate(0)


unittest.main()
