import numpy as np

class Plane:

    # Base Class which defines a single aircraft's state and response to actions

    def __init__(self, x0, z0, v0, phi0, waypoint, t0 = 0.0, climb_x = 10e6, climb_z = 0.0):

        # Position and Velocity
        self.x0 = x0
        self.z0 = z0
        self.v0 = v0
        self.phi0 = phi0

        self.waypoint = waypoint

        # phi0 > 0 plane is climbing
        if(np.abs(self.phi0) > 0):
            self.climb = True

        else:
            self.climb = False

        # Set climbing distance and final height
        self.climb_x = climb_x
        self.climb_z = climb_z
        self.climb_start = x0

        self.x1 = self.x0 + self.climb_x
        self.z1 = self.z0 + self.climb_z
        self.phi1 = 0.0

        self.checkInputs()

        # Initialise lists to store historic variables
        self.t = []
        self.t.append(t0)
        self.x = []
        self.x.append(self.x0)
        self.z = []
        self.z.append(self.z0)
        self.v = []
        self.v.append(self.v0)
        self.phi = []
        self.phi.append(self.phi0)

        self.commandCount = 0

    def checkInputs(self):

        if(self.phi0 > 0):
            assert self.climb, "Plane is climbing since phi0 > 0, but self.climb = False"
            assert self.climb_z > 0, "Plane is climbing since phi0 > 0 but self.climb_z < 0"




    def step(self, dt):

        assert dt > 0, "Step size should be positive."

        xc = self.x[-1] + self.v[-1] * dt # Compute new position xc

        tnew = self.t[-1] + dt


        if(self.climb == True): # Plane is climbing (or descending)

            s = (np.abs(xc - self.climb_start)) / self.climb_x # fraction through climb

            if (s > 1.0 - 1e-6): # Climb complete in this time step

                self.climb = False
                z = self.z1
                phi = self.phi1 # Should be set to 0.0

            else: # Still climbing

                # Coefficients for cubic spline
                h00 = 2 * (s ** 3) - 3 * (s ** 2) + 1
                h10 = s**3 - 2 * (s**2) + s
                h01 = -2 * (s ** 3) + 3 * (s**2)
                h11 = s**3 - s**2

                # Compute derivative phi = dz/dx

                z = h00 * self.z0 + h10 * self.phi0 + h01 * self.z1 + h11 * self.phi1
                phi = 0.0

        else: # Plane is not Climbing

            assert self.phi[-1] == 0.0, "Plane is not climbing, but abs(phi[-1]) > 0.0"

            self.z.append(self.z[-1]) # Repeat Altitude

        # Update all variables
        self.t.append(tnew)
        self.x.append(xc) # Store current position
        self.z.append(z)
        self.phi.append(phi)
        self.v.append(self.v[-1]) # Repeat will be update by changeSpeed() if required

    def initiateClimb(self, z1, climb_x):

        # Initiate Climb - defined by a change of altitude + a distance over which it is done

            self.climb = True

            self.z0 = self.z[-1] # Start of climb at current altitude
            self.z1 = z1 # Set new target altitude

            self.climb_start = self.x[-1]
            self.climb_x = climb_x

            self.phi0 = self.phi[-1]
            self.phi1 = 0.0 # Assumption for now

            self.commandCount += 1

    def changeSpeed(self, v):

        self.v[-1] = v
        self.commandCount += 1

    def setWayPoint(self, waypoint):

        self.waypoint = waypoint
