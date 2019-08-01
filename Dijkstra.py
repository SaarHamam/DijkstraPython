from collections import deque
import math
#Implementation of a Graph D.S.
class Node:
    def __init__(self,key,value=""):
        self.key=key
        self.value=value
    def getKey(self):
        return self.key
    def getValue(self):
        return self.value
    def setValue(self,value):
        self.value=value
class Edge:
    def __init__(self,source,target,weight=1):
        self.weight=weight
        self.source=source.getKey()
        self.target=target.getKey()
    def getSource(self):
        return self.source
    def getTarget(self):
        return self.target
    def getWeight(self):
        return self.weight
    def setWeight(self,weight):
        self.weight=weight
class Graph:
    def __init__(self,nodes=[],edges=[]):
        self.nodes = dict()
        self.Adj = dict()
        self.weights=dict()
        self.size = 0 #Defined by number of nodes
        self.weight = 0 #Total weight of graph
        for node in nodes:
            self.addNode(node)
        for edge in edges:
            self.addEdge(edge)
    def addNode(self,node):
        if node.getKey() not in self.nodes:
            self.Adj[node.getKey()]=set()
            self.nodes[node.getKey()]=node.getValue()
            self.size+=1
            return 0
        print("Key already inserted.")
        return -1
    def addEdge(self,edge):
        if edge.getSource() in self.nodes and edge.getTarget() in self.nodes:
            self.Adj[edge.getSource()].add((edge.getTarget()))
            if edge.getSource() not in self.weights:
                self.weights[edge.getSource()]=dict()
            self.weights[edge.getSource()][edge.getTarget()]=edge.getWeight()
            self.weight+=edge.getWeight()
    def getSize(self):
        return self.size
    def getWeight(self):
        return self.weight
    def getNodesKeys(self):
        keys=[]
        for node in self.nodes:
            keys.append(node)
        return keys
def extractMin(Q):
    r=min(Q.items(),key=lambda x: x[1])[0]
    del Q[min(Q.items(),key=lambda x: x[1])[0]]
    return r

def Dijkstra(g,s):
    #Initialization
    d=dict()
    pi=dict()
    for node in g.nodes:
        d[node]=math.inf
        pi[node]=None
    d[s]=0
    #Dijkstra Algorithm
    Q=dict()
    for node in g.nodes:
        Q[node]=d[node]
    while len(Q)!=0:
        u=extractMin(Q)
        for v in g.Adj[u]:
            #Relaxation
            if d[v]>d[u]+g.weights[u][v]:
                d[v]=d[u]+g.weights[u][v]
                pi[v]=u
    return d,pi
v=(Node(1),Node(2),Node(3))
e=[Edge(v[0],v[1],5),Edge(v[1],v[2],0),Edge(v[0],v[2],1)]
g=Graph(v,e)
print(Dijkstra(g,v[0].getKey()))




