
class car(object):
    def __init__(self, text):
        self.colour = "red"
        self.doors = 5
        self.horsepower = 450
        
    def __iter__(self):
        #for x in filter(lambda x: not x.startswith('__'), dir(self)):
        for x in [x for  x in dir(self) if not x.startswith('__')]:
            yield getattr(self, x)



myCar = car("hello")


for a in myCar:
    print(a)




class dependency(object):
    def __init__(self, dependencyInformation):
        self.init = True
        self.name = dependencyInformation["name"]
        self.readsArgument = dependencyInformation["readsArgument"]
        self.readsConstants = dependencyInformation["readsConstants"]
        self.readsSignals = dependencyInformation["readsSignals"]

    def __iter__(self):
        return 
    
