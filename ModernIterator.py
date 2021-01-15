class OldIterTest():

    def __init__(self, text):
        self.text = text

    def __getitem__(self, index):
        result = self.text[index].upper()
        return result

a = OldIterTest("Hello World")
for x in a:
    print(x)


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


b = NewIterTest("\nHello World")
for x in b:
    print(x)       
        

class BackWards_NewIterTest():

    def __init__(self, text):
        self.text = text[::-1]
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


c = BackWards_NewIterTest("Hello World\n")
for x in c:
    print(x) 

class BackWards2_NewIterTest():

    def __init__(self, text):
        self.text = text
        self.i = len(self.text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 0:
            i = self.i - 1
            result = self.text[i].upper()
            self.i -= 1
            return result

        else:
            raise StopIteration()


d = BackWards2_NewIterTest("Hello World\n")
for x in d:
    print(x)



