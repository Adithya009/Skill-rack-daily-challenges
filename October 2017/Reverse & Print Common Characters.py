#Arieswaran
#Happy Diwali , have a blast!
def com(s1,s2):
    common=""#function to print common letters
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            common+=s1[i]
    print common
    return 0

s1=raw_input().strip()
s2=raw_input().strip()
s2=s2[::-1]              #reversing the string2 , haha python..I'm in love with the power of python
if(len(s1)<len(s2)):
    com(s1,s2)
else:
    com(s2,s1)
