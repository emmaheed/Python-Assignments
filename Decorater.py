
def deco(f):

    def tempFuncName():
        print("START")
        f()
        print("STOP")
    return tempFuncName

@deco
def myFunction():
    print("hello")

myFunction()
