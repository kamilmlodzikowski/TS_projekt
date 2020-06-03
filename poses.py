from robopy.base import pose
from robopy.base import transforms
from robopy import rpy2r


def przyklad():
    rot1 = rpy2r([0, 0, 0], unit='deg')
    tran1 = [0.5, 0.5, 0.5]
    return pose.SE3(tran1[0], tran1[1], tran1[2], rot1)