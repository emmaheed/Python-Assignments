
def hello(a):
    yield 2
    yield 6
    yield 8
    yield 12
    yield 26
    yield 32

g = hello(3)

for x in g:
    print(x)

def hello2(a):
    i = 0
    while i < a:
        yield i
        i += 1

g = hello2(4)
for x in g:
    print(x)
