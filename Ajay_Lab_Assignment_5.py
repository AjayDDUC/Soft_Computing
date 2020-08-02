import matplotlib.pyplot as plt
import numpy as np

def get_Relation():
    i,j = list(map(int,input("Enter the order of 1 Relation using space:").split()))
    x,y = list(map(int,input("Enter the order of 2 Relation using space:").split()))
    if j==x:
        R = list(map(float,input("Enter the element of 1 Relation using space:").split()))
        R = np.array(R).reshape(i,j)
        S = list(map(float,input("Enter the element of 1 Relation using space:").split()))
        S = np.array(S).reshape(x,y)
        S = S.T
    else:
        print("Operatio is not Perform on the give order because its required matrix multiply rule:")
    return i,y,R,S

def max_Production():
    i,y,R,S = get_Relation()
    RoS = [ max([ i*j for x,i in enumerate(row) for y,j in enumerate(col) if x==y]) for row in R for col in S]
    RoS = np.array(RoS).reshape((i,y))
    print("max-production Composition\n",RoS)
    return RoS

def max_min():
    i,y,R,S = get_Relation()
    R_S = [ max([ min(i,j) for x,i in enumerate(row) for y,j in enumerate(col) if x==y]) for row in R for col in S]
    R_S = np.array(R_S).reshape((i,y))
    print("min-max Composition\n",R_S)
    return R_S

max_Production()