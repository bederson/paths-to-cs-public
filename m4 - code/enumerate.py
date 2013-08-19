foods = ['peaches', 'apples', 'grapes']


def print_foods1():
    index = 0
    for food in foods:
        print str(index) + ": " + food
        index = index + 1


def print_foods2():
    index = 0
    for food in foods:
        print str(index) + ": " + food
        index += 1


def print_foods3():
    for index, food in enumerate(foods):
        print str(index) + ": " + food



print_foods3()