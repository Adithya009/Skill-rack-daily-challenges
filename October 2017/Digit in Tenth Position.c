//Arieswaran
//Easy peasy lemon squeezy
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n,t;               //number , Digit in Tenth
    scanf("%d",&n);        //getting the input on n 
    n=n/10;                //last digit(ex:143 last digit:3) will be removed.
    t=n%10;                //now, storing the last digit(tenth digit ex:143 ,3 already removed. 14, 4 is the last digit) in t 
    printf("%d",t);
    return 0;
}
