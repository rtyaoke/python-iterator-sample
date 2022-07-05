# from the book of 'python trick'.

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


repeater = Repeater('Hello')

i = 0
for item in repeater:
    if i >= 100:
        break
    print(i, item)
    i += 1
