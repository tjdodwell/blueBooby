from blueBooby import *


aircraft = []

aircraft.append(Plane(0.0, [0.0, 0.0, 0.0], [1.0, 0.0, 0.0]))

aircraft.append(Plane(0.0, [15.0, 0.0, 200.0], [-2.0, 0.0, 0.0]))

twitcher = Plotting(aircraft, True)

for i in range(60):

    if(i == 8):
        aircraft[0].initiateClimb(200, 40)

    if(i == 26):
        aircraft[0].initiateClimb(-100, -40)

    for j in range(len(aircraft)):
        aircraft[j].step(0.25)


twitcher.plot()
