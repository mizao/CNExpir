import random
import networkx as nx

class priceGraph:
    
    def __init__(self):
        ;
    
    @staticmethod
    def generateGraph(n, m, p):
        edges = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,1],[1,3],[2,4],[2,5],[2,6],[2,7],[3,5],[3,6],[3,7],[3,8],[4,5],[4,6],[4,7],[5,6],[8.1],[8,2],[9,1],[9,3],[9,4]];
        array = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,1,1,3,2,4,2,5,2,6,2,7,3,5,3,6,3,7,3,8,4,5,4,6,4,7,5,6,8.1,8,2,9,1,9,3,9,4];
        for item1 in range(10, n+1, 1):
            tmpNodes = [];
            for item2 in range(m):
                tmpNodes.append(item1);
                tmpNode = item1;
                if random.uniform(0,1)<p:
                    while tmpNode in tmpNodes:
                        tmpNode = random.choice(array);
                    tmpNodes.append(tmpNode);
                else:
                    while tmpNode in tmpNodes:
                        tmpNode = random.choice(range(1, item1));
                    tmpNodes.append(tmpNode);
                edges.append([tmpNode,item1]);
            for item3 in tmpNodes:
                array.append(item3);
        graph = nx.from_edgelist(edges);
        return graph;