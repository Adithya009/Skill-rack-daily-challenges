#Arieswaran
#If you're reading this , then my code is probably success... cheers!
s=raw_input().strip() #getting the input as a string 
a,b=s.split(" ")      #spliting the string into A and B (two numbers)
m=len(a)              #getting the length of A 
n=len(b)              #Getting the length of B 
l=max(m,n)            #Finding the maximum between the lengths of A and B 
if m<n:               #Magic
    for i in range(m,n):
        a='0'+a
else:
    for i in range(n,m):
        b='0'+b 
s=[]             
for i in range(0,l): #Adding same digit numbers here
    s.append(int(a[i])+int(b[i]))
for i in s[::-1]:    #Printing it in the reverse order
    print i,
#God bless you
