import numpy as np
import matplotlib.pyplot as plt

class fuzzy_MF:
    def __init__(self):
        self.age = np.array([i for i in range(101)])
        self.young_param = [20, 2, 0]
        self.old_param = [30, 3, 100]
        self.young_mfv = self.bell_mf(self.young_param)
        self.old_mfv = self.bell_mf(self.old_param)
        self.more_less_young = None
        self.not_young_not_old = None
        self.young_not_too_young = None
        self.extremely = None

    def bell_mf(self, param):
        y = list()
        a, b, c = param[0], param[1], param[2]
        for x in self.age:
            y.append((1/(1+np.abs(((x-c)/a))**(2*b))))
        return np.array(y)

    def young_old(self):
        plt.plot(self.age, self.young_mfv, label="Young(x)")
        plt.plot(self.age, self.old_mfv, label="Old(x)")
        plt.legend()
        plt.show()

    def more_or_less_young(self):
        self.more_less_young = [np.sqrt(mfv) for mfv in self.young_mfv]
        plt.plot(self.age, self.young_mfv, label="Young(x)")
        plt.plot(self.age, self.old_mfv, label="Old(x)")
        plt.plot(self.age, self.more_less_young, label="more_or_less_young")
        plt.legend()
        plt.show()

    def intersection(self, A, B):
        return [[max(x, y)] for x, y in zip(A, B)]

    def not_young_and_not_old(self):
        young_neg = 1-self.young_mfv  # not_young
        old_neg = 1-self.old_mfv  # not_old
        self.not_young_not_old = self.intersection(young_neg, old_neg)  # not_young_and_not_old
        plt.plot(self.age, self.young_mfv, label="Young(x)")
        plt.plot(self.age, self.old_mfv, label="Old(x)")
        plt.plot(self.age, self.not_young_not_old,label="not_young_and_not_old")
        plt.legend()
        plt.show()

    def young_but_not_too_young(self):
        y = np.array([np.power(mfv, 2) for mfv in self.young_mfv])  # too_young
        young_neg = 1-y  # not_too_young
        self.young_not_too_young = self.intersection(
        self.young_mfv, young_neg)  # young_but_not_too_young
        plt.plot(self.age, self.young_mfv, label="Young(x)")
        plt.plot(self.age, self.old_mfv, label="Old(x)")
        plt.plot(self.age, self.young_not_too_young,label="young_but_not_too_young")
        plt.legend()
        plt.show()

    def extremely_old(self):
        self.extremely = [np.power(mfv, 8)for mfv in self.old_mfv]  # extremly_old
        plt.plot(self.age, self.young_mfv, label="Young(x)")
        plt.plot(self.age, self.old_mfv, label="Old(x)")
        plt.plot(self.age, self.extremely, label="extremely_old")
        plt.legend()
        plt.show()  
        
def main():
    print("\nFuzzySet Operation.")
    print("1. young_old.")
    print("2. more_or_less_young.")
    print("3. not_young_and_not_old.")
    print("4. young_but_not_too_young.")
    print("5. extremely_old.")
    print("0. Exit(NO Operation)")
    x = int(input("Which Operation you want to perform on FuzzySet:"))
    if x==0:
        print("\nThank You!")
        return
    elif x==1:
        obj = fuzzy_MF()
        obj.young_old()
        print('\n\n\nOperation Loading...')
        main()
    elif x==2:
        obj = fuzzy_MF()
        obj.more_or_less_young()
        print('\n\n\nOperation Loading...')  
        main()
    elif x==3:
        obj = fuzzy_MF()
        obj.not_young_and_not_old()
        print('\n\n\nOperation Loading...')
        main()
    elif x==4:
        obj = fuzzy_MF()
        obj.young_but_not_too_young()
        print('\n\n\nOperation Loading...')
        main()
    elif x==5:
        obj = fuzzy_MF()
        obj.extremely_old()
        print('\n\n\nOperation Loading...')
        main()
  
if __name__ == '__main__':
    main()