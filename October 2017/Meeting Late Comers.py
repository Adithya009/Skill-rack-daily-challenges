#Arieswaran
#I'm in a hurry, so no comments
s=raw_input().split(" ")
c=0                          #count
for i in range(len(s)):
    s[i]=s[i].split(':')
for i in s:
    if int(i[0])>10:
        c+=1 
    elif int(i[0])==10:
        if int(i[1])>0:
            c+=1
print c
    
