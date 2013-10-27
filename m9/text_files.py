import string


def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            print line.strip("\n")


def extract_data(item):
    subject = ""
    where = ""
    when = ""
    url = ""
    for line in item.split("\n"):
        trimmed_line = line.strip(string.whitespace)
        lower_line = trimmed_line.lower()
        if lower_line.find("subject:") == 0:
            subject = trimmed_line[8:].strip(string.whitespace)
        if lower_line.find("where         :") == 0:
            where = trimmed_line[15:].strip(string.whitespace)
        if lower_line.find("when          :") == 0:
            when = trimmed_line[15:].strip(string.whitespace)
        if lower_line.find("website:") == 0:
            url = trimmed_line[8:].strip(string.whitespace)
    return subject, where, when, url


def process_file(filename):
    started = False
    item = ""
    with open(filename, 'r') as f:
        for line in f:
            if not started and line.find("----------") == 0:
                started = True
            elif started and line.find("----------") == 0:
                subject, where, when, url = extract_data(item)
                if subject:
                    print subject
                    if where:
                        print "Where: " + where
                    if when:
                        print "When:  " + when
                    if url:
                        print "Web:   " + url
                    print ""
                item = ""
            elif started:
                item += line

process_file("data/fyi5.txt")