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

    assert True
