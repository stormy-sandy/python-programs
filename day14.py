print("User input length of pattern.")
num=int(input())
def pattern():
	for j in range(num):
		print("		* \n")
		print("	*		*\n")
def pat2():
		print("	|		|\n			_  \n")
		print("	|		|\n		/        \  \n")
		print("	  \	  /       |\n")
		print("		|\n			\         /   \n")
		print("		|               _\n")

print("If you want pattern, press b. Else, press any other key.")
a=input()
while True:
	if a=='b':
		pattern()
		break
	else:
		pat2()
		break

