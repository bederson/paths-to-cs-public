from hw4_part2 import simulator

WORLD_DIM = 5
NUM_FOODS = 10
INIT_HUNGER = 9


###### Indices into Creature
CREATURE_LOCATION_INDEX = 0     # Index of the item in the "creature" array that
                                # stores the creature's location.
CREATURE_HUNGER_INDEX = 1       # Index of the item in the "creature" array that
                                # stores the creature's hunger.

###### Possible cell values in the world
CELL_FOOD = "FOOD"              # String used in a cell to indicate food
CELL_EMPTY = ""                 # String used in a cell to indicate that nothing is there

# world data structure represents a 2D grid with a list of lists (initially empty)
world = []

# creature is a list containing the creature's location and hunger level.
# The location is a list containing it's row and column indices into the world grid.
creature = [[0, 0], 0]


######### GETTERS AND SETTERS
def get_cell(row, col):
    return world[row][col]


def set_cell(row, col, cell):
    world[row][col] = cell


def get_creature_location():
    return creature[CREATURE_LOCATION_INDEX]


def set_creature_location(loc):
    creature[CREATURE_LOCATION_INDEX] = loc


def get_creature_hunger_level():
    return creature[CREATURE_HUNGER_INDEX]


def set_creature_hunger_level(hunger_level):
    creature[CREATURE_HUNGER_INDEX] = hunger_level
