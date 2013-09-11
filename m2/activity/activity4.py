from graphics import *


# First, initialize the graphics system
init_graphics(size=200, title="Drawing")

# Then create your graphics
create_rect(50, 50, 100, 100, fill="orange")
create_line(100, 50, 75, 25)
create_line(75, 25, 50, 50)
create_text(50, 100, "Hello World!", fill="#448")

# Finally, display the graphics that you created
display_window()