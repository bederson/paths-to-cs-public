
from graphics import *


# First, initialize the graphics system
init_graphics(size=400, title="Turtle Graphics")

# Then create your graphics
move_to(200, 200)   # Move the turtle to the specified position

# Draw a triangle
move(100)           # Moves in the current direction by the specified amount
turn(120)           # Turns the specified # of degrees clockwise
move(100)
turn(120)
move(100)

# Mov the turtle somewhere else
pen_up()            # This lifts the pen so moving the turtle doesn't draw
move(50)
pen_down()

# Repeat the triangle code
move(100, fill="cornflowerblue", width=3)  # Moves in the current direction by the specified amount
turn(120)                       # Turns the specified # of degrees clockwise
move(100, fill="cornflowerblue", width=3)
turn(120)
move(100, fill="cornflowerblue", width=3)


# Finally, display the graphics that you created
display_window()