s=input("enter the name: ")
  
print ("The original string  is : ",end="") 
print (s) 

s= "".join(reversed(s)) 

print ("The reversed string(using reversed) is : ",end="") 
print (s)