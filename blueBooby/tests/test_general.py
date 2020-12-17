from blueBooby import *

import numpy as np

# content of test_plane.py

def test_units():

    d = 100 # FL

    assert ft(d,"FL") == 10000, "Conversion from FL to ft is wrong"
    assert np.abs(nm(d,"FL") - 1.645788)< 1e-3, "Conversion from FL to nm is wrong"

    d = 10000

    assert FL(d,"ft") == 100, "Conversion from FL to ft is wrong"
    assert np.abs(nm(d,"ft") - 1.645788)< 1e-3, "Conversion from FL to nm is wrong"

    d = 1

    assert np.abs(FL(d,"nm") - 60.7612)< 1e-2, "Conversion from nm to FL is wrong"
    assert np.abs(ft(d,"nm") - 6076.12)< 1e-2, "Conversion from nm to ft is wrong"
