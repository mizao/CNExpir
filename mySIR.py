import networkx as nx
import random    

class SIRProcess:

    def __init__(self,G, p, q, r, source):
        self.p = p;
        self.q = q;
        self.r = r;
        self.source = source;
        self.G = G;
        self.nodeState = {};
        self.transPaths = [];
        self.tmpTransPathsDict = {};
        self.tmpStep = 0;
        self.tmpStepInfected = set();
        self.tmpStepRecovered = set();
        self.tmpStepForget = set();
        self.transTree = [];

        for node in list(self.G.nodes()):
            if node not in self.source:
                self.nodeState[node] = 0;
            else:
                self.nodeState[node] = 1;

    def nextStep(self):
        self.tmpStepInfected = set();
        self.tmpStepRecovered = set();
        self.tmpStepForget = set();
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
                if random.uniform(0,1) < self.q:
                    self.tmpStepRecovered.add(node);
            elif self.nodeState[node] == 2:
                if random.uniform(0,1) < self.r:
                    self.tmpStepForget.add(node);
        
        for node in self.tmpStepInfected:
            self.nodeState[node] = 1;
        for node in self.tmpStepRecovered:
            self.nodeState[node] = 2;
        for node in self.tmpStepForget:
            self.nodeState[node] = 0;
        for node in self.tmpTransPathsDict.keys():
            self.transPaths.append([self.tmpTransPathsDict[node] ,node]);
            
        return self.nodeState;
        
    def getTransTree(self):
        self.transTree = nx.from_edgelist(self.transPaths);
        return self.transTree;