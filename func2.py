def max(a,b,c):
	if(a>b and a>c):
		return a
	elif(b>a and b>c):
		return b
	else:
		return c
a=input("First number ")
b=input("second number ")
c=input("Third number ")
m=max(a,b,c)
print(m, "is the largest number")


