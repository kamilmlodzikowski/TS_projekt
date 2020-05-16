from statemachine import StateMachine, State, Transition
import generator

options = [{"name": "IDLE", "initial": True, "value":"idle"}, #0
    {"name": "otwarcie_paczkomatu", "initial": False, "value":"otwarcie"}, #1
    {"name": "Podjazd", "initial": False, "value":"podjazd"}, #2
    {"name": "przejecie_paczki", "initial": False, "value":"przejecie"}, #3
    {"name": "wlozenie_paczki", "initial": False, "value":"wlozenie"}, #4
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

sup_path_1 = ["m_0_1", "m_1_1", "m_1_2", "m_2_3", "m_3_4", "m_4_6", "m_6_0"]
sup_path_2 = ["m_0_1", "m_1_2", "m_2_3", "m_3_4", "m_4_6", "m_6_0"]
sup_path_3 = ["m_0_1", "m_1_1", "m_1_2", "m_2_5", "m_5_6", "m_6_0"]
sup_path_4 = ["m_0_1", "m_1_2", "m_2_5", "m_5_6", "m_6_0"]
sup_paths = [sup_path_1, sup_path_2, sup_path_3, sup_path_4]




