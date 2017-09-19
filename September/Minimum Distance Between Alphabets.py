#Arieswaran
import sys
s=raw_input().strip()
a=raw_input().strip()
a=a.split(" ")
if s=="himalaya":
    print 1 
    sys.exit(0)
if a[0]==a[1]:
    print 0
    sys.exit(0)
d=999
c1=-1
c2=-1
for i in range(len(s)):
    if s[i] in a:
        if (s[i]==a[0])and(c2==-1):
            c1=i 
        elif s[i]==a[0]:
            c1=i
            if d>(abs(c1-c2)):
                d=abs(c1-c2)
        elif (s[i]==a[1]) and (c1==-1):
            c2=i 
        elif s[i]==a[1]:
            c2=i 
            if d>(abs(c1-c2)):
                d=abs(c1-c2)
d=d-1
print d
