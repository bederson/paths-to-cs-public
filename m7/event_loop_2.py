from system import *


class SimpleGrid():
    DIM = 5                 # Member variable
    DIRECTION_DELTAS = {    # Dictionary
        'left':  [0, -1],
        'right': [0, 1],
        'up':    [-1, 0],
        'down':  [1, 0]
    }

    def __init__(self):
        self.me = [2, 2]
        self.system = System()
        self.system.add_callback(self.callback)

    def callback(self, event):
        if event in SimpleGrid.DIRECTION_DELTAS:
            delta = SimpleGrid.DIRECTION_DELTAS[event]
            self.move(delta)
            print self

    def move(self, delta):
        new_row = self.me[0] + delta[0]
        new_col = self.me[1] + delta[1]
        if (0 <= new_row <= SimpleGrid.DIM) and (0 <= new_col <= SimpleGrid.DIM):     # Note simpler condition
            self.me = [new_row, new_col]

    def __str__(self):
        result = ""
        for rowNum in range(SimpleGrid.DIM):
            for colNum in range(SimpleGrid.DIM):
                if self.me == [rowNum, colNum]:
                    result += "* "
                else:
                    result += "- "
            result += "\n"
        return result


grid = SimpleGrid()
print grid
grid.system.main_loop()