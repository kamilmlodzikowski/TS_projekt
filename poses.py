from robopy.base import pose
from robopy.base import transforms
from robopy import rpy2r


def robot_positions(testRun=False):

    if testRun:
        import robopy.base.model as model
        from moves import move_j, move_lin
        testRobot = model.Puma560()

    # Poniżej znajduje się lista dostępnych dla robota pozycji.

    rot1 = rpy2r([0, 0, 0], unit='deg')
    tran1 = [0.0, 0.0, 0.0]
    idle = pose.SE3(tran1[0], tran1[1], tran1[2], rot1)  # Pozycja w stanie spoczynku

    rot2 = rpy2r([0, 0, 0], unit='deg')
    tran2 = [-0.5, 1.5, 0.5]
    pos1 = pose.SE3(tran2[0], tran2[1], tran2[2], rot2)

    rot3 = rpy2r([0, 0, 0], unit='deg')
    tran3 = [-0.5, 1.0, 0.5]
    pos3 = pose.SE3(tran3[0], tran3[1], tran3[2], rot3)

    # TODO: Więcej pozycji robota

    if testRun:
        testPath = move_lin(testRobot, pos1, pos3) # move_j nie chce współpracować, move_lin powinien wystarczyć. Dla robota pracującego przy paczkomacie nieprzewidziane ruchy i tak nie są wskazane.

        testRobot.animate(testPath, frame_rate=30, unit='deg')

if __name__ == '__main__':
    # Uruchomienie poses.py jako skrypt główny spowoduje uruchomienie testowej animacji robota
    robot_positions(testRun=True)