class FuzzySet:
	def __init__(self):
		self.A=None
		self.B=None
		self.getFuzzySet()

	def getFuzzySet(self):
		element_A = list(map(int,input("Enter element of FuzzySet A with space:").split()))
		membership_A = list(map(float,input("Enter Membership value FuzzySet A with space:").split()))
		element_B = list(map(int,input("Enter element FuzzySet B with space:").split()))
		membership_B = list(map(float,input("Enter membership value FuzzySet B with space:").split()))
		self.A = [[x,y] for x,y in zip(element_A,membership_A)]
		self.B = [[x,y] for x,y in zip(element_B,membership_B)]
		


	def union_(self):
		A_B = list()
		if len(self.A)==len(self.B):
			for x,y in zip(self.A,self.B):
				if x[0] == y[0]:
					x[1]=max(x[1],y[1])
					A_B.append(x)
			print("\n\nUnion of A & B",A_B)

	def complement_(self):
		A_ = list()
		B_ = list()
		for x,y in zip(self.A,self.B):
			A_.append((x[0],1-x[1]))
			B_.append((y[0],1-y[1]))
		print("\n\nComplement of A:",A_)
		print("Complement of B:",B_)



	def intersection_(self):
		# A,B = getFuzzySet(self)
		A_B = list()
		if len(self.A)==len(selfB):
			for x,y in zip(self.A,self.B):
				if x[0] == y[0]:
					x[1]=min(x[1],y[1])
					A_B.append(x)
			print("\n\nIntersection of A & B:",A_B)
		else:
			print("Operation is not performed because Set size is not equal")



	def sum_(self):
		# A,B = getFuzzySet(self)
		if len(self.A)==len(self.B):
			for x,y in zip(self.A,self.B):
				if x[0]==y[0]:
					A_B = [(x[0],(x[1]+y[1]-x[1]*y[1])) for x in self.A for y in self.B]
			print("\n\nSum A+B:",A_B)
		else:
			print("Operation is not performed because Set size is not equal")

	def difference_(self):
		if len(self.A)==len(self.B):
			#B'
			B_ = list()
			for x in self.B:
				B_.append((y[0],1-y[1]))
			#A and B'
			AB_ = list()
			for x,y in zip(self.A,B_):
				if x[0] == y[0]:
					x[1]=min(x[1],y[1])
					AB_.append(x)
			print("\n\nSum A-B:",AB_)
		else:
			print("Operation is not performed because Set size is not equal")


	def cartesianProduct_(self):
		A_B = [[(x[0],y[0]),min(x[1],y[1])] for x in self.A for y in self.B]
		print("\n\nAxB",A_B)

def main():
	
	print("\nFuzzySet Operation.")
	print("1. Sum.")
	print("2. Union.")
	print("3. Difference.")
	print("4. Complement.")
	print("5. Intersection.")
	print("6. Cartesian_Product.")
	print("0. Exit(NO Operation)")
	x=int(input("Which Operation you want to perform on FuzzySet:"))
	
	if x==0:
		print("\nThank You!")
		return
	if x==1:
		obj = FuzzySet()
		obj.sum_()
		print('\n\n\nOperation Loading...')
		main()
	elif x==2:
		obj = FuzzySet()
		obj.union_()
		print('\n\n\nOperation Loading...')
		main()
	elif x==3:
		obj = FuzzySet()
		obj.difference_()
		print('\n\n\nOperation Loading...')
		main()
	elif x==4:
		obj = FuzzySet()
		obj.complement_()
		print('\n\n\nOperation Loading...')
		main()
	elif x==5:
		obj = FuzzySet()
		obj.intersection_()
		print('\n\n\nOperation Loading...')
		main()
	elif x==6:
		obj = FuzzySet()
		obj.cartesianProduct_()
		print('\n\n\nOperation Loading...')
		main()
		
if __name__ == '__main__':
	main()
