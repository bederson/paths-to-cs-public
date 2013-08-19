from system import *
from random import randint


class Cell(object):
    def __str__(self):
        return "-"

    def move_into(self):
        pass


class Food(Cell):
    def __init__(self, level):
        self.level = level

    def __str__(self):
        return str(self.level)

    def has_food(self):
        return self.level > 0

    def eat(self):
        if self.level > 0:
            self.level -= 1

    def move_into(self):
        if self.has_food():
            self.eat()
            print "Chomp!"


class SimpleGrid():
    DIM = 5                 # Member variable
    NUM_FOOD = 5
    DIRECTION_DELTAS = {    # Dictionary
        'left':  [0, -1],
        'right': [0, 1],
        'up':    [-1, 0],
        'down':  [1, 0]
    }

    def __init__(self):
        self.grid = self.gen_grid()
        self.me = [2, 2]
        self.system = System()
        self.system.add_callback(self.callback)

    def gen_grid(self):
        # First generate black grid
        self.grid = []
        for rowNum in range(SimpleGrid.DIM):
            row = []
            for colNum in range(SimpleGrid.DIM):
                row.append(Cell())
            self.grid.append(row)

        # Then insert some food
        for foodNum in range(SimpleGrid.NUM_FOOD):
            rowNum = randint(0, SimpleGrid.DIM-1)
            colNum = randint(0, SimpleGrid.DIM-1)
            food = Food(randint(1, 5))
            self.grid[rowNum][colNum] = food

        return self.grid

    def callback(self, event):
        if event in SimpleGrid.DIRECTION_DELTAS:
            delta = SimpleGrid.DIRECTION_DELTAS[event]
            self.move(delta)
            print self

    def move(self, delta):
        new_row = self.me[0] + delta[0]
        new_col = self.me[1] + delta[1]
        if (0 <= new_row < SimpleGrid.DIM) and (0 <= new_col < SimpleGrid.DIM):     # Note simpler condition
            self.me = [new_row, new_col]
            cell = self.grid[new_row][new_col]
            cell.move_into()

    def __str__(self):
        result = ""
        for rowNum in range(SimpleGrid.DIM):
            for colNum in range(SimpleGrid.DIM):
                if self.me == [rowNum, colNum]:
                    result += "* "
                else:
                    result += self.grid[rowNum][colNum].__str__() + " "
            result += "\n"
        return result


world = SimpleGrid()
print world
world.system.main_loop()