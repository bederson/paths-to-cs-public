import re

# Count
num_subjects = 0
num_whens = 0
whens = []
with open("data/fyi5.txt", 'r') as f:
    for line in f:
        match = re.match("(Subject:|When)(.*)", line)
        if match:
            groups = match.groups()
            if groups[0] == "Subject:":
                num_subjects += 1
            if groups[0] == "When":
                whens.append(groups[1])
                num_whens += 1
    print "Counts:"
    print "# Subjects: " + str(num_subjects)
    print "# Whens: " + str(num_whens)

# Parse dates
dates = []
for when in whens:
    match = re.match(".*: (.*?), (.*?) (.*?), .*", when)
    if match:
        # print "WHEN='" + when + "'"
        groups = match.groups()
        day = groups[0]
        month = groups[1]
        day_num = groups[2]
        dates.append([day, month, day_num])


# Sort dates
def compare_dates(a, b):
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    a_month = a[1]
    b_month = b[1]
    if a_month == b_month:
        a_day_num = int(a[2])
        b_day_num = int(b[2])
        return a_day_num - b_day_num
    else:
        return month_names.index(a_month) - month_names.index(b_month)

print ""
print "Sorted Dates:"
dates.sort(compare_dates)
for date in dates:
    day = date[0]
    month = date[1]
    day_num = date[2]
    print "DAY='"+day + "' MONTH='" + month + "' DATE='" + day_num + "'"

# Use dictionary to count dates
days = {}
months = {}
for date in dates:
    day = date[0]
    month = date[1]
    if day in days:
        days[day] += 1
    else:
        days[day] = 1
    if month in months:
        months[month] += 1
    else:
        months[month] = 1
print ""
print "Day and Month counts:"
print "Days: " + str(days)
print "Months: " + str(months)