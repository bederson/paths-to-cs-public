world = ["", "ME", "", "", "", "food", "", "", "", ""]


def display_world():
    str = ""
    for cell in world:
        if cell == "ME":
            str += " ME "
        elif cell == "food":
            str += "FOOD"
        else:
            str += " __ "
        str += "   "
    print str


def move_right():
    loc = world.index("ME")
    world[loc] = ""
    world[loc + 1] = "ME"

display_world()
move_right()
display_world()
move_right()
display_world()
move_right()
display_world()