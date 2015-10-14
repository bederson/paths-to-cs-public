from hw4_part2.simulator import *
import unittest
import StringIO
import sys
import pprint
from util import *
from test_assets import *

class TestDisplayWorld(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
#        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_display_standard_world(self):
        world[0:] = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_FOOD, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],]
        set_creature_location([0, 0])
        set_creature_hunger_level(0)
        proper_output = 'ME(0)  --    --    --   FOOD  \n --    --    --   FOOD   --   \n --    --   FOOD   --    --   \n --   FOOD   --    --    --   \nFOOD   --    --    --    --   \n'
        simulator.display_world(world, creature)
        submission_output = self.contained_output.getvalue()
        if unws(proper_output) != unws(submission_output):
            msg = "This tests that display_world() works as intended for a standard small world. \nExpected: "+pprint.pformat(proper_output)+"\nSubmitted:"+pprint.pformat(submission_output)
            self.assertEqual(proper_output, submission_output, msg)
        self.contained_output.truncate(0)

unittest.main()