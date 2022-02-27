
def eight():
	"""results in eight"""
	print(5+3)
	print(11-3)
	print(4*2)
	print(16/2)

eight()

def favorite():
	"""reveals"""
	num=7
	message="My favorite number is: "
	print(message + str(num))

favorite()

def number_sets():
	num_1=456234
	num_2=68423791
	num_3=13794628
	num_4=96374
	print(num_1, num_2, num_3, num_4)

number_sets()

def duo_argu(ar_1, ar_2):
	ar_1=input("Enter argument 1: ")
	ar_1=int(ar_1)
	print(ar_1)
	ar_1=input("Enter argument 2: ")
	ar_2=float(ar_2)
	print(ar_2)

duo_argu(1, 2)

def movie(fav, times):
	fav=input("What is your favorite movie?")
	fav=str()
	times=input("How many times have you seen it?")
	times=int()
	print("I have seen " + fav + times + " times.")

movie(1, 2)