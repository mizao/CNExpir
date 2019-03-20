# CNExpir
#### 示例
````
from CNExpir import mySI
from CNExpir import mySIR
from CNExpir import PriceGraph
import networkx as nx
import random

si = mySI.SIProcess(SI = SIProcess(G, p, initial_node)
sequence = [degree]*200
G = nx.configuration_model(sequence)
G = max(nx.connected_component_subgraphs(G), key=len)
G = nx.Graph(G)
G.remove_edges_from(nx.selfloop_edges(G))

ran_init_node = random.randint(0, len(list(G.nodes()))-1)
initial_node = list(G.nodes())[ran_init_node]

p = 0.1

SI = SIProcess(G, p, initial_node);
````
