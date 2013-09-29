#### Private storage
name = ""


#### API for accessing name
def set_name(a_name):
    global name
    name = a_name


def get_name():
    return name


def get_first_name():
    space_index = name.find(" ")
    if space_index != -1:
        first_name = name[:space_index]
        return first_name


def get_last_name():
    space_index = name.find(" ")
    if space_index != -1:
        last_name = name[space_index + 1:]
        return last_name


#### Code that uses API
set_name("Ronald McDonald")
print "Whole name: " + get_name()
print "First name: " + get_first_name()
print "Last name: " + get_last_name()