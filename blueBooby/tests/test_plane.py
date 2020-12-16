from blueBooby import *

# content of test_plane.py

def test_constructPlane():

    testPlane = Plane(0.0, 0.0, 1.0, 0.0, [0.0, 0.0])

    testPlane =  Plane(0.0, 0.0, 1.0, 1.0, [0.0, 0.0], 0.0, 100.0, 1.0)

    # Check first point has been added
    assert len(testPlane.t) == 1
    assert len(testPlane.x) == 1
    assert len(testPlane.phi) == 1
    assert len(testPlane.z) == 1

    assert testPlane.commandCount == 0


def test_initiateClimb():

    # testing function initiate climb

    testPlane = Plane(0.0, 0.0, 1.0, 0.0, [0.0, 0.0])

    assert testPlane.climb == False

    testPlane.initiateClimb(1000.0, 10.)

    assert testPlane.climb == True
    assert testPlane.z1 == 1000.0
    assert testPlane.climb_x == 10.0
