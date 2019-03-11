def sum(l):
	s=0
	for i in l:
		s=s+i
	return(s)
l=[]
n=int(input("enter number of elements in list "))
for x in range(n):
	w=int(input("Enter elements "))
	l.append(w)
s=sum(l)
print(s,"is the sum of list ")




