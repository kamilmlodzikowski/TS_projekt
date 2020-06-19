from robopy.base import pose
from robopy.base import transforms
from robopy import rpy2r
import robopy.base.model as model
from moves import move_j, move_lin
import numpy as np
testRobot = model.Puma560()

'''def robot_positions(testRun=False):

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

    if testRun:
        testPath = move_lin(testRobot, idle, pos1) # move_j nie chce współpracować, move_lin powinien wystarczyć. Dla robota pracującego przy paczkomacie nieprzewidziane ruchy i tak nie są wskazane.
        testRobot.animate(testPath, frame_rate=25, unit='deg')


if __name__ == '__main__':
    #Uruchomienie poses.py jako skrypt główny spowoduje uruchomienie testowej animacji robota
    robot_positions(testRun=True)'''


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


Path1 = move_lin(testRobot, idle, pos1)
Path2 = move_lin(testRobot, pos1, pos2)
Path3 = move_lin(testRobot, pos2, pos3)
Path4 = move_lin(testRobot, pos3, pos4)
Path5 = move_lin(testRobot, pos4, idle)
Path6 = move_lin(testRobot, pos4, pos3)
Path7 = move_lin(testRobot, pos2, pos1)
Path8 = move_lin(testRobot, pos3, idle)
Path9 = move_lin(testRobot, idle, pos3)
Path10 = move_lin(testRobot, pos3, pos1)
Path11 = move_lin(testRobot, pos1, idle)
Path12 = move_lin(testRobot, pos1, pos3)
Path13 = move_lin(testRobot, pos4, pos1)
Path14 = move_lin(testRobot, pos2, idle)



Path_odb = np.concatenate((Path1, Path2, Path3, Path4, Path4, Path5), axis=0)
Path_nad = np.concatenate((Path9, Path4, Path13, Path2, Path14), axis=0)

#Path_odb = np.concatenate((Path1, Path2, Path7, Path12, Path4, Path6, Path8), axis=0)
#Path_nad = np.concatenate((Path9, Path4, Path6, Path10, Path2, Path7, Path11), axis=0)


