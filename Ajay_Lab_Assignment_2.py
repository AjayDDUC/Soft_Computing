import matplotlib.pyplot as plt
import numpy as np
def tri_mf(x,param):
    y=list()
    a,b,c = param[0],param[1],param[2]
    for i in x:
        y.append(max(min((i-a)/(b-a),(c-i)/(c-b)),0))
    plt.plot(x,y)
    plt.show()

def trape_mf(x,param):
    y=list()
    a,b,c,d = param[0],param[1],param[2],param[3]
    for i in x:
        y.append(max(min((i-a)/(b-a),1,(d-i)/(d-c)),0))
    plt.plot(x,y)
    plt.show()
def gau_mf(x,param):
    y=list()
    c,s_d = param[0],param[1]
    for i in x:
        y.append((np.exp(-0.5*((i-c)/s_d)**2)))
    plt.plot(x,y)
    plt.show()

def bell_mf(x,param):
    y=list()
    a,b,c = param[0],param[1],param[2]
    for i in x:
        y.append((1/(1+np.abs(((i-c)/a))**(2*b))))
    plt.plot(x,y)
    plt.show()
    
x= [x for x in range(101)]
param = [20,4,50]
# tri_mf(x,param)
# trape_mf(x,param)
# gau_mf(x,param)
# bell_mf(x,param)