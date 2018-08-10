while True:
	print("Welcome user. Type one of the given numbers to get a corresponding character.")
	print("1-A 2-B 3-C 4-D 5-E 6-F 7-G")
	num=int(input("Enter your number--"))
	print("The character you asked for is:")
	if num==1:
		print("A")
	elif num==2:
		print("B")
	elif num==3:
		print('C')
	elif num==4:
		print("D")
	elif num==5:
		print("E")
	elif num==6:
		print("F")
	elif num==7:
		print("G")
	else:
		print("No character.")
		print("Enter only the aforementioned digits.")
	print("Press Enter 0 to input characters again.")
	more=int(input())
	if more==0:
		continue
	else:
		break
	