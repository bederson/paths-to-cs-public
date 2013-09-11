from graphics import *
import math


# First, initialize the graphics system
init_graphics()

# Then create your graphics
x = 250
y = 250

move_to(x, y)
for i in range(0, 100):
    d = i * (2 * 3.14) / 100
    x = i
    y = 100 + 50.0 * math.sin(d)
    line_to(x, y)

# Finally, display the graphics that you created
display_window()