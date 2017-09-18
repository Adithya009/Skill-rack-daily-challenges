n=int(input())
a=[]
for i in range(n):
    a.append(raw_input().strip())
b=["","",""]
for i in range(n):
    b[0]+=a[i][0:i+1]
for i in range(n):
    b[1]+=a[i][i+1:len(a[i])-i-1]
for i in range(n):
    b[2]+=a[i][len(a[i])-i-1:len(a[i])]
for i in b:
    print i
        
