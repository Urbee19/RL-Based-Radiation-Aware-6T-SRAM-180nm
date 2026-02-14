import numpy as np

class SRAMEnvironment:
    def __init__(self):
        self.reset()

    def reset(self):
        # Initial baseline parameters (180nm realistic)
        self.Wp = 0.6
        self.Wn = 0.3
        self.Vbody = 0.0
        
        self.state = self._calculate_metrics()
        return np.array(self.state, dtype=np.float32)

    def step(self, action):
        # Actions
        if action == 0:
            self.Wp += 0.05
        elif action == 1:
            self.Wn += 0.05
        elif action == 2:
            self.Vbody += 0.02
        elif action == 3:
            self.Vbody -= 0.02

        self.state = self._calculate_metrics()
        done = False
        return np.array(self.state, dtype=np.float32), done

    def _calculate_metrics(self):
        # Physics-inspired trends (replace later with Cadence data)

        Qcrit = 20 + 10*np.log(self.Wp/self.Wn + 1) + 15*self.Vbody
        SNM = 150 + 40*(self.Wp/self.Wn) + 30*self.Vbody
        Delay = 500 - 100*(self.Wn) + 20*self.Wp
        Power = 1 + 0.5*self.Wp + 0.3*self.Wn

        return [Qcrit, SNM, Delay, Power, self.Vbody, self.Wp/self.Wn]
