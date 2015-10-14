import unittest
from hw7.cells import LandCell
from hw7.world import World


class TestLandCell(unittest.TestCase):
    def test_instantiation(self):
        LandCell([], [0, 0], 0)

    def test_get_location(self):
        cell = LandCell([], [0, 0], 0)
        submited_output = cell.get_location()
        expected_output = [0, 0]
        self.assertEqual(submited_output, expected_output)
        cell = LandCell([], [100, 0], 0)
        submited_output = cell.get_location()
        expected_output = [100, 0]
        self.assertEqual(submited_output, expected_output)

    def test_get_elevation(self):
        cell = LandCell([], [0, 0], 0)
        submited_output = cell.get_elevation()
        expected_output = 0
        self.assertEqual(submited_output, expected_output)
        cell = LandCell([], [0, 0], 1)
        submited_output = cell.get_elevation()
        expected_output = 1
        self.assertEqual(submited_output, expected_output)

    def test_get_neighbors_inner(self):
        world = World(world_dim=10, num_foods=10)
        cell = LandCell(world, [5, 5], 0)
        neighbors = cell.neighbors()
        submitted_num_neighbors = len(neighbors)
        expected_neighbors = [[4, 5], [5, 4], [5, 6], [6, 5]]
        expected_num_neighbors = len(expected_neighbors)
        self.assertEqual(submitted_num_neighbors, expected_num_neighbors)
        for neighbor in neighbors:
            self.assertIn(neighbor.get_location(), expected_neighbors)

    def test_get_neighbors_edge(self):
        world = World(world_dim=10, num_foods=10)
        cell = LandCell(world, [0, 5], 0)
        neighbors = cell.neighbors()
        submitted_num_neighbors = len(neighbors)
        expected_neighbors = [[0, 4], [0, 6], [1, 5]]
        expected_num_neighbors = len(expected_neighbors)
        self.assertEqual(submitted_num_neighbors, expected_num_neighbors)
        for neighbor in neighbors:
            self.assertIn(neighbor.get_location(), expected_neighbors)

    def test_get_neighbors_corner(self):
        world = World(world_dim=10, num_foods=10)
        cell = LandCell(world, [9, 9], 0)
        neighbors = cell.neighbors()
        submitted_num_neighbors = len(neighbors)
        expected_neighbors = [[8, 9], [9, 8]]
        expected_num_neighbors = len(expected_neighbors)
        self.assertEqual(submitted_num_neighbors, expected_num_neighbors)
        for neighbor in neighbors:
            self.assertIn(neighbor.get_location(), expected_neighbors)
unittest.main()