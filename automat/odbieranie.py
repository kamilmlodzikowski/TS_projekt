from statemachine import State, Transition
import networkx as nx
import matplotlib.pyplot as plt
from automat.transitions import transitions

G=nx.Graph()

options = [{"name": "IDLE", "initial": True, "value":"idle"}, #0
    {"name": "otwarcie_paczkomatu", "initial": False, "value":"otwarcie"}, #1
    {"name": "Podjazd", "initial": False, "value":"podjazd"}, #2
    {"name": "wyciagniecie_paczki", "initial": False, "value":"wyciagniecie"}, #3
    {"name": "odlozenie_paczki", "initial": False, "value":"odlozenie"}, #4
    {"name": "Blad", "initial": False, "value":"blad"}, #5
    {"name": "zamkniecie_paczkomatu", "initial": False, "value":"zamkniecie"}] #6

master_states = [State(**opt) for opt in options]

form_to = [
    [0, [1]],
    [1,[1,2]],
    [2,[3,5]],
    [3,[4]],
    [4,[6]],
    [5,[6]],
    [6,[0]]
]
G.add_edges_from([(0,1),(1,1),(1,2),(2,3),(2,5),(3,4),(4,6),(5,6),(6,0)])

master_transitions = transitions(master_states, form_to)

path_1 = ["m_0_1", "m_1_2", "m_2_3", "m_3_4", "m_4_6", "m_6_0"]
path_2 = ["m_0_1", "m_1_2", "m_2_5", "m_5_6", "m_6_0"]
path_3 = ["m_0_1", "m_1_1", "m_1_1", "m_1_2", "m_2_3", "m_3_4", "m_4_6", "m_6_0"]
paths = [path_1, path_2, path_3]

plt.title('Odbieranie')
nx.draw(G, with_labels=True)
plt.draw()
plt.show()