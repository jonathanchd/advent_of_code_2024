import sys
import networkx as nx
infile = sys.argv[1]
D = open(infile).read().strip()

lines = D.split('\n')

edges = [tuple(line.split('-')) for line in lines]
G = nx.Graph()
e = []
for a, b in edges:
    e.append((a, b))
    e.append((b, a))

G.add_edges_from(e)

largest_clique = max(nx.find_cliques(G), key=len)
print(','.join(sorted(largest_clique)))