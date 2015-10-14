import unittest
import StringIO
import sys
from hw6.creature import Creature


class TestCreatureGettersSetters(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_get_location(self):
        test_creature = Creature([0, 0], 0)
        self.assertEqual(test_creature.get_location(), [0, 0], "A new-born creature's location is [0,0].")

    def test_set_location(self):
        test_creature = Creature([0, 0], 0)
        test_creature.set_location([1, 1])
        self.assertEqual(test_creature.get_location(), [1, 1], "Testing creature.set_location([1,1]).")

    def test_get_hunger_level_zero(self):
        test_creature = Creature([0, 0], 0)
        self.assertEqual(test_creature.get_hunger_level(), 0, "Testing Creature([0,0],0) initialization.")

    def test_get_hunger_level_one(self):
        test_creature = Creature([0, 0], 1)
        self.assertEqual(test_creature.get_hunger_level(), 1, "Testing Creature([0,0],1) initialization.")

unittest.main()
