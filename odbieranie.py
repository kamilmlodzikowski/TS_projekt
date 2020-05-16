from statemachine import StateMachine, State, Transition
import generator

from statemachine import StateMachine, State, Transition
import generator

options = [{"name": "IDLE", "initial": True, "value":"idle"}, #0
    {"name": "otwarcie_paczkomatu", "initial": False, "value":"otwarcie"}, #1
    {"name": "Podjazd", "initial": False, "value":"podjazd"}, #2
    {"name": "wyciagniecie_paczki", "initial": False, "value":"wyciagniecie"}, #3
    {"name": "odlozenie_paczki", "initial": False, "value":"odlozenie"}, #4
    {"name": "Blad", "initial": False, "value":"blad"}, #5
    {"name": "zamkniecie_paczkomatu", "initial": True, "value":"zamkniecie"}] #6

master_states = [State(**opt) for opt in options]

form_to = {
    [0, [1]],
    [1,[1,2]],
    [2,[3,5]],
    [3,[4]],
    [4,[6]],
    [5,[6]],
    [6,[0]]
}

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




