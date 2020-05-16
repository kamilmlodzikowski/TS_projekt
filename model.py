from statemachine import StateMachine, State, Transition
from generator import Generator
import supervisor as sup


# create paths from transitions (exemplary)
sup_path_1 = ["m_0_1", "m_1_0", "m_0_2", "m_2_0"]
sup_path_2 = ["m_0_2", "m_2_0", "m_0_2", "m_2_0"]
sup_path_3 = ["m_0_1", "m_1_0", "m_0_1", "m_1_0"]
sup_paths = [sup_path_1, sup_path_2, sup_path_3]

# execute paths
for path in sup_paths:

    # create a supervisor
    supervisor = Generator.create_master(sup.master_states, sup.master_transitions)
    print('\n' + str(supervisor))

    # run supervisor for exemplary path
    print("Executing path: {}".format(path))
    for event in path:

        # launch a transition in our supervisor
        sup.master_transitions[event]._run(supervisor)
        print(supervisor.current_state)

        # add slave
        if supervisor.current_state.value == "nadawanie":
            # TODO: automata 1 (for) slave1
            ...
            print("Nadawanie zakonczone!")

        if supervisor.current_state.value == "odbieranie":
            # TODO: automata 2 (for) slave2
            ...
            print("Odbieranie zakonczone!")