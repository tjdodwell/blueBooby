import numpy as np

class Plane:

    # Base Class which defines a single aircraft's state and response to actions

    def __init__(self, t0, position, velocity, waypoints = []):

        self.data = {
            'time': [],
            'Lat': [],
            'Long': [],
            'Alt': [],
            'vx': [],
            'vy': [],
            'vz': [],
            'command': [],
        }

        self.data['time'].append(t0)
        self.data['Lat'].append(position[0])
        self.data['Long'].append(position[1])
        self.data['Alt'].append(position[2])

        self.data['vx'].append(velocity[0])
        self.data['vy'].append(velocity[1])
        self.data['vz'].append(velocity[2])

        #self.data['command'].append(False) # No initial

        self.waypoints = waypoints

        # phi0 > 0 plane is climbing
        if(np.abs(self.data['vz'][-1]) > 0):
            self.climb = True
        else:
            self.climb = False

        self.checkInputs()

        # Initialise lists to store historic variables

        self.commandCount = 0

    def checkInputs(self):

        if(self.data['vz'][-1] > 0):
            assert self.climb, "Plane is climbing since phi0 > 0, but self.climb = False"
            #assert self.climb_z > 0, "Plane is climbing since phi0 > 0 but self.climb_z < 0"




    def step(self, dt):

        assert dt > 0, "Step size should be positive."

        latNew = self.data['Lat'][-1] + self.data['vx'][-1] * dt # Compute new position lat
        longNew = self.data['Long'][-1] + self.data['vy'][-1] * dt # Compute new position long

        tnew = self.data['time'][-1] + dt



        if(self.climb == True): # Plane is climbing (or descending)

            s = (tnew - self.climb_t0) / self.climb_totalTime

            if (s > 1.0 - 1e-6): # Climb complete in this time step

                self.climb = False # Stop simulation
                z = self.z1
                dzdt = 0.0

            else: # Still climbing

                assert self.climb == True

                # Coefficients for cubic spline
                h00 = 2 * (s ** 3) - 3 * (s ** 2) + 1
                h10 = s**3 - 2 * (s**2) + s
                h01 = -2 * (s ** 3) + 3 * (s**2)
                h11 = s**3 - s**2

                # Compute derivative phi = dz/dx
                h00dt = (1 / self.climb_totalTime) * (6*(s**2) - 6*s)
                h10dt = (1 / self.climb_totalTime) * (3*(s**2) - 4*s + 1)
                h01dt = (1 / self.climb_totalTime) * (-6*(s**2) + 6*s)
                h11dt = (1 / self.climb_totalTime) * (3*(s**2) - 2*s)

                z = h00 * self.z0 + h10 * self.phi0 + h01 * self.z1 + h11 * self.phi1

                dzdt = h00dt * self.z0 + h10dt * self.phi0 + h01dt * self.z1 + h11dt * self.phi1

        else: # Plane is not Climbing

            z = self.data['Alt'][-1] # Same as previous

            dzdt = 0.0

        # Update all variables

        self.data['time'].append(tnew)
        self.data['Lat'].append(latNew)
        self.data['Long'].append(longNew)
        self.data['Alt'].append(z)
        self.data['vx'].append(self.data['vx'][-1]) # Repeated - horizontal speed updated in changeSpeed()
        self.data['vz'].append(dzdt)
        self.data['vy'].append(self.data['vy'][-1]) # Repeated


    def initiateClimb(self, dz, climbRate):

        # Initiate Climb - defined by a change of altitude + a distance over which it is done

            self.climb = True # Set climbing flag to True

            self.z0 = self.data['Alt'][-1] # Start of climb at current altitude
            self.z1 = self.z0 + dz # Set new target altitude

            self.climb_t0 = self.data['time'][-1]

            if(dz < 0):
                self.climbRate = -np.abs(climbRate)
            else:
                self.climbRate = np.abs(climbRate)

            self.climb_totalTime = dz / self.climbRate

            self.phi0 = self.data['vz'][-1]
            self.phi1 = 0.0 # Assumption for now

            self.commandCount += 1

            commanddata = {
                'timestamp': len(self.data['time']) - 1,
                'text': "Climb " + str(dz) + " ft",
            }

            self.data['command'].append(commanddata)

    def changeSpeed(self, dv):

        self.data['vx'][-1] += dv[0]

        self.commandCount += 1

        commanddata = {
            'timestamp': len(self.data['time']) - 1,
            'text': "Change Speed " + str(dv) + " nm",
        }
        self.data['command'].append(commanddata)

    def setWayPoint(self, waypoint):

        self.waypoint = waypoint
