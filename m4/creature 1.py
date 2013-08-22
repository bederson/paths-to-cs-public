world = ["", "ME", "", "", "", "FOOD", "", "", "", ""]

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

def move_right():
    loc = world.index("ME")
    world[loc] = ""
    world[loc + 1] = "ME"

def is_food_to_right():
    if not "FOOD" in world:
        return False

    me_loc = world.index("ME")
    food_loc = world.index("FOOD")
    if food_loc > me_loc:
        return True
    else:
        return False

def move_to_food():
    display_world()
    while is_food_to_right():
        move_right()
        display_world()

move_to_food()