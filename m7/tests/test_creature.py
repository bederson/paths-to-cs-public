import unittest
from hw7.world import World
from hw7.cells import *
from hw7.creature import Creature


class TestCreature(unittest.TestCase):
    def test_get_location(self):
        test_creature = Creature([0, 0], 0, 4)
        self.assertEqual(test_creature.get_location(), [0, 0])

    def test_set_location(self):
        test_creature = Creature([0, 0], 0, 4)
        test_creature.set_location([1, 1])
        self.assertEqual(test_creature.get_location(), [1, 1])

    def test_get_hunger_level_zero(self):
        test_creature = Creature([0, 0], 0, 4)
        self.assertEqual(test_creature.get_hunger_level(), 0)

    def test_get_hunger_level_one(self):
        test_creature = Creature([0, 0], 1, 4)
        self.assertEqual(test_creature.get_hunger_level(), 1)

    def test_legal_move_creatures_current_locaiton(self):
        test_world = World(4, 0)
        test_creature = Creature([0, 0], INIT_HUNGER, 1)
        self.assertTrue(test_creature.legal_move([0, 0], test_world))

    def test_legal_move_creatures_legal_locaiton(self):
        test_world = World(4, 0)
        test_creature = Creature([0, 0], INIT_HUNGER, 1)
        self.assertTrue(test_creature.legal_move([1, 0], test_world))

    def test_legal_move_creatures_out_of_bounds_locaiton(self):
        test_world = World(4, 0)
        test_creature = Creature([0, 0], INIT_HUNGER, 1)
        self.assertFalse(test_creature.legal_move([6, 6], test_world))

    def test_find_best_neighbor_does_not_crash(self):
        near_sighted_creature = Creature([0, 0], INIT_HUNGER, 2)
        test_world = World(6, 0)
        near_sighted_creature.find_best_neighbor(test_world, METRIC_COMBINED)

    def test_find_best_neighbor_food_metric_1(self):
        near_sighted_creature = Creature([0, 0], starting_hunger=1, eye_sight=2)
        test_world = World(6, 0)
        food_cell = ArableLandCell(test_world, [0, 2], 0)
        test_world.set_cell(0, 2, food_cell)
        food_cell.set_food_level(2)
        submited_output = near_sighted_creature.find_best_neighbor(test_world, METRIC_FOOD)
        expected_output = [0, 1]
        self.assertEqual(submited_output, expected_output)

    def test_find_best_neighbor_food_metric_1(self):
        near_sighted_creature = Creature([0, 0], starting_hunger=1, eye_sight=2)
        test_world = World(6, 0)
        food_cell = ArableLandCell(test_world, [2, 0], 0)
        test_world.set_cell(2, 0, food_cell)
        food_cell.set_food_level(2)
        submited_output = near_sighted_creature.find_best_neighbor(test_world, METRIC_FOOD)
        expected_output = [1, 0]
        self.assertEqual(submited_output, expected_output)

    def test_find_best_neighbor_elevation_metric_1(self):
        near_sighted_creature = Creature([0, 0], starting_hunger=1, eye_sight=1)
        test_world = World(6, 0)
        high_cell1 = LandCell(test_world, [0, 0], 2)
        test_world.set_cell(0, 0, high_cell1)
        high_cell2 = LandCell(test_world, [1, 0], 1)
        test_world.set_cell(1, 0, high_cell2)
        high_cell3 = LandCell(test_world, [0, 1], 0)
        test_world.set_cell(0, 1, high_cell3)
        high_cell4 = LandCell(test_world, [1, 1], 2)
        test_world.set_cell(1, 1, high_cell4)
        submited_output = near_sighted_creature.find_best_neighbor(test_world, METRIC_ELEVATION)
        expected_output = [0, 1]
        self.assertEqual(submited_output, expected_output)

    def test_find_best_neighbor_elevation_metric_2(self):
        near_sighted_creature = Creature([0, 0], starting_hunger=1, eye_sight=1)
        test_world = World(6, 0)
        high_cell1 = LandCell(test_world, [0, 0], 2)
        test_world.set_cell(0, 0, high_cell1)
        high_cell2 = LandCell(test_world, [1, 0], 0)
        test_world.set_cell(1, 0, high_cell2)
        high_cell3 = LandCell(test_world, [0, 1], 1)
        test_world.set_cell(0, 1, high_cell3)
        high_cell4 = LandCell(test_world, [1, 1], 2)
        test_world.set_cell(1, 1, high_cell4)
        submited_output = near_sighted_creature.find_best_neighbor(test_world, METRIC_ELEVATION)
        expected_output = [1, 0]
        self.assertEqual(submited_output, expected_output)

    def test_find_best_neighbor_distance_metric(self):
        near_sighted_creature = Creature([0, 0], starting_hunger=1, eye_sight=1)
        test_world = World(6, 0)
        high_cell1 = LandCell(test_world, [0, 0], 2)
        test_world.set_cell(0, 0, high_cell1)
        high_cell2 = LandCell(test_world, [1, 0], 0)
        test_world.set_cell(1, 0, high_cell2)
        high_cell3 = LandCell(test_world, [0, 1], 1)
        test_world.set_cell(0, 1, high_cell3)
        high_cell4 = LandCell(test_world, [1, 1], 2)
        test_world.set_cell(1, 1, high_cell4)
        submited_output = near_sighted_creature.find_best_neighbor(test_world, METRIC_ELEVATION)
        expected_not_output1 = [0, 0]
        expected_not_output2 = [1, 1]
        self.assertNotEqual(submited_output, expected_not_output1)
        self.assertNotEqual(submited_output, expected_not_output2)

    def test_find_best_neighbor_combined_metric(self):
        near_sighted_creature = Creature([0, 0], starting_hunger=1, eye_sight=2)
        test_world = World(6, 0)
        high_cell1 = LandCell(test_world, [0, 0], 2)
        test_world.set_cell(0, 0, high_cell1)
        high_cell2 = LandCell(test_world, [1, 0], 3)
        test_world.set_cell(1, 0, high_cell2)
        high_cell3 = LandCell(test_world, [0, 1], 1)
        test_world.set_cell(0, 1, high_cell3)
        high_cell4 = LandCell(test_world, [1, 1], 2)
        test_world.set_cell(1, 1, high_cell4)
        food_cell = ArableLandCell(test_world, [2, 0], 0)
        test_world.set_cell(2, 0, food_cell)
        food_cell.set_food_level(2)
        submited_output = near_sighted_creature.find_best_neighbor(test_world, METRIC_COMBINED)
        expected_output = [1, 0]
        self.assertEqual(submited_output, expected_output)

    def test_find_best_neighbor_combined_metric_food_beyond_eyesight(self):
        near_sighted_creature = Creature([0, 0], starting_hunger=1, eye_sight=2)
        test_world = World(6, 0)
        high_cell1 = LandCell(test_world, [0, 0], 2)
        test_world.set_cell(0, 0, high_cell1)
        high_cell2 = LandCell(test_world, [1, 0], 3)
        test_world.set_cell(1, 0, high_cell2)
        high_cell3 = LandCell(test_world, [0, 1], 0)
        test_world.set_cell(0, 1, high_cell3)
        high_cell4 = LandCell(test_world, [1, 1], 2)
        test_world.set_cell(1, 1, high_cell4)
        food_cell = ArableLandCell(test_world, [3, 0], 0)
        test_world.set_cell(3, 0, food_cell)
        food_cell.set_food_level(2)
        submited_output = near_sighted_creature.find_best_neighbor(test_world, METRIC_COMBINED)
        expected_output = [0, 1]
        self.assertEqual(submited_output, expected_output)

    def test_move_illegal_move_off_world(self):
        creature = Creature([0, 0], INIT_HUNGER, 1)
        test_world = World(4, 0)
        submited_output = creature.move("Left", test_world)
        expected_output = False
        self.assertEqual(submited_output, expected_output)

    def test_move_legal_move(self):
        creature = Creature([0, 0], INIT_HUNGER, 1)
        test_world = World(4, 0)
        submited_output = creature.move("Right", test_world)
        expected_output = [0, 1]
        self.assertEqual(submited_output, expected_output)

    def test_eat_hungry_on_food(self):
        creature = Creature([0, 0], 1, 1)
        test_world = World(4, 0)
        food_cell = ArableLandCell(test_world, [0, 0], 0)
        for i in range(200):
            food_cell.grow()
        test_world.set_cell(0, 0, food_cell)
        submited_output = creature.eat(test_world)
        expected_output = True
        self.assertEqual(submited_output, expected_output)
        self.assertEqual(creature.get_hunger_level(), 0)

    def test_eat_less_hungry_on_food(self):
        creature = Creature([0, 0], 0.5, 1)
        test_world = World(4, 0)
        food_cell = ArableLandCell(test_world, [0, 0], 0)
        for i in range(200):
            food_cell.grow()
        test_world.set_cell(0, 0, food_cell)
        submited_output = creature.eat(test_world)
        expected_output = True
        self.assertEqual(submited_output, expected_output)
        self.assertEqual(creature.get_hunger_level(), 0)

    def test_eat_not_hungry_on_food(self):
        creature = Creature([0, 0], 0, 1)
        test_world = World(4, 0)
        food_cell = ArableLandCell(test_world, [0, 0], 0)
        for i in range(200):
            food_cell.grow()
        test_world.set_cell(0, 0, food_cell)
        submited_output = creature.eat(test_world)
        expected_output = None
        self.assertEqual(submited_output, expected_output)
        self.assertEqual(creature.get_hunger_level(), 0)
        self.assertTrue(food_cell.get_food_level() > FOOD_DEFAULT)

unittest.main()
