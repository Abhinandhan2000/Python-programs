import random
p=0
d=0
#dictionary of snake and ladder
snl={11:2,8:37,25:4,13:34,38:9,40:68,89:70,76:97,93:64,52:81,65:46}
#function to roll dice
def rolldice():
	return random.randint(1,6)
#rolling dice to start game
while True:
	r=input("press r to roll dice , q to quit ")
	if(r=="r"):
		d=rolldice()
		print("you got ",d)
		if d==1 or d==6:
			p=d
			print("you are in the game!\n you are at " ,p)
			break
		else:
			print("you need 1 or 6 to start")	
	elif r=='q':
	 exit() 
#changing of position for each roll
while True:
	r=input("press r to roll dice , q to quit ")
	if(r=="r"):
		d=rolldice()
		print("you got ",d)
		p=p+d
		if p==100:
			print("hurray! you won")
			exit()
		if p>100:
			p=p-d
			print("you need ", 100-p ,"to win")
		if p in snl:
			if(p<snl[p]):
				print("wow ladder! you moved to" )
			else:
				print("oh snake! you moved to" )
			p=snl[p]
			print(p)
		print("you are at " ,p)
	elif r=='q':
		exit()

