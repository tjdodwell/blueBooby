from blueBooby import *

# content of test_plane.py

def test_constructPlane():

    testPlane = Plane(0.0, [0.0, 0.0, 0.0], [1.0, 0.0, 0.0])


def test_climb():

    testPlane = Plane(0.0, [0.0, 0.0, 10.0], [1.0, 0.0, 0.0])

    assert testPlane.climb == False

    testPlane.initiateClimb(1000.0, 1.0)

    assert testPlane.climb == True
    assert testPlane.z1 == 1010.0
    assert testPlane.commandCount == 1

def test_changeSpeed():

    testPlane = Plane(0.0, [0.0, 0.0, 10.0], [1.0, 0.0, 0.0])

    testPlane.changeSpeed([1.0,0.0,0.0])

    assert testPlane.data['vx'][-1] == 2.0
    assert testPlane.commandCount == 1

def test_plotting():

    aircraft = []

    aircraft.append(Plane(0.0, [0.0, 0.0, 0.0], [1.0, 0.0, 0.0]))

    twitcher = Plotting(aircraft, True)


# def test_initiateClimb():
#
#     # testing function initiate climb
#
#     testPlane = Plane(0.0, 0.0, 1.0, 0.0, [0.0, 0.0])
#
#     assert testPlane.climb == False
#
#     testPlane.initiateClimb(1000.0, 10.)
#
#     assert testPlane.climb == True
#     assert testPlane.z1 == 1000.0
#     assert testPlane.climb_x == 10.0
