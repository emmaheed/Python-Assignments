def myGeneratorFunction(a):
    yield a + 1
    yield a + 2
    yield (a + 3) ** 2
    yield a + 5
    yield a + 7
    yield a + 11
    yield a + 13
    yield a + 17

def myGeneratorFunction2(a):
    for x in a:
        yield x

def myGeneratorFunction3(a):
    for x in range(0,a):
        if x%2 == 0:
            yield x

#gen = myGeneratorFunction2([1,2,3,5,7,11,13,17])
gen = myGeneratorFunction3(20)

for x in gen:
    for y in gen:
        print(y)
    print(x)
