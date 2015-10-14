import unittest
import StringIO
import sys

from hw6.world import World
from hw6.constants import *


class TestWorldStr(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_world_str_basic(self):
        world = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_FOOD], ]
        test_world = World(WORLD_DIM, NUM_FOODS)
        test_world.grid = world

        proper_output = '[[\'\', \'\', \'\', \'\', \'FOOD\'], [\'\', \'\', \'\', \'\', \'FOOD\'], [\'\', \'\', \'\', \'\', \'FOOD\'], [\'\', \'\', \'\', \'\', \'FOOD\'], [\'\', \'\', \'\', \'\', \'FOOD\']]\n'
        print world
        submission_output = self.contained_output.getvalue()
        self.assertEqual(proper_output, submission_output, "Testing str() method of an World instance whose cells on the 5th column contain food.")
        self.contained_output.truncate(0)

    def test_world_str_empty(self):
        world = [[CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY],
                 [CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY, CELL_EMPTY], ]
        test_world = World(WORLD_DIM, NUM_FOODS)
        test_world.grid = world

        proper_output = '[[\'\', \'\', \'\', \'\', \'\'], [\'\', \'\', \'\', \'\', \'\'], [\'\', \'\', \'\', \'\', \'\'], [\'\', \'\', \'\', \'\', \'\'], [\'\', \'\', \'\', \'\', \'\']]\n'
        print world
        submission_output = self.contained_output.getvalue()
        self.assertEqual(proper_output, submission_output, "Testing str() method of an empty World instance.")
        self.contained_output.truncate(0)


unittest.main()