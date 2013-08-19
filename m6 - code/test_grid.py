import unittest
import random
from event_loop_2 import *

class TestSimpleGrid(unittest.TestCase):
    def setUp(self):
        self.grid = SimpleGrid()

    def testMove(self):
        for i in range(100):
            row_delta = random.randint(-1, 1)
            col_delta = random.randint(-1, 1)
            self.grid.move([row_delta, col_delta])
            me = self.grid.me
            self.assertGreaterEqual(me[0], 0)
            self.assertLess(me[0], self.grid.DIM)
            self.assertGreaterEqual(me[1], 0)
            self.assertLess(me[1], self.grid.DIM)

unittest.main()