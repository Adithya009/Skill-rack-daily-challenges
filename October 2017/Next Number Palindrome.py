'''Next Number Palindrome

Given a number N, the program must print the next palindromic number P.

Boundary Conditions:
9 < N < 100000



Input Format:
First line will contain the number N


Output Format:
First line will contain the next palindromic number P.


Sample Input/Output:


Example 1:
Input:
909


Output:
919


Example 2:
Input:
2131


Output:
2222
'''
n=int(input())
while(13):
  n+=1
  s=str(n)
  if(s==s[::-1]):
    print s
    break;
