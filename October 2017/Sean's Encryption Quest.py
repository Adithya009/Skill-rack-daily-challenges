#Arieswaran
#May God bless this code 
import sys
x=int(raw_input())
k=int(raw_input())
m=raw_input().strip()
if(x>1 or x<-1):              #I've to save my program from idiots
    print "Invalid Input"   #so , here we go....
    sys.exit()              #I can't take this anymore
e=""                   #encrypted message
for i in m:            #i takes every character of the message
    n=ord(i)           #ascii value of i 
    d=n-65             #converting it in range of 26.(ascii A=65,Z=90)
    d+=k               #adding encrypted key to d 
    k+=x               #adding the encrypting type to key
    d=d%26             #converting d in range of 26
    e+=chr(65+d)       #converting d to ascii value(+65) and converting it into character
print e                #printing the encrypted message
