#Arieswaran
#It's been a long day without you my friend (Python)
a=raw_input().strip()
a=a.split(" ")
aj=[]
for i in a:
    j=i.split("@")
    j[1]=float(j[1])
    aj.append(j)
aj.sort(key=lambda x:x[1])
print aj[0][0]
