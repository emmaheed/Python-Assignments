class oldIterTest():
    def __init__(self, text):
        self.text = text

    def __getitem__(self, index):
        result = self.text[index].upper()
        return result



myIterator = oldIterTest("hi there!")

#for x in myIterator:
#    print(x)




class newIterTest():
    def __init__(self, text):
        self.text = text
        self.i = 0
        self.n = len(text)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i <self.n:
            i = self.i
            self.i += 1
            result = self.text[i].upper()
            return result
        else:
            raise StopIteration()


mynewIterator = newIterTest('hi there!')

for x in mynewIterator:
    print(x)
    for b in mynewIterator:
        print(b)
    
