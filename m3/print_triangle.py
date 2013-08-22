def gen_line(size):
    line = ""
    for col in range(size):
        line = line + "*"
    return line


def print_triangle(numrows):
    rownum = 0
    for row in range(numrows):
        line = gen_line(rownum + 1)
        rownum += 1
        print line


print_triangle(3)