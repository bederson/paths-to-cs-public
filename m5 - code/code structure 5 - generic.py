data = "****--*--$$@@@---$**$$$$$---!"

# Take input string that is a sequence of *'s and -'s and print out the total number of *'s and -'s
# along with the maximum length of each sequence

def get_uniq_chars(data):
    chars = []
    for char in data:
        if not char in chars:
            chars.append(char)
    return chars


def process_str(data):
    uniq_chars = get_uniq_chars(data)
    num_uniq_chars = len(uniq_chars)
    counts = [0] * num_uniq_chars     # Total number of each char
    maxs = [0] * num_uniq_chars       # Maximum run of each char
    lens = [0] * num_uniq_chars       # Current run of each char
    for letter in data:
        letter_index = uniq_chars.index(letter)

        counts[letter_index] += 1
        lens[letter_index] += 1
        if lens[letter_index] > maxs[letter_index]:     # Update max count
            maxs[letter_index] = lens[letter_index]
        for index in range(len(uniq_chars)):            # Reset other runs
            if index != letter_index:
                lens[index] = 0

    print "str = '" + data + "'"
    for char in uniq_chars:
        index = uniq_chars.index(char)
        print "# " + char + "'s = " + str(counts[index]) + ", max " + char + "'s = " + str(maxs[index])

process_str(data)