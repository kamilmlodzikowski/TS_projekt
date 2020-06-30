from statemachine import State, Transition
import networkx as nx
import matplotlib.pyplot as plt
from automat.transitions import transitions

# define states for a master (way of passing args to class)
options = [
    {"name": "IDLE", "initial": True, "value": "idle"},  # 0
    {"name": "ODBIERANIE", "initial": False, "value": "odbieranie"},  # 1
    {"name": "NADAWANIE", "initial": False, "value": "nadawanie"}]  # 2

# create State objects for a master
# ** -> unpack dict to args
master_states = [State(**opt) for opt in options]

#create graph
G = nx.Graph()

# valid transitions for a master (indices of states from-to)
form_to = [
    [0, [1, 2]],
    [1, [0]],
    [2, [0]]
]
G.add_edges_from([(0, 1), (0, 2), (1, 0), (2, 0)])
plt.title('Supervisor')
nx.draw(G, with_labels=True)
plt.draw()
plt.show()

# create transitions for a master (as a dict)
master_transitions = transitions(master_states, form_to)