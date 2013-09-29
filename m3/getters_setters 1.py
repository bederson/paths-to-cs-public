name = ""


def print_first_name():
    space_index = name.find(" ")
    if space_index != -1:
        first_name = name[:space_index]
        print first_name


def print_last_name():
    space_index = name.find(" ")
    if space_index != -1:
        last_name = name[space_index + 1:]
        print last_name


name = "Ronald McDonald"
print_first_name()
print_last_name()