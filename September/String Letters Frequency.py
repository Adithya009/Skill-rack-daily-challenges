def bsort(c):
  for j in range(len(c)):
    for i in range(len(c)-1):
        if c[i][1]<c[i+1][1]:
            t=c[i]
            c[i]=c[i+1]
            c[i+1]=t 
    
    
s=raw_input().strip()
c=[]
t=0
for i in range(65,123):
    t=0
    for a in s:
        if chr(i)==a:
            t+=1 
    if(t>0):
        c.append(chr(i)+str(t))
bsort(c)
for i in c:
    print i
