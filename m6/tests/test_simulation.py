import unittest
from random import randrange

from hw6.creature import Creature
from hw6.world import World
from hw6.simulation import Simulation
from hw6.constants import *


class TestSimulation(unittest.TestCase):
    def test_creatures_starting_hunger(self):
        test_creature = Creature((0, 0), 0)
        test_world = World(5, 5)
        sim = Simulation(world_dim=5, num_foods=5, creature_location=(0, 0), creature_hunger_level=0)
        sim.world = test_world
        sim.creature = test_creature
        prev_hunger = test_creature.get_hunger_level()
        for i in range(5):
            self.assertTrue(prev_hunger <= test_creature.get_hunger_level())
            prev_hunger = test_creature.get_hunger_level()
        self.assertEqual(test_creature.get_hunger_level(), sim.creature.get_hunger_level())

    def test_simulation_with_new_creature_instance(self):
        '''
        This test is mostly to make sure the simlation can work with interchangeable creatures of different attributes
        '''
        test_creature = Creature((0, 0), 0)
        test_world = World(5, 5)
        sim = Simulation(world_dim=5, num_foods=5, creature_location=(0, 0), creature_hunger_level=0)
        sim.world = test_world
        sim.creature = test_creature
        sim.step()
        for steps in range(100):
            row = randrange(0, 4)
            col = randrange(0, 4)
            hunger = randrange(0, 10)
            test_creature = Creature([row, col], hunger)
            sim.creature = test_creature
            sim.step()

    def test_simulation_with_new_world_instance(self):
        '''
        This test is mostly to make sure the simlation can work with interchangeable worlds of the same size
        '''
        test_creature = Creature()
        test_world = World(5, 0)
        sim = Simulation(5, 0)
        sim.world = test_world
        sim.creature = test_creature
        sim.step()
        for steps in range(100):
            food = randrange(0, 10)
            test_world = World(5, LEVEL_MAX)
            sim.world = test_world
            sim.step()

    def test_simulation_with_new_world_instance(self):
        '''
        This test is mostly to make sure hunger is growing properly in the simulation
        '''
        test_creature = Creature([0, 0], 0)
        test_world = World(5, 0)
        sim = Simulation(world_dim=5, num_foods=0, creature_location=(0, 0), creature_hunger_level=0)
        sim.world = test_world
        sim.creature = test_creature
        hunger = test_creature.get_hunger_level()
        for steps in range(100):
            sim.step()
            self.assertEqual(test_creature.get_hunger_level(), hunger + HUNGER_GROWTH)
            hunger += HUNGER_GROWTH


unittest.main()