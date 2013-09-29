#### Private storage
first_name = ""
last_name = ""


#### API for accessing name
def set_name(a_name):
    global first_name, last_name
    space_index = a_name.find(" ")
    if space_index == -1:
        first_name = a_name
        last_name = ""
    else:
        first_name = a_name[:space_index]
        last_name = a_name[space_index + 1:]


def get_name():
    return first_name + " " + last_name


def get_first_name():
    return first_name


def get_last_name():
    return last_name


#### Code that uses API
set_name("Ronald McDonald")
print "Whole name: " + get_name()
print "First name: " + get_first_name()
print "Last name: " + get_last_name()