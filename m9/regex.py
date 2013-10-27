import re

data = "my age is #37#"
matches = re.findall("#.*#", data)
if len(matches) > 0:
    match = matches[0]
    print match[1:-1]

data = "my age is 37"
matches = re.findall("[0-9]+", data)
if len(matches) > 0:
    match = matches[0]
    print match

matches = re.findall("\d+", data)
if len(matches) > 0:
    match = matches[0]
    print match

data = "He said 'I love you'."
matches = re.findall("'.*'", data)
if len(matches) > 0:
    match = matches[0]
    print match

data = "Cats are smarter than dogs"
groups = re.match("(.*) are (.*) than .*", data).groups()
print groups

print "---- FYI ----"
with open("data/fyi1.txt", 'r') as f:
    for line in f:
        match = re.match("Subject: (.*)", line)
        if match:
            groups = match.groups()
            for group in groups:
                print group
