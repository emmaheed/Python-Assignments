class Node(object):
    def __init__(self, name, ip, netmask, gw):
        self.name = name
        self.ip = ip
        self.netmask = netmask
        self.gw = gw
        self.numberoftests = 0

    def __str__(self):
        return "" + self.ip + ", " + self.netmask + ", " + self.gw




class NodeConfigList(object):
    def __init__(self, max):
        self.nodeList = []
        self.maxNr = max
        self.num = 0

    def append(self, newnode):
        if self.num < self.maxNr:
            self.nodeList.append(newnode)
            self.num += 1

    def __iter__(self):
        for x in self.nodeList:
            yield x

    def __getitem__(self, name):
        return [x for x in self.nodeList if x.name == name]



myNodeConfigList = NodeConfigList(2)

myNodeConfigList.append(Node("work", "123.123.123.123", "255.255.255.0", "8.8.8.8"))

myNode = Node("home", "123.123.123.123", "255.255.255.0", "8.8.8.8")

myNodeConfigList.append(myNode)
myNode.ip = "321.321.321.321"
myNodeConfigList.append(myNode)
myNodeConfigList.append(myNode)

for n in myNodeConfigList:
    print(n)
        

print ("yes" if myNodeConfigList[0] in myNodeConfigList else "no")

