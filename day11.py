import random
def daring():
	while True:
		n=int(input("Input an integer from 1 to 10."))
		s=random.randint(0,10)
		if n==s:
			print("congratulations")
			continue
		else:
			print("I am sorry")
			break
daring()


