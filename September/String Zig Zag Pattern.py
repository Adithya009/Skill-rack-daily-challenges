a=raw_input().strip()
b=int(input())
n=len(a)%b
if (n!=0):
    n=b-n
    a=a+"*"*n
j=0
for i in range(0,len(a),b):
   if(j%2==0):
       print(a[i:i+b:1])
   else:
        print(a[i+b-1:i-1:-1])
   j+=1 
