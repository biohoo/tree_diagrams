import networkx as nx
import random
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import json
from networkx.readwrite import json_graph
from jonathan_utilities.custom_colors import AMGEN_BLUE, AMGEN_DARKBLUE, AMGEN_LIGHTBLUE

#   Initialize directed graph
B = nx.DiGraph()

#   edges: parent, child


parents = ['Jonathan Rice', 'Samantha Hurado']
children = ['Some random dog','Buttermilk "Poops" \nBoop Hurado-Rice', 'Biscuit "Bisque"\nTigerlilly (not racist) \nBoopette Hurado-Rice']
grandchildren = ['We do not have any grandchildren\nBecause all of our children are fixed']

B.add_edge('Michele Fridel','Jonathan Rice')
B.add_edge('John Randolph Rice','Jonathan Rice')
B.add_edge('Ray Hurado','Samantha Hurado')
B.add_edge('Joanne Beiswanger','Samantha Hurado')

for parent in parents:
    for child in children:
        for grandchild in grandchildren:
            B.add_edge(parent, child)
            B.add_edge(child,grandchild)

#   Draw the graph in hierarchical form.
pos = graphviz_layout(B, prog='dot')
nx.draw(B, pos, node_color=AMGEN_BLUE, with_labels=True, node_size=10000, node_shape='8', alpha=0.5)
plt.show()

G = nx.balanced_tree(3, 5)
pos = graphviz_layout(G, prog='twopi', args='')
plt.figure(figsize=(6, 6))
nx.draw(G, pos, node_size=20, alpha=0.5, node_color="blue", with_labels=False)
plt.axis('equal')
plt.show()

d = json_graph.node_link_data(G)
json.dump(d, open('force/force.json','w'))