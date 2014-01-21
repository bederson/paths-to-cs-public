#Test basic neighbor
#test food growth
import unittest
from hw8.world import World
from hw8.cells import *


class TestWorld(unittest.TestCase):
    def get_water_grid_str(self, world):
        s = ""
        for row in world.grid:
            line = ""
            for cell in row:
                line += str(cell.water_level) + " "
            s += line + "\n"
        return s

    def get_expected_water_str(self, expected):
        s = ""
        for row in expected:
            line = ""
            for water_level in row:
                line += str(water_level) + " "
            s += line + "\n"
        return s

    def is_valid_water(self, world, expected, initial_msg):
        MAX_DIFF = 0.1
        for row_num in range(world.world_dim):
            for col_num in range(world.world_dim):
                expected_val = expected[row_num][col_num]
                actual_val = world.get_cell(row_num, col_num).get_water_level()
                if abs(expected_val - actual_val) > MAX_DIFF:
                    msg = initial_msg
                    msg += "Expected water levels after flow:\n" + self.get_expected_water_str(expected) + "\n"
                    msg += "Actual water levels after flow:\n" + self.get_water_grid_str(world) + "\n"
                    return False, msg
        return True, ""

    def test_flow_water_once_flat(self):
        world = World(world_dim=2, num_foods=0, num_water_sources=0)
        cell = WaterSourceCell(world, (0, 0), 0, 0)
        cell_right = LandCell(world, (1, 0), 0)
        cell_down = LandCell(world, (0, 1), 0)
        cell_mid = LandCell(world, (1, 1), 0)
        world.set_cell(0, 0, cell)
        world.set_cell(1, 0, cell_right)
        world.set_cell(0, 1, cell_down)
        world.set_cell(1, 1, cell_mid)
        world.add_water_to_sources()

        expected_water = [[2.6, 0.2], [0.2, 0.0]]
        initial_msg = "\nInitial water levels:\n" + self.get_water_grid_str(world) + "\n"
        world.flow_water()
        world.apply_water_delta()
        valid, msg = self.is_valid_water(world, expected_water, initial_msg)
        self.assertTrue(valid, msg)

    def test_flow_water_twice_flat(self):
        world = World(world_dim=2, num_foods=0, num_water_sources=0)
        cell = WaterSourceCell(world, (0, 0), 0, 0)
        cell_right = LandCell(world, (1, 0), 0)
        cell_down = LandCell(world, (0, 1), 0)
        cell_mid = LandCell(world, (1, 1), 0)
        world.set_cell(0, 0, cell)
        world.set_cell(1, 0, cell_right)
        world.set_cell(0, 1, cell_down)
        world.set_cell(1, 1, cell_mid)
        world.add_water_to_sources()

        expected_water = [[2.6, 0.2], [0.2, 0.0]]
        initial_msg = "\nInitial water levels:\n" + self.get_water_grid_str(world) + "\n"
        world.flow_water()
        world.apply_water_delta()
        valid, msg = self.is_valid_water(world, expected_water, initial_msg)
        self.assertTrue(valid, msg)

        expected_water = [[2.2, 0.3], [0.35, 0.15]]
        initial_msg = "\nInitial water levels:\n" + self.get_water_grid_str(world) + "\n"
        world.flow_water()
        world.apply_water_delta()
        valid, msg = self.is_valid_water(world, expected_water, initial_msg)
        self.assertTrue(valid, msg)

    def test_flow_water_once_hilly(self):
        world = World(world_dim=2, num_foods=0, num_water_sources=0)
        cell = WaterSourceCell(world, (0, 0), 5, 0)
        cell_right = LandCell(world, (1, 0), 1)
        cell_down = LandCell(world, (0, 1), 1)
        cell_mid = LandCell(world, (1, 1), 0)
        world.set_cell(0, 0, cell)
        world.set_cell(1, 0, cell_right)
        world.set_cell(0, 1, cell_down)
        world.set_cell(1, 1, cell_mid)
        world.add_water_to_sources()

        expected_water = [[2.6, 0.2], [0.2, 0.0]]
        initial_msg = "\nInitial water levels:\n" + self.get_water_grid_str(world) + "\n"
        world.flow_water()
        world.apply_water_delta()
        valid, msg = self.is_valid_water(world, expected_water, initial_msg)
        self.assertTrue(valid, msg)

    def test_flow_water_twice_hilly(self):
        world = World(world_dim=2, num_foods=0, num_water_sources=0)
        cell = WaterSourceCell(world, (0, 0), 5, 0)
        cell_right = LandCell(world, (1, 0), 1)
        cell_down = LandCell(world, (0, 1), 1)
        cell_mid = LandCell(world, (1, 1), 0)
        world.set_cell(0, 0, cell)
        world.set_cell(1, 0, cell_right)
        world.set_cell(0, 1, cell_down)
        world.set_cell(1, 1, cell_mid)
        world.add_water_to_sources()

        expected_water = [[2.6, 0.2], [0.2, 0.0]]
        initial_msg = "\nInitial water levels:\n" + self.get_water_grid_str(world) + "\n"
        world.flow_water()
        world.apply_water_delta()
        valid, msg = self.is_valid_water(world, expected_water, initial_msg)
        self.assertTrue(valid, msg)

        expected_water = [[2.2, 0.2], [0.2, 0.4]]
        initial_msg = "\nInitial water levels:\n" + self.get_water_grid_str(world) + "\n"
        world.flow_water()
        world.apply_water_delta()
        valid, msg = self.is_valid_water(world, expected_water, initial_msg)
        self.assertTrue(valid, msg)

unittest.main()