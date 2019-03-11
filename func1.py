#Function without parameter
def fun():
	print("LOL")
fun()

#Function with parmeter
def fun1(a):
	b=a+1
	print(b)
fun1(3)

#Function with parameters
def fun2(a,b,c):
	h=a+b
	print(a)
	print(b)
	print(h)
	print(c)
fun2(5,3,"HAHA")

#Function with default parameter.
def fun3(a=5,b="nah"):
	print(a)
	a=a+6
	print(a)
	print(b)
fun3(6,"Yep")
fun3()
fun3(0,"k")

#Function with return value
def fun4(a=55,b=24):
	c=a+b
	return(c)
w=fun4()
print(w)

#Function calling other function
def fun5(x):
	d=fun4(2,5)
	y=x+d
	print(y)
fun5(2)
