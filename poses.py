from robopy.base import pose
from robopy.base import transforms
from robopy import rpy2r


def robot_positions(testRun=False):

    if testRun:
        import robopy.base.model as model
        from moves import move_j, move_lin
        testRobot = model.Puma560()

    # Poniżej znajduje się lista dostępnych dla robota pozycji.

    rot = rpy2r([0, 0, 0], unit='deg')
    tran = [0.0, 0.5, 0.5]
    idle = pose.SE3(tran[0], tran[1], tran[2], rot)  # Pozycja w stanie spoczynku

    rot = rpy2r([0, 0, 0], unit='deg')
    tran = [0.2, 0.0, 0.5]
    pos1 = pose.SE3(tran[0], tran[1], tran[2], rot)  # Chwytak przed paczkomatem

    rot = rpy2r([0, 0, 0], unit='deg')
    tran = [0.2, 0.0, 1.2]
    pos2 = pose.SE3(tran[0], tran[1], tran[2], rot)  # Chwytak w paczkomacie

    rot = rpy2r([0, 0, 0], unit='deg')
    tran = [-0.2, 0.0, 0.5]
    pos3 = pose.SE3(tran[0], tran[1], tran[2], rot)  # Chwytak przed punktem odbioru/nadawania

    rot = rpy2r([0, 0, 0], unit='deg')
    tran = [-0.2, 0.0, 1.2]
    pos4 = pose.SE3(tran[0], tran[1], tran[2], rot)  # Chwytak w punkcie odbioru/nadawania

    # TODO: Więcej pozycji robota

    if testRun:
        testPath = move_lin(testRobot, idle, pos1) # move_j nie chce współpracować, move_lin powinien wystarczyć. Dla robota pracującego przy paczkomacie nieprzewidziane ruchy i tak nie są wskazane.

        testRobot.animate(testPath, frame_rate=25, unit='deg')

if __name__ == '__main__':
    # Uruchomienie poses.py jako skrypt główny spowoduje uruchomienie testowej animacji robota
    robot_positions(testRun=True)