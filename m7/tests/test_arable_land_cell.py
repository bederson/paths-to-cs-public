import unittest
from hw7.cells import *


class TestArableLandCell(unittest.TestCase):
    def test_instantiation(self):
        ArableLandCell([], [0, 0], 0)

    def test_inheritance(self):
        self.assertTrue(issubclass(ArableLandCell, LandCell))

    def test_reset_food_level_and_get_food_level(self):
        cell = ArableLandCell([], [0, 0], 0)
        cell.reset_food_level()
        submited_output = cell.get_food_level()
        self.assertTrue(submited_output == FOOD_DEFAULT)

    def test_set_food_level(self):
        cell = ArableLandCell([], [0, 0], 0)
        cell.set_food_level(1)
        submited_output = cell.get_food_level()
        expected_output = 1
        self.assertEqual(submited_output, expected_output)

    def test_grow(self):
        cell = ArableLandCell([], [0, 0], 0)
        cell.set_food_level(1)
        cell.grow()
        submited_output = cell.get_food_level()
        expected_output = 1 + FOOD_GROWTH
        self.assertEqual(submited_output, expected_output)

    def test_grow_limited(self):
        cell = ArableLandCell([], [0, 0], 0)
        cell.set_food_level(LEVEL_MAX)
        cell.grow()
        submited_output = cell.get_food_level()
        expected_output = LEVEL_MAX
        self.assertEqual(submited_output, expected_output)

unittest.main()