class Kalman():
    def __init__(self):
        """ Initialize filter """
        self.x_current = 0
        self.v_current = 0.3
        self.dt = 1
        self.a_current = 0.003
        self.alpha = 0.5
        self.beta = 0.0001
        self.gamma = 0.00001

        self.x_pred = self.x_current + self.v_current*self.dt + self.a_current*((self.dt**2)*0.5)
        self.v_pred = self.v_current + self.a_current*self.dt
        self.a_pred = self.a_current

        
        
    def estimate_current_position_and_velocity(self, zi):
        """ Estimate current position and velocity from (noisy) position measurement """ 

        # State update equation
        self.x_current = self.x_pred + self.alpha*(zi - self.x_pred)
        self.v_current = self.v_pred + self.beta*((zi-self.x_pred)/self.dt)
        self.a_current = self.a_pred + self.gamma*((zi-self.x_pred)/(0.5*(self.dt**2)))

        # State extrapolation equation
        self.x_pred = self.x_current + self.v_current*self.dt + self.a_current*((self.dt**2)*0.5)
        self.v_pred = self.v_current + self.a_current*self.dt
        self.a_pred = self.a_current

        return self.x_current, self.v_current