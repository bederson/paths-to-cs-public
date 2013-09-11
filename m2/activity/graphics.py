from Tkinter import *
import math

# A simple graphics library using "Tk"

WINDOW_DIM = 500

root = None
canvas = None
xpos = 0
ypos = 0
angle = 0
pen = True


def init_graphics(size=WINDOW_DIM, title=""):
    """
    Call this to initialize the graphics system.
    This must be called before creating any graphics
    """
    global root, canvas

    root = Tk()
    root.wm_title(title)
    canvas = Canvas(root, width=size, height=size)
    canvas.pack()


def display_window():
    """
    Call this to display the graphics window
    with whatever graphics you have created.
    Once this is called, you can not execute any more of your own code.
    """
    root.mainloop()


def create_line(x1, y1, x2, y2, fill='black', width=1.0):
    """
    Create a line from the point (x1, y1) to (x2, y2)
    with the specified color and line width.
    The origin is at the top-left of the window.
    """
    canvas.create_line(x1, y1, x2, y2, fill=fill, width=width)


def create_rect(x1, y1, x2, y2, fill='grey', outline='black'):
    """
    Create a rectangle from the point (x1, y1) to (x2, y2)
    with the specified fill and outline colors.
    The origin is at the top-left of the window.
    """
    canvas.create_rectangle(x1, y1, x2, y2, outline=outline, fill=fill)


def create_text(x, y, text="", fill='black'):
    """
    Create some text with the top-left corner of the text at the specified position.
    The text will be drawn with the specified fill color.
    The origin is at the top-left of the window.
    """
    canvas.create_text(x, y, text=text, fill=fill, anchor="nw")


def move_to(x, y):
    """
    Move the "pen" to the specified position, but don't draw anything.
    The origin is at the top-left of the window.
    """
    global xpos, ypos

    xpos = x
    ypos = y


def line_to(x, y, fill='black', width=1.0):
    """
    Draw a line from the current pen position to the specified position (x, y).
    The line will be drawn with the specified color and line width.
    After the line is drawn, the pen will be moved to the position (x, y).
    The origin is at the top-left of the window.
    """
    global xpos, ypos

    create_line(xpos, ypos, x, y, fill=fill, width=width)
    xpos = x
    ypos = y


def pen_down():
    """
    Tells the turtle to put the pen down so that future move() commands will draw
    """
    global pen

    pen = True


def pen_up():
    """
    Tells the turtle to lift the pen up so that future move() commands will NOT draw.
    """
    global pen

    pen = False


def move(distance, fill='black', width=1.0):
    """
    Moves the turtle the specified distance forward.
    If the pen is down, it will draw while it moves with the specified fill color and pen width.
    """
    global pen, xpos, ypos

    rad = angle * 2 * 3.14 / 180
    x = xpos + distance * math.cos(rad)
    y = ypos + distance * math.sin(rad)

    if pen:
        line_to(x, y, fill=fill, width=width)

    xpos = x
    ypos = y


def turn(theta):
    """
    Turns the turtle the specified number of degrees clockwise.
    """
    global angle

    angle -= theta