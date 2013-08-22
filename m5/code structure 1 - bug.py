data = "****--*-----***---"

# Take input string that is a sequence of *'s and -'s and print out the total number of *'s and -'s
# along with the maximum length of each sequence

def process_str(data):
    stars = 0
    dashes = 0
    max_stars = 0
    max_dashes = 0
    prev_letter = ''
    current_dash_len = 0
    current_star_len = 0
    for letter in data:
        if letter == '*':
            stars += 1
            if prev_letter == '*':
                current_star_len += 1
                current_dash_len = 0
            elif prev_letter == '-':
                if current_dash_len > max_dashes:
                    max_dashes = current_dash_len
                current_dash_len = 0
                current_star_len = 1
        elif letter == '-':
            dashes += 1
            if prev_letter == '-':
                current_dash_len += 1
                current_star_len = 0
            elif prev_letter == '*':
                if current_star_len > max_stars:
                    max_stars = current_star_len
                current_star_len = 0
                current_dash_len = 1
        prev_letter = letter

    print "str = '" + data + "'"
    print "# stars = " + str(stars) + ", max stars = " + str(max_stars)
    print "# dashes = " + str(dashes) + ", max dashes = " + str(max_dashes)

process_str(data)