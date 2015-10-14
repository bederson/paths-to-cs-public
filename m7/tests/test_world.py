#Test basic neighbor
#test food growth
import unittest
from hw7.world import World
from hw7.cells import *


class TestWorld(unittest.TestCase):
    def test_empty_world(self):
        World(4, 0)

    def test_world_with_one_food(self):
        World(4, 1)

    def test_get_dim(self):
        expected_output = 4
        world = World(expected_output, 1)
        submited_output = world.get_dim()
        self.assertEqual(submited_output, expected_output)

    def test_get_cell(self):
        world = World(4, 0)
        cell = world.get_cell(0, 0)
        self.assertEqual(type(cell), LandCell)

    def test_set_cell(self):
        world = World(4, 0)
        expected_output = ArableLandCell(world, [0, 0], 0)
        world.set_cell(0, 0, expected_output)
        submited_output = world.get_cell(0, 0)
        self.assertEqual(submited_output, expected_output)

    def test_get_food_level(self):
        world = World(4, 0)
        cell = ArableLandCell(world, [0, 0], 0)
        cell.set_food_level(1)
        expected_output = 1
        world.set_cell(0, 0, cell)
        submited_output = world.get_food_level(0, 0)
        self.assertEqual(submited_output, expected_output)

    def test_grow_all_food_level(self):
        world = World(4, 0)
        cell = ArableLandCell(world, [0, 0], 0)
        cell.set_food_level(0)
        expected_output = FOOD_GROWTH
        world.set_cell(0, 0, cell)
        world.grow_all_food_level()
        submited_output = world.get_food_level(0, 0)
        self.assertEqual(submited_output, expected_output)


unittest.main()