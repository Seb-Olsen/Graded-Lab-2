import networkx as nx
import random 
from itertools import groupby
import matplotlib.pyplot as plt

X=1000
Y=0.5
G=nx.Graph()


G.add_node(0)
List=[0]

for n in range(X-1):
    G.add_node(n+1)
    for m in List:
        if random.random()<Y:
            G.add_edge(n+1,m)
    List.append(n+1)
    
    