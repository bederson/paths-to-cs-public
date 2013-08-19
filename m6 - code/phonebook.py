# Supports multiple people with the same name
class Phonebook():
    def __init__(self):
        self.phonebook = {}

    def add(self, name, number):
        if name in self.phonebook:
            self.phonebook[name].append(number)
        else:
            self.phonebook[name] = [number]

    def getNames(self):
        return self.phonebook.keys()

    def get(self, name):
        return self.phonebook[name]

    def dump(self):
        for k,v in self.phonebook.iteritems():
            print k,v
        print ""

    def __str__(self):
        result = ""
        for name in self.phonebook:
            numbers = self.phonebook[name]
            if len(numbers) == 1:
                result += name + ": " + numbers[0] + "\n"
            else:
                result += name + ":" + "\n"
                for number in numbers:
                    result += "  " + number + "\n"
        result += "\n"
        return result


class RunPhonebook():
    def __init__(self):
        pb = Phonebook()
        pb.add("Ben", "5-2764")
        pb.add("Ben", "5-3394")
        pb.add("Allison", "5-7406")

        pb.dump()

        print pb