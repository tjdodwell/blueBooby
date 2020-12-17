
# Units.py - Simple set of functions which converts between various units used in ATC

def FL(value, unit):
    # Function converts ft and nm to Flight Level (FL)
    if(unit == "ft"):
        return value / 100.
    elif(unit == "nm"):
        return value * 60.7612162547110347
    else:
        assert 1 == 0, "Unit for conversion not recognised"

def ft(value, unit):
    # Function converts FL and nm to feet (ft)
    if(unit == "FL"):
        return value * 100
    elif(unit == "nm"):
        return value * 6076.12162547110347
    else:
        assert 1 == 0, "Unit for conversion not recognised"

def nm(value, unit):
    # Function converts FL and ft to nautical miles (nm)
    if(unit == "FL"):
        return value / 60.7612162547110347
    elif(unit == "ft"):
        return value / 6076.12162547110347
    else:
        assert 1 == 0, "Unit for conversion not recognised"
