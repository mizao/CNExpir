import networkx as nx
import random    

class SIProcess:

    def __init__(self,G, p, source):
        self.p = p;
        self.source = source;
        self.G = G;
        self.nodeState = {};
        self.transPaths = [];
        self.tmpTransPathsDict = {};
        self.tmpStep = 0;
        self.tmpStepInfected = set();
        self.transTree = [];

        for node in list(self.G.nodes()):
            if node != self.source:
                self.nodeState[node] = 0;
            else:
                self.nodeState[node] = 1;

    def nextStep(self):
        mark = 0;
        
        self.tmpStepInfected = set();
        self.tmpTransPathsDict = {};
        for node in list(self.G.nodes()):
            if self.nodeState[node] == 1:
                neighbors = self.G.neighbors(node);
                for neighbor in neighbors:
                    if self.nodeState[neighbor] == 0 and random.uniform(0, 1) < self.p:
                        self.tmpStep = self.tmpStep + 1;
                        if(not neighbor in self.tmpStepInfected):
                            self.tmpStepInfected.add(neighbor);
                            self.tmpTransPathsDict[neighbor] = node;
                        else:
                            if(random.uniform(0, 1) < 0.5):
                                self.tmpTransPathsDict[neighbor] = node;
            else:
                mark = mark + 1;
        
        for node in self.tmpStepInfected:
            self.nodeState[node] = 1;
        for node in self.tmpTransPathsDict.keys():
            self.transPaths.append([self.tmpTransPathsDict[node] ,node]);
            
        if mark > 0:
            return True;
        else:
            return False;
        
    def getTransTree(self):
        self.transTree = nx.from_edgelist(self.transPaths);
        return self.transTree;