from statemachine import StateMachine, State, Transition
import generator

options_odbieranie = [
    {"name": "IDLE", "initial": True, "value": "idle"},  # 0
    {"name": "Otworzenie paczkomatu", "initial": False, "value": "otwarcie"},  # 1
    {"name": "Podjazd do paczkomatu", "initial": False, "value": "podjazd"},  # 2
    {"name": "Wyciągnięcie paczki", "initial": False, "value": "wyciagniecie"},  # 3
    {"name": "Odłożenie paczki", "initial": False, "value": "odlozenie"}, # 4
    {"name": "Błąd", "initial": False, "value": "blad"},  # 5
    {"name": "Zamknięcie paczkomatu", "initial": False, "value": "zamkniecie"}]  # 6

master_states_odbieranie = [State(**opt) for opt in options_odbieranie]

form_to_odbieranie = [
    [0, [1]],
    [1, [1, 2]],
    [2, [3, 5]],
    [3, [4]],
    [4, [6]],
    [6, [0]]
]

master_transitions_odbieranie = {}
for indices in form_to_odbieranie:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "m_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(master_states_odbieranie[from_idx], master_states_odbieranie[to_idx], identifier=op_identifier)
        master_transitions_odbieranie[op_identifier] = transition

        # add transition to source state
        master_states_odbieranie[from_idx].transitions.append(transition)