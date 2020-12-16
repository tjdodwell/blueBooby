from blueBooby import *


aircraft = []

aircraft.append(Plane(0.0, [0.0, 0.0, 0.0], [1.0, 0.0, 0.0]))

twitcher = Plotting(aircraft, True)

for i in range(40):

    if(i == 8):
        aircraft[0].initiateClimb(200, 40)

    if(i == 26):
        aircraft[0].initiateClimb(-100, -40)

    aircraft[0].step(0.25)

twitcher.plot()
