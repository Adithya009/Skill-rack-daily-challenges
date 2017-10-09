#This code is horrible , written in a hurry and I'm not proud of it
#Arieswaran
a=int(input()) 
b=int(input())
odd=[]                    #odd numbers array where we'll store odd numbers
even=[]
for i in range(a,b+1):
    if(i%2!=0):           #odd number
        odd.append(i)     #adding the odd number to the list
    else:                 #even number
        even.append(i)    #adding the even number to the list
m=len(odd)
n=len(even)
even=even[::-1]          #reversing the even numbers
if m==n:                 #if no. of odd and even numbers are equal
    for i in range(m):
        print odd[i],even[i],
elif m>n:                #if no. of odd numbers are greater than no. of even numbers
    for i in range(n):
        print odd[i],even[i],
    print odd[n]
else:                    #else
    for i in range(m):
        print even[i],odd[i],
    print even[m]
