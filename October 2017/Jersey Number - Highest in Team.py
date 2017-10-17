#Arieswaran
#I hope this code will be hard to read, curse me later ;)
n=int(raw_input().strip())
s=raw_input().strip()
a=s.split(" ")
for i in range(len(a)):
    a[i]=int(a[i])             ###**-- IF ANYBODY FOUND A BETTER WAY TO CHANGE THE ARRAY ELEMENTS TO INT , please mail me with the solution . mail: arieswaran@gmail.com --**###
m=int(raw_input())
#fuck, i got all the inputs, what to do next?
t=n/m 
r=n%m 
#I don't know what I'm doing here....
teams=[]
for i in range(t):
    teams.append([])
    for j in range(i*m,i*m+m):       #fuck the for loop
        teams[i].append(a[j])
if(r!=0):
    for i in range(r):
        teams[i].append(a[t*m+i])
#Wow, I think I divided them into a team without a violence
for i in teams:
    max=0;
    for j in i:
        if(j>max):
            max=j 
    print max," ",
#fuck , private test cases failed..... :(

