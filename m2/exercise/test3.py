from graphics import *


# First, initialize the graphics system
init_graphics()

# Then create your graphics
create_rect(50, 50, 100, 100)
create_line(100, 50, 75, 5)
create_line(75, 5, 50, 50)
create_text(50, 100, "Hello World!", fill="#448")

# Finally, display the graphics that you created
display_window()