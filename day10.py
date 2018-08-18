print("This program adds two numbers without the use of an arithmetic operator.")
a=int(input())
b=int(input())
n=[a,b]
addition=sum(n)
i=0
while True:
	if addition>i:
		i+=1
		continue
	else:
		break
print(i)
	