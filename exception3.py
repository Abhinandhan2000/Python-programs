try:
	a=["b",3,8,2]
	print(a[2])
except:
	print("Index error")


try:
	a=["b",3,8,2]
	print(a[2])
	raise IndexError
except IndexError:
	print("Index error")
