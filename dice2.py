import random
while True:
	i=input("press r to roll\n press z to quit")
	if(i=="r"):
		print (random.randint(1,6))
	if(i=="z"):
		print ("end")
		exit()

