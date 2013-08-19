# Pick n uniquely random numbers in [1,m]
import random

# 4: debug
def gen_unique_rand4(max, rands):
    have_num = False
    print "gen: " + str(rands)
    while not have_num:
        num = random.randint(1, max)
        print "  trying: " + str(num)
        have_num = not num in rands   # removed "not" generates infinite loop
    print "  => " + str(num)
    return num

# 3: best - introduces use of "in" for lists. Eliminates already_picked()
def gen_unique_rand3(max, rands):
    have_num = False
    while not have_num:
        num = random.randint(1, max)
        have_num = not num in rands
    return num

# 2: good - introduces "not", but already_picked() overly complicated
def gen_unique_rand2(max, rands):
    have_num = False
    while not have_num:
        num = random.randint(1, max)   # Note that num guaranteed to be defined because while loop must execute once
        have_num = not already_picked(num, rands)
    return num

# 1: Adequate - but repeats line of code - introduces "while"
def gen_unique_rand1(max, rands):
    num = random.randint(1, max)
    while already_picked(num, rands):
        num = random.randint(1, max)
    return num

def already_picked(num, rands):
    found = False
    for rand in rands:
        if num == rand:
            found = True
            break  # Introduce later for efficiency

    return found

# 2: correct solution
def unique_rands(num_rands, max):
    rands = []
    for i in range(num_rands):
        num = gen_unique_rand3(max, rands)
        rands.append(num)
    return rands

# 1: First incorrect solution
def non_unique_rands(num_rands, max):
    rands = []
    for i in range(num_rands):
        num = random.randint(1, max)
        rands.append(num)
    return rands

num_rands = 5
max = 5

# print non_unique_rands(num_rands, max)
# print unique_rands(num_rands, max)

###################### TESTING
# Hard code tests for now - introduce Python unittest's later
def is_right_length(rands, num_rands):
    return len(rands) == num_rands

def is_all_unique(rands):
    copy = list(rands)
    copy.sort()
    prev = -1
    dup = False
    for item in copy:
        if item == prev:
            dup = True
            break
    return not dup

def is_right_values(rands, max):
    too_high = False
    for item in rands:
        if item > max:
            too_high = True
            break
    return not too_high

def is_correct(rands, num_rands, max):
    if is_right_length(rands, num_rands) and is_all_unique(rands) and is_right_values(rands, max):
        return True
    else:
        return False


def test_soln(num_rands, max):
    rands = unique_rands(num_rands, max)
    if is_correct(rands, num_rands, max):
        print "Correct: " + str(rands)
    else:
        print "Error: " + str(rands)


for i in range(100):
    test_soln(5, 5)
    test_soln(5, 8)
    test_soln(5, 20)
    test_soln(20, 20)
    test_soln(100, 100)