#Arieswaran
n=int(input())
l,r=0,0
m=2*n-1
for i in range(m):
    l=i+1
    r=(2*m)-i-1
    if(i==0 or i==m-1):
        for j in range(m):
            if(j==n-1):
                print i+1,
            else:
                print 0,
        print ""
        continue
    for j in range(m):
        l1=n-i-1
        l1=abs(l1)
        r1=n+i-1
        if(r1>m-1):
            z=r1-m+1
            r1=m-z-1
        if(j==l1):
            print l,
        elif(j==r1):
            print r,
        else:
            print 0,
    print ""
        
