  class Composition:
    def __init__(self):
        self.R1 = np.array([[.1, .3, .5, .7],
                   [.4, .2, .8, .9],
                   [.6, .8, .3, .2]])
        self.R2 = np.array([[.9, .1],
                   [.2, .3],
                   [.5, .6],
                   [.7, .2]]).T

    def max_Production(self):
        RoS = [ max([ i*j for x,i in enumerate(row) for y,j in enumerate(col) if x==y]) 
        for row in self.R1 for col in self.R2]
        RoS = np.array(RoS).reshape((self.R1.shape[0],self.R2.shape[0]))
        print("max-production Composition\n",RoS)
  

    def max_min(self):
        R_S = [ max([ min(i,j) for x,i in enumerate(row) for y,j in enumerate(col) if x==y]) 
        for row in self.R1 for col in self.R2]
        R_S = np.array(R_S).reshape((self.R1.shape[0],self.R2.shape[0]))
        print("min-max Composition\n",R_S)
