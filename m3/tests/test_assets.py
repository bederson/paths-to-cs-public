from hw3 import simulator

CREATURE_LOCATION_INDEX = 0     # Index of the item in the "creature" array that
                                # stores the creature's location.
CREATURE_HUNGER_INDEX = 1       # Index of the item in the "creature" array that

CELL_FOOD = "FOOD"
CELL_EMPTY = ""

def get_world():
# #     # This function simply returns a list that represents the world.
# #     # Simply return the world variable here.
    return simulator.world
# #
# #
def set_world(world_list):
# #     # You don't need to implement this function - we've done it for you
    simulator.world = world_list
# #
# #
def get_cell(index):
# #     # This function returns the value of the n-th cell in the current world
# #     # (which is given as the 'index' parameter)
    return simulator.world[index]
# #
# #
def set_cell(index, cell):
# #     # This replaces the value of the n-th cell (given as 'index')
# #     # with a new cell value (given as the 'cell' parameter)
    simulator.world[index] = cell
# #
# #
def get_creature_location():
# #     # This function returns the current location of the creature as an integer,
# #     # which is a zero-based index into the world.
    return simulator.creature[CREATURE_LOCATION_INDEX]
# #
# #
def set_creature_location(loc):
# #     # This function changes the creature's current location to the new location
# #     # (specified as 'loc' parameter).
    #global creature
    simulator.creature[CREATURE_LOCATION_INDEX] = loc
# #
def get_creature_hunger_level():
# #     # This function returns the current hunger level of the creature.
    return simulator.creature[CREATURE_HUNGER_INDEX]
# #
# #
def set_creature_hunger_level(hunger_level):
# #     # This function changes the creature's current hunger level to the new hunger level
# #     # (specified as the 'hunger_level' parameter).
    simulator.creature[CREATURE_HUNGER_INDEX] = hunger_level

