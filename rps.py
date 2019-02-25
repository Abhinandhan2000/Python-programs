import random
l=['r','p','s']
i=input("enter choice\n r/ p/ s ")
print("your choice ",i)
c=random.choice(l)
print("comp's choice ",c)
if(i==c):
	print('tie')
elif i=='r' and c=='p':
	print('comp wins')
elif i=='s' and c=='r':
	print('comp wins')
elif i=='p' and c=='s':
	print('comp wins')
elif i=='p'and c=='r':
	print('you win')
elif i=='r'and c=='s':
	print('you win')
elif i=='s'and c=='p':
	print('you win')
else:
	print('invalid input')
