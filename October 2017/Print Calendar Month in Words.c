#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    char a[11][10]={"January","February","March","April","May","June","July","August","September","October","November","December"};
    scanf("%d",&n);
    n--;
    if(n>=0&&n<12)
    printf("%s",a[n]);
    else
    printf("Invalid Input");
    return 0;


}
