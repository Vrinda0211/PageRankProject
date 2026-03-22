import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def read_graph(file_path):
    graph={}
    with open(file_path,"r") as f:
        for line in f:
            parts=line.strip().split("->")
            node=parts[0].strip()

            if len(parts)>1:
                links=parts[1].strip().split()
            else:
                links=[]
            graph[node]=links
    return graph
graph=read_graph("data\graph.txt")
print(graph)

def adj_mat(graph):
    nodes=list(graph.keys())
    n=len(nodes)
    index={node: i for i,node in enumerate(nodes)}
    A=np.zeros((n,n))
    for node,links in graph.items():
        j=index[node]
        for link in links:
            if link in index:
                i=index[link]
                A[i][j]=1
    return A,nodes
