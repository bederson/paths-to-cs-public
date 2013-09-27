from graphics import *
import math


# First, initialize the graphics system
init_graphics(size=400, title="Sin Wave")

# Then create your graphics
initx = 200
inity = 200

move_to(initx, inity)

for i in range(100):
    d = i * (2 * 3.14) / 100
    x = initx + i
    y = inity + 50.0 * math.sin(d)
    line_to(x, y)

# Finally, display the graphics that you created
display_window()