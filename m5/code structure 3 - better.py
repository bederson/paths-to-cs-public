data = "****--*-----***---"
# data = "*"    # Bug in this case

# Take input string that is a sequence of *'s and -'s and print out the total number of *'s and -'s
# along with the maximum length of each sequence

def process_str(data):
    STAR_INDEX = 0
    DASH_INDEX = 1
    counts = [0, 0]
    maxs = [0, 0]
    runs = [0, 0]
    prev_letter = ''
    for letter in data:
        # First calc indexes into data structures of current and previous letter
        if letter == '*':
            letter_index = STAR_INDEX
            other_index = DASH_INDEX
        else:
            letter_index = DASH_INDEX
            other_index = STAR_INDEX

        # Now do the counting
        counts[letter_index] += 1
        runs[letter_index] += 1
        if prev_letter == letter:   # letter same as previous
            runs[other_index] = 0
        else:                       # letter different than previous
            if runs[other_index] > maxs[other_index]:
                maxs[other_index] = runs[other_index]
            runs[other_index] = 0
            runs[letter_index] = 1
        prev_letter = letter

    print "str = '" + data + "'"
    print "# stars = " + str(counts[STAR_INDEX]) + ", max stars = " + str(maxs[STAR_INDEX])
    print "# dashes = " + str(counts[DASH_INDEX]) + ", max dashes = " + str(maxs[DASH_INDEX])

process_str(data)