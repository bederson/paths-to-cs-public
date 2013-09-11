from graphics import *
import math


# First, initialize the graphics system
init_graphics()

# Then create your graphics
x = 200
y = 200

move_to(x, y)   # This moves the pen to the specified position

# This executes the body of the for loop 100 times, once for each value of i
# starting at 0 and ending at 99
for i in range(0, 100):
    move(10)    # This moves in the current direction by the specified amount
    turn(5)     # This turns the specifed number of *degrees*

# Finally, display the graphics that you created
display_window()