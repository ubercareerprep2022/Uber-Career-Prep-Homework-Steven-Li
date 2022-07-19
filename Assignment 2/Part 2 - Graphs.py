class GraphNode:
    def __init__(self, data):
        self.data = data

class GraphWithAdjacencyList:
    def __init__(self):
        self.adjNodes = {}

    def addNode(self, key):
        new = GraphNode(key)
        self.adjNodes[new] = []

    def removeNode(self, key):
        remove = GraphNode(key)
        del self.adjNodes[remove]

        for node in self.adjNodes.keys():
            if remove in self.adjNodes[node]:
                self.adjNodes[node].remove(remove)

    def addEdge(self, node1, node2):
        self.adjNodes[node1].append(node2)
        self.adjNodes[node2].append(node1)

    def removeEdge(self, node1, node2):
        self.adjNodes[node1].remove(node2)
        self.adjNodes[node2].remove(node1)



