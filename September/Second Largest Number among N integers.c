//Arieswaran
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n,max=-999999,index;
    scanf("%d",&n);
    int a[n];
    for(int i=0;i<n;i++)
    scanf("%d",&a[i]);
    for(int i=0;i<n;i++)
    {
     if(a[i]>max)
     {
         max=a[i];
         index=i;
     }
    }
    a[index]=-999999;
    max=a[index];
    for(int i=0;i<n;i++)
    {
        if(a[i]>max)
        max=a[i];
    }
    printf("%d",max);
    return 0;


}
