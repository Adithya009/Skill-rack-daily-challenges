#Arieswaran
a=raw_input().strip()
b=""
n=len(a)
for i in range(n-1):
    if a[i] in b:
        continue
    for j in range(i+1,n):
        if a[i]==a[j]:
            b+=a[i]
            break;
print b
