l=[]
print (l)
l1=[12,'abc',88,24,'def',52]
print(l1)
print(l1[4])
for i in range(0,4):
	print(l1[i])
l1[2]=15
print(l1)
print(len(l1))
if 55 in l1:
	print('s')
elif 12 in l1:
	print('ss')
else:
	print('n')
l1.append('app')
print(l1)
import random
r=input('enter choice')
print(random.randint(1,8),"random")
s=random.choice(l1)
print(s)