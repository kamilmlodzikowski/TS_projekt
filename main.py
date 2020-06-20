from automat.generator import Generator
from automat import nadawanie as nad, odbieranie as odb, supervisor as sup
from animation import poses

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
        #NADAWANIE
        if supervisor.current_state.value == "nadawanie":
            ind = 0
            for nad_path in nad.sup_paths:

                # create a supervisor
                nadaw = Generator.create_master(nad.master_states, nad.master_transitions)
                print('\n' + str(nadaw))

                # run supervisor for exemplary path
                print("Executing path: {}".format(path))
                for nad_event in nad_path:
                    # launch a transition in our supervisor
                    nad.master_transitions[nad_event]._run(nadaw)
                    print(nadaw.current_state)

            poses.odb_animate()
            # poses.testRobot.animate(poses.Path_odb, frame_rate=10, unit='deg')


            print("Nadawanie zakonczone!")

        if supervisor.current_state.value == "odbieranie":
            for odb_path in odb.paths:

                # create a supervisor
                odbie = Generator.create_master(odb.master_states, odb.master_transitions)
                print('\n' + str(odbie))

                # run supervisor for exemplary path
                print("Executing path: {}".format(path))
                for odb_event in odb_path:
                    # launch a transition in our supervisor
                    odb.master_transitions[odb_event]._run(odbie)
                    print(odbie.current_state)
                    
            poses.nad_animate()
            # poses.testRobot.animate(poses.Path_nad, frame_rate=10, unit='deg')

            print("Odbieranie zakonczone!")

