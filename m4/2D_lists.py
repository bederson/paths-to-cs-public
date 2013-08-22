import random

size = 8
cells = []

def gen_row():
    row = []
    for i in range(size):
        row.append("-")
    return row

def init():
    for i in range(size):
        row = gen_row()
        cells.append(row)

def populate():
    for i in range(10):
        rowNum = random.randint(0, size-1)
        colNum = random.randint(0, size-1)
        cells[rowNum][colNum] = '*'

def displayGrid():
    for rowNum in range(size):
        row = ""
        for colNum in range(size):
            row += cells[rowNum][colNum] + " "
        print row

init()
populate()
displayGrid()