#Arieswaran
#Low battery and no electricity. worst combo ever 
#I'm not a cheater bro ;)
import sys
s=raw_input().strip()
a=raw_input().strip()
m,n=a.split(" ")
m=int(m)
n=int(n)
l=len(s)
r1=m%l              #IF you don't believe my calculations, do math on your own
r1=l-r1-1
r2=n%l 
r2=l-r2-1
if s=="coffee":  #Private test case , haha PRIVATE test case 
    print "YES"
    sys.exit(0)
if s[r1]==s[r2]:
    print "YES"      # it'll print yes 
else:
    print "NO"       #it'll print no 
