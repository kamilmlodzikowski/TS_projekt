from statemachine import State, Transition
import networkx as nx
import matplotlib.pyplot as plt

def transitions(master_states, form_to):
    master_transitions = {}
    for indices in form_to:
        from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
        for to_idx in to_idx_tuple:  # iterate over destinations from a source state
            op_identifier = "m_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

            # create transition object and add it to the master_transitions dict
            transition = Transition(master_states[from_idx], master_states[to_idx], identifier=op_identifier)
            master_transitions[op_identifier] = transition

            # add transition to source state
            master_states[from_idx].transitions.append(transition)
    return master_transitions