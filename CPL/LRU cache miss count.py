#Arieswaran
s,n=raw_input().strip().split(" ")
s=int(s)
n=int(n)
p=raw_input().strip().split(" ")
a=[]
c=0
for i in range(n):
    p[i]=int(p[i])
#print p
for i in range(s):
    a.append("")
for i in p:
    if i in a:
        a.remove(i)
        #print "Already",i
        a.append(i)
    else:
        c+=1
        #print i
        del a[0]
        a.append(i)
print c
