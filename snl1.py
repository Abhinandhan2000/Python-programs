import random
p=0
d=0
def rolldice():
	return random.randint(1,6)
while True:
	r=input("press r to roll dice  ")
	if(r=="r"):
		d=rolldice()
		print("you got ",d)
	if d==1 or d==6:
		p=d
		break
print("you are in the game!\n you are at " ,p)
while True:
	r=input("press r to roll dice  ")
	if(r=="r"):
		d=rolldice()
		print("you got ",d)
		p=p+d
		print("you are at " ,p)
		if p==100:
			print("hurray! you won")
			exit()
		if p>100:
			p=p-d
			print("you need ", 100-p ,"to win")
		if p==8:
			p=37
			print("wow ladder! you moved to" ,p)
		if p==13:
			p=34
			print("wow ladder! you moved to" ,p)
		if p==40:
			p=68
			print("wow ladder! you moved to" ,p)
		if p==52:
			p=81
			print("wow ladder! you moved to" ,p)
		if p==76:
			p=97
			print("wow ladder! you moved to" ,p)
		if p==11:
			p=2
			print("ah snake! you moved to" ,p)
		if p==25:
			p=4
			print("ah snake!you moved to" ,p)
		if p==38:
			p=9
			print("ah snake!you moved to" ,p)
		if p==65:
			p=46
			print("ah snake!you moved to" ,p)
		if p==89:
			p=70
			print("ah snake!you moved to" ,p)
		if p==93:
			p=64
			print("ah snake!you moved to" ,p)
