def numberlist(n):
    list = []
    for x in range(n+1):
        list.append(x)
    return list

a = numberlist(4)
print(a)

for x in a:
    print(x)


class newRange(object):

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return (n for n in range(self.n))
        ## return newRange_iterator(self)


##class newRange_iterator(object):
##
##    def __init__(self, dataholder):
##        self.dataholder = dataholder
##        self.i = 0
##
##    def __iter__(self):
##        return self
##
##    def __next__(self):
##        if self.i < self.dataholder.n + 1:
##            number = self.i
##            self.i += 1
##            return number
##
##        else:
##            raise StopIteration()

a = newRange(4)
for x in a:
    print(x)


def generator_function(n):
    for x in range(n+1):
        yield x

a = generator_function(4)
for x in a:
    print(x)

