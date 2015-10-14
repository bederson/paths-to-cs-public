import unittest
from random import randrange
import StringIO
import sys
from util import *
import pprint
from test_assets import *
from hw3.simulator import *


class TestEat(unittest.TestCase):
    def setUp(self):
        ####Intercept Standard Output.
        #### This way students can use print and not be confised with string concatination
        self.contained_output = StringIO.StringIO()   # Save new output storage
        #        actual_standard_output = sys.stdout     # Save actual standard output, for later if necessary
        sys.stdout = self.contained_output            # reassign standard out to this new controled output

    def test_eat_when_hungry_in_random_world(self):
        for world_size in range(2, 102):
            new_world = []
            for location in range(world_size + 1):
                cell_type = randrange(0, 2)
                if cell_type == 0:
                    new_world.append(CELL_EMPTY)
                else:
                    new_world.append(CELL_FOOD)
            set_world(new_world)
            creature_location = randrange(0, world_size)
            set_creature_location(creature_location)
            set_creature_hunger_level(1)
            msg = "\nThis test places a hungry creature at a random cell and attempts to eat. If the cell contains food, " \
                  "the hunger level should be reduced by 1 and the cell at the previous location should be empty and not " \
                  "contain any food."
            if get_cell(creature_location) == CELL_FOOD:
                state_before = "\n[BEFORE] world=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
                eat()
                state_after = "\n[AFTER] world=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
                self.assertEqual(0, get_creature_hunger_level(),state_before+state_after+msg)
                self.assertEqual(get_cell(creature_location), CELL_EMPTY,state_before+state_after+msg)
            else:
                state_before = "\n[BEFORE] world=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
                eat()
                state_after = "\n[AFTER] world=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
                self.assertEqual(1, get_creature_hunger_level(),state_before+state_after+msg)
                self.assertEqual(get_cell(creature_location), CELL_EMPTY,state_before+state_after+msg)

    def test_eat_when_not_hungry_in_random_world_hunger_level_unchanged(self):
        for world_size in range(2, 102):
            new_world = []
            for location in range(world_size + 1):
                cell_type = randrange(0, 2)
                if cell_type == 0:
                    new_world.append(CELL_EMPTY)
                else:
                    new_world.append(CELL_FOOD)
            set_world(new_world)
            creature_location = randrange(0, world_size)
            set_creature_location(creature_location)
            set_creature_hunger_level(0)
            current_cell = get_cell(creature_location)
            state_before = "\n[BEFORE] world=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            eat()
            state_after = "\n[AFTER] world=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            msg = "\nA creature that is not hungry is placed at a random location in the world and attempts to eat. \nAfter " \
                  "attempting to eat the creature's hunger level should reamin unchanged and should still be 0."
            self.assertEqual(0, get_creature_hunger_level(),state_before+state_after+msg)



    def test_eat_when_not_hungry_in_random_world_cell_type_unchanged(self):
        for world_size in range(2, 102):
            new_world = []
            for location in range(world_size + 1):
                cell_type = randrange(0, 2)
                if cell_type == 0:
                    new_world.append(CELL_EMPTY)
                else:
                    new_world.append(CELL_FOOD)
            set_world(new_world)
            creature_location = randrange(0, world_size)
            set_creature_location(creature_location)
            set_creature_hunger_level(0)
            current_cell = get_cell(creature_location)
            state_before = "\n[BEFORE] world=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            eat()
            state_after = "\n[AFTER] world=\n" + pprint.pformat(world) + "\ncreature=" + pprint.pformat(creature) +"\n"
            msg = "\nA creature that is not hungry is placed at a random location in the world and attempts to eat. \nAfter " \
                  "attempting to eat, the cell type should remain unchanged."
            self.assertEqual(get_cell(creature_location), current_cell,state_before+state_after+msg)



unittest.main()