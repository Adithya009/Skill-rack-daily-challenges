a=raw_input().split()
d=0
t=0
b=[]
for i in a:
    b.append(i.split('@'))
for i in b:
    d+=int(i[0])
    t+=int(i[1])
avg=float(d)/float(t) 
print "%.2f kmph"%avg
