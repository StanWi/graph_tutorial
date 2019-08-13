#!/usr/bin/python3

import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv

nodes_data = [{}, {}] # Fill this
nodes = []
for node in nodes_data:
    nodes.append(node.get('name'))
print(nodes)
edges = [('', '', 1), ('', '', 5)] # Fill this
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

print("Nodes is", G.nodes())
print("Edges is", G.edges())
#print("Neighbors is", G.neighbors(1))


#nx.draw_networkx(G, node_color=color, alpha=0.6, node_size=1000, node_shape='s')

#plt.axis('off')
#plt.show()

#G = nx.complete_graph(5)
A = nx.nx_agraph.to_agraph(G)
#H = nx.nx_agraph.from_agraph(A)
#prog=neato|dot|twopi|circo|fdp|nop.
#A.layout()
A.node_attr['style']='filled'
for data in nodes_data:
    n=A.get_node(data.get('name'))
    owner = data.get('owner')
    if owner == 'IESV':
        n.attr['shape']='box'
        n.attr['fillcolor']='#0000ff80'
    elif owner == 'IESK':
        n.attr['shape']='box'
        n.attr['fillcolor']='#ffff0080'
    elif owner == 'IE':
        n.attr['shape']='box'
        n.attr['fillcolor']='#ff000080'

A.graph_attr.update(landscape='false')
A.edge_attr.update(len=1.5)

A.layout(prog='neato')
A.draw('file.png')
