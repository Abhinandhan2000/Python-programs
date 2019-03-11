#except
try:
	n= int(input("Give a number: "))
	print(n)
except:
	print("Type error")
else:
	print("is the number")
finally:
	print("done")

#except with raise
try:
	n1= int(input("Give a number: "))
	print(n1)
	raise ValueError
except ValueError:
	print("Invalid input")


