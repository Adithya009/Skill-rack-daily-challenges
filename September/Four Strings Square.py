a=[]
for i in range(4):
    a.append(raw_input().strip())
n=len(a[0])
for i in range(1,4):
    if a[0][n-1]==a[i][0]:
        b=a[i]
for i in range(1,4):
    if b==a[i]:
        continue
    elif b[n-1]==a[i][0]:
        c=a[i]
for i in range(1,4):
    if b==a[i] or c==a[i]:
        continue
    elif c[n-1]==a[i][0]:
        d=a[i]
op=a[0]
for i in range(1,n-1):
    op+="\n"
    for j in range(n):
        if j==0:
            op+=d[n-i-1]
        elif j==n-1:
            op+=b[i]
        else:
            op+="*"
op+="\n"
op+=c[::-1]
print(op)
