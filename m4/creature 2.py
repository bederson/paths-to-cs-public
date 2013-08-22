world = ["", "FOOD", "", "", "", "", "", "ME", "", ""]

def display_world():
    str = ""
    for cell in world:
        if cell == "ME":
            str += " ME "
        elif cell == "FOOD":
            str += "FOOD"
        else:
            str += " __ "
        str += "   "
    print str


def move(delta):
    loc = world.index("ME")
    world[loc] = ""
    world[loc + delta] = "ME"


def delta_to_food():
    if not "FOOD" in world:
        return False

    me_loc = world.index("ME")
    food_loc = world.index("FOOD")

    if food_loc > me_loc:
        return 1
    else:
        return -1


def move_to_food():
    display_world()
    delta = delta_to_food()
    while delta:
        move(delta)
        display_world()
        delta = delta_to_food()

move_to_food()