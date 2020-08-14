import numpy as np
import matplotlib.pyplot as plt

def bell_mf(age,param):
    y=list()
    a,b,c = param[0],param[1],param[2]
    for x in age:
        y.append((1/(1+np.abs(((x-c)/a))**(2*b))))
    return np.array(y)

def show():
    plt.plot(age, young_mfv, label = "Young(x)")
    plt.plot(age, old_mfv, label = "Old(x)")
    plt.legend()
    plt.show()


def more_or_less_young():
    y = [np.sqrt(mfv) for mfv in young_mfv]
    plt.plot(age, young_mfv, label = "Young(x)")
    plt.plot(age, old_mfv, label = "Old(x)")
    plt.plot(age,y, label = "more_or_less_young")
    plt.legend()
    plt.show()

def intersection(A,B):
    return [ [max(x,y)] for x,y in zip(A, B )]
    
def not_young_and_not_old():
    young_neg = 1-young_mfv #not_young
    old_neg = 1-old_mfv #not_old
    new_mfv = intersection(young_neg, old_neg) #not_young_and_not_old
    plt.plot(age, young_mfv, label = "Young(x)")
    plt.plot(age, old_mfv, label = "Old(x)")
    plt.plot(age,new_mfv, label = "not_young_and_not_old")
    plt.legend()
    plt.show()

def young_but_not_too_young():
    y = np.array([np.power(mfv,2) for mfv in young_mfv]) #too_young
    young_neg = 1-y #not_too_young
    new_mfv = intersection(young_mfv, young_neg) #young_but_not_too_young
    plt.plot(age, young_mfv, label = "Young(x)")
    plt.plot(age, old_mfv, label = "Old(x)")
    plt.plot(age,new_mfv, label = "young_but_not_too_young")
    plt.legend()
    plt.show()
    

def extremely_old():
    y = [np.power(mfv, 8) for mfv in old_mfv] #extremly_old
    plt.plot(age, young_mfv, label = "Young(x)")
    plt.plot(age, old_mfv, label = "Old(x)")
    plt.plot(age,y, label = "extremely_old")
    plt.legend()
    plt.show()

age = [i for i in range(101)]
young_mfv = bell_mf(age,[20,2,0])
old_mfv = bell_mf(age,[30,3,100])

# show()
more_or_less_young()
not_young_and_not_old()
young_but_not_too_young()
extremely_old()