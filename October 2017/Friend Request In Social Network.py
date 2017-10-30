#Arieswaran
#I dedicate this code to Epcipha (the birthday girl) !
n=int(input())
a=[]
f=[]
new=[]
for i in range(n): #Loop to get the input 
    b=raw_input().strip()
    a.append(b.split(" "))
for i in a: #Loop to find John's friend list
    f.append(i[0])
for i in a: #It's time to find new friends
    for j in i[2::]:
        if j not in f:
            new.append(j)
for i in new: #Loop to print out new friends
    print i,

#God bless you        
####Question#####
'''
Friend requests in social network
                                                 In a social 
network, a person can invite friends of his/her friend. John wants to 
invite and add new friends. Complete the program below so that it prints
 the names of the persons to whom John can send a friend request.


Input Format:
The first line contains the value of the N which represent the number of friends.
Next N lines contain the name of the friend F followed by the number of friends of F and finally their names separated by space.


Boundary Conditions:
2 <= N <= 10


Output Format:
The names to which John can send a friend request.


Example Input/Output 1:
Input:
3
Mani 3 Ram Raj Guna
Ram 2 Kumar Kishore
Mughil 3 Praveen Naveen Ramesh


Output:
Raj Guna Kumar Kishore Praveen Naveen Ramesh


Explanation:
Ram is not present in the output as Ram is already John's friend.


Example Input/Output 2:
Input:
4
Arjun 3 Bhuvana Ramya Rajesh
Naveen 2 Arjun Sangeetha
Rajesh 3 Narmada Madan Suresh
Suresh 2 Pawan Adhil


Output:
Bhuvana Ramya Sangeetha Narmada Madan Pawan'''
