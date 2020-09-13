# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:34:41 2020

@author: Randy
"""

import networkx as nx
import pandas as pd
import itertools
import networkx.generators.small as sm
import networkx.algorithms as al
from networkx.algorithms import traversal as tr

gg = pd.read_csv("rec-amz-Health-Personal-Care.edges", header=None)

gfull = nx.from_pandas_edgelist(gg, source = 0, target = 1, edge_attr = 2)

nx.is_connected(gfull)

nx.number_connected_components(gfull)

Gcc = sorted(nx.connected_components(gfull), key=len, reverse=True)

G0 = gfull.subgraph(Gcc[0])

G0.number_of_nodes()

sub = gg.sample(n = 50000)
gsub = nx.from_pandas_edgelist(sub, source = 0, target = 1, edge_attr = 2)
nx.is_connected(gsub)

nx.number_connected_components(gsub)

gsubcc = sorted(nx.connected_components(gsub), key=len, reverse=True)
G1 = gsub.subgraph(gsubcc[0])
G1.number_of_nodes()

nx.is_connected(G1)

nx.diameter(G1)

nx.average_shortest_path_length(G1)

nx.draw(G1)

