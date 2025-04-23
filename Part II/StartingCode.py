import networkx as nx 
import visualizer as viz
import experiments as exp


N=1000
tMax=50
nExp=1000
infected=1
vaccinated=5
gamma=2.5
probabilityOfTransmission=0.5


#generating a random graph with 1000 nodes
rG=nx.binomial_graph(N,1.5/N)


#generating a powerlaw graph with 1000 nodes 
plG=exp.generatePowerLawGraph(N,gamma)



