class NewIterTest():

    def __init__(self, text):
        self.text = text
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.text):
            i = self.i
            result = self.text[i].upper()
            self.i += 1
            return result

        else:
            raise StopIteration()


x = NewIterTest("Hello")
for a in x:
    print("Outer: " + a)

    for b in x:
        print("Inner: " + b)

class newRange(object):

    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return newRange_iterator(self)


class newRange_iterator(object):

    def __init__(self, dataholder):
        self.dataholder = dataholder
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.dataholder.text):
            i = self.i
            result = self.dataholder.text[i].upper()
            self.i += 1
            return result

        else:
            raise StopIteration()


x = newRange("Hello")
for a in x:
    print("Outer: " + a)

    for b in x:
        print("Inner: " + b)
