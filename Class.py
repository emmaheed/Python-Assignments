

class nodeConfig(object):

    def __init__(self, i, n, g):
        self.ip = i
        self.netmask = n
        self.gw = g
        self.nrOfTest = 0

    def __str__(self):
        return "ip: {}, netmask: {}, gw: {}".format(self.ip,self.netmask,self.gw)

    def __call__(self,newIp):
        self.ip = newIp

    @classmethod
    def bulkInsertNewInstancesToNodeList(cls, currNodeList):
   
        f = open("nodeConfigs.txt")
        for x in f:
            mylist = x.split(",")
            currentNodeList.append(cls(x[0], x[1], x[2]))
        return currentNodeList        
        

class nodeConfigList(object):

    def __init__(self, n):
        self.maxNrOfNodes = n
        self.nodeList = []

    def append(self, nodeConfig):

        if len(self.nodeList) < self.maxNrOfNodes:
            self.nodeList.append(nodeConfig)
        else:
            print("List is full")

    def __len__(self):
        return len(self.nodeList)
        
    def __iter__(self):
        return (i for i in self.nodeList)

    def __contains__(self, node):
        return node in self.nodeList

    def __getitem__(self, nr):
        return self.nodeList[nr]
        
#d = nodeConfList(20)
#d = nodeConfig.bulkInsertNewInstancesToNodeList(d)

a = nodeConfig('192.168.1.10', '255,255,255,0', '192.168.1.1')
b = nodeConfig('192.168.1.12', '255,255,255,0', '192.168.1.1')
c = nodeConfig('192.168.1.13', '255,255,255,0', '192.168.1.1')

print(a.ip)
print(b.netmask)
print(c.gw)
print(b)

x = nodeConfigList(20)

x.append(a)
x.append(b)
x.append(c)

print(len(x))

for i in x:
    print(i)

if a in x:
    print("Node \"{}\" is in the list".format(a))

print(x[2])




