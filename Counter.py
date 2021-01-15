def outer():
    counter = [1]
    def inner():
        counter[0] += 1
        return counter[0]
    return inner

a = outer()
b = outer()

print( a() )
print( a() )
print( b() )
print( a() )



