import matplotlib.pyplot as plt
import numpy as np
class Fuzzy_MF:
    def __init__(self):
        self.x =None
        self.param = None
        self.get_Param()

    def get_Param(self):
        
        temp = list(map(int,input("Enter the range of x range:").split('-')))
        self.x = [i for i in range(temp[0],temp[1])]
        self.param = list(map(int,input("Enter the param using space:").split()))

    def tri_mf(self):
        if len(self.param) == 3:
            y=list()
            a,b,c = self.param[0],self.param[1],self.param[2]
            for i in self.x:
                y.append(max(min((i-a)/(b-a),(c-i)/(c-b)),0))
            plt.plot(self.x,y)
            plt.show()
        else:
            print("\n\nPlease enter valid len of Parameter:")


    def trape_mf(self):
        if len(self.param) == 4:
            y=list()
            a,b,c,d = self.param[0],self.param[1],self.param[2],self.param[3]
            for i in self.x:
                y.append(max(min((i-a)/(b-a),1,(d-i)/(d-c)),0))
            plt.plot(self.x,y)
            plt.show()
        else:
            print("\n\nPlease enter valid len of Parameter:")


    def gau_mf(self):
        if len(self.param) == 2:
            y=list()
            c,s_d, = self.param[0],self.param[1]
            for i in self.x:
                y.append((np.exp(-0.5*((i-c)/s_d)**2)))
            plt.plot(self.x,y)
            plt.show()
        else:
            print("\n\nPlease enter valid len of Parameter:")


    def bell_mf(self):
        if len(self.param) == 3:
            y=list()
            a,b,c = self.param[0],self.param[1],self.param[2]
            for i in self.x:
                y.append((1/(1+np.abs(((i-c)/a))**(2*b))))
            plt.plot(self.x,y)
            plt.show()
        else:
            print("\n\nPlease enter valid len of Parameter:")


    def sig_mf(self):
        if len(self.param) == 2:
            y=list()
            a,c = self.param[0],self.param[1]
            for i in self.x:
                y.append((1/(1+np.exp(-a*(i-c)))))
            plt.plot(self.x,y)
            plt.show()
        else:
            print("\n\nPlease enter valid len of Parameter:")

def main():
	
	print("\nFuzzy Membership Fuction.")
	print("1. Triangular MF.")
	print("2. Trapezoidal MF.")
	print("3. Gaussian MF.")
	print("4. Bell MF.")
	print("5. Sigmoid MF.")
	print("0. Exit")
	x=int(input("Which Operation you want to perform on Fuzzy_MF:"))
	
	if x==0:
		print("\nThank You!")
		return
	elif x==1:
        # print("Note: this function required 3 parameter:")
		obj = Fuzzy_MF()
		obj.tri_mf()
		print('\n\nMFs Loading...')
		main()
	elif x==2:
        # print("Note: this function required 4 parameter:")
		obj = Fuzzy_MF()
		obj.trape_mf()
		print('\n\nMFs Loading...')
		main()
	elif x==3:
        # print("Note: this function required 2 parameter:")
		obj = Fuzzy_MF()
		obj.gau_mf()
		print('\n\nMFs Loading...')
		main()
	elif x==4:
        # print("Note: this function required 3 parameter:")
		obj = Fuzzy_MF()
		obj.bell_mf()
		print('\n\nMFs Loading...')
		main()
	elif x==5:
        # print("Note: this function required 1 parameter:")
		obj = Fuzzy_MF()
		obj.sig_mf()
		print('\n\nMFs Loading...')
		main()
	
if __name__ == '__main__':
	main()