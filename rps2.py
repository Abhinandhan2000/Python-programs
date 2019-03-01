import random
a=0
b=0
l=['rock','paper','scissor']
d={'r':'rock','p':'paper','s':'scissor'}
while True:
	i=input("enter choice rock,paper,scissor \nq to quit \n")
	if i=='q':
		if(a>b):
			print("Computer wins the game by ",a,"-",b)
		elif(a==b):
			print("It's a tie ",a,"-",b)
		else:
			print("You win the game by ", b,"-",a)
		exit()
	print("your choice ",d[i])
	c=random.choice(l)
	print("comp's choice ",c)
	if(d[i]==c):
		print('tie')
		a=a
		b=b
	elif d[i]=='rock' and c=='paper':
		print('comp wins')
		a=a+1
	elif d[i]=='scissor' and c=='rock':
		print('comp wins')
		a=a+1
	elif d[i]=='paper' and c=='scissor':
		print('comp wins')
		a=a+1
	elif d[i]=='paper'and c=='rock':
		print('you win')
		b=b+1
	elif d[i]=='rock'and c=='scissor':
		print('you win')
		b=b+1
	elif d[i]=='scissor'and c=='paper':
		print('you win')
		b=b+1
	else:
		print("invalid input")
	print ("comp = " ,a ,"\nuser = " ,b)
