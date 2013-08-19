data = "****--*-----***---"
data = "*"

# Take input string that is a sequence of *'s and -'s and print out the total number of *'s and -'s
# along with the maximum length of each sequence

STAR_INDEX = 0
DASH_INDEX = 1


def process_str(data):
    counts = [0, 0]     # Total number of each char
    maxs = [0, 0]       # Maximum run of each char
    lens = [0, 0]       # Current run of each char
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
        lens[letter_index] += 1
        if lens[letter_index] > maxs[letter_index]:
            maxs[letter_index] = lens[letter_index]
        lens[other_index] = 0

    print "str = '" + data + "'"
    print "# stars = " + str(counts[STAR_INDEX]) + ", max stars = " + str(maxs[STAR_INDEX])
    print "# dashes = " + str(counts[DASH_INDEX]) + ", max dashes = " + str(maxs[DASH_INDEX])

process_str(data)