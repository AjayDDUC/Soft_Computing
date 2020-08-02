import matplotlib.pyplot as plt
import numpy as np

class Composition:
    def __init__(self):
        self.i =None
        self.j = None
        self.x = None
        self.y = None
        self.R = None
        self.S = None
        self.get_Relation()

    def get_Relation(self):
        self.i,self.j = list(map(int,input("Enter the order of 1 Relation using space:").split()))
        self.x,self.y = list(map(int,input("Enter the order of 2 Relation using space:").split()))
        if self.j==self.x:
            self.R = list(map(float,input("Enter the element of 1 Relation using space:").split()))
            self.R = np.array(self.R).reshape(self.i,self.j)
            self.S = list(map(float,input("Enter the element of 1 Relation using space:").split()))
            self.S = np.array(self.S).reshape(self.x,self.y)
            self.S = self.S.T
        else:
            print("Operatio is not Perform on the give order because its required matrix multiply rule:")


    def max_Production(self):
        RoS = [ max([ i*j for x,i in enumerate(row) for y,j in enumerate(col) if x==y]) for row in self.R for col in self.S]
        RoS = np.array(RoS).reshape((self.i,self.y))
        print("max-production Composition\n",RoS)
        return RoS

    def max_min(self):
        R_S = [ max([ min(i,j) for x,i in enumerate(row) for y,j in enumerate(col) if x==y]) for row in self.R for col in self.S]
        R_S = np.array(R_S).reshape((self.i,self.y))
        print("min-max Composition\n",R_S)
        return R_S



def main():
    obj = Composition()
    RoS=obj.max_Production()
    R_S=obj.max_min()
    # print(RoS)

if __name__ == "__main__":
    main()

"""
i,j = 3 4
x,y = 4 2
R = .1 .3 .5 .7   .4 .2 .8 .9   .6 .8 .3 .2
S = .9 .1  .2 .3  .5 .6  .7 .2
RoS =? max-production_Composition
Answer
RoS =
[[0.49 0.3 ]
 [0.63 0.48]
 [0.54 0.24]]

R_S =? max-min_Composition 
Answer
R_S =
[[0.7 0.5]
 [0.7 0.6]
 [0.6 0.3]]
"""