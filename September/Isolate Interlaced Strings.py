a=raw_input().strip()
b=int(input())
s1=""
s2=""
if len(a)>2*b:
 for i in range(len(a)):
    if i<2*b:
        if i%2==0:
            s1+=a[i]
        else:
            s2+=a[i]
    else:
        s2+=a[i]
else:
    n=len(a)-b
    for i in range(len(a)):
        if i<2*n:
            if i%2==0:
                s1+=a[i]
            else:
                s2+=a[i]
        else:
            s1+=a[i]
print s1+"\n"+s2
    
