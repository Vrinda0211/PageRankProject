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

def prob_mat(A):
    n=A.shape[0]
    M=np.zeros((n,n))
    for j in range(n):
        col_sum=np.sum(A[:,j])
        if col_sum==0:
            M[:,j]=1/n
        else:
            M[:,j]=A[:,j]/col_sum
    return M
A,nodes=adj_mat(graph)
M=prob_mat(A)
print("Stochastic matrix:\n",M)

def damping(M,d=0.85):
    n=M.shape[0]
    E=np.ones((n,n))/n
    G=d*M+(1-d)*E
    return G
G=damping(M)
print("Damped Matrix:\n",G)