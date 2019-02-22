import random
i=0
while i<2:
	d=6
	i=input("press r to roll\n press z to quit")
	if(i=="r"):
		print ("you got" ,d)
		d=d/3
	if(i=="z"):
		print ("end")
	i=input("press r to roll\n press z to quit")
	if(i=="r"):
		print ("you got" ,d)
		d=d+1
i=i+1
	
print ("you won")
		