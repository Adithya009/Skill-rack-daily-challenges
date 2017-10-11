//Arieswaran
//This code is shit. Don't waste your time, find a better one
#include<stdio.h>
#include <stdlib.h>
#define TRUE 0 
int main()
{
    int a,b,c,i,count=0;
    scanf("%d%d%d",&a,&b,&c);
    //printf("%d\n%d\n%d",a,b,c);
    i=1;
    while(!TRUE)
    {
        if((i%a==0)&&(i%b==0)&&(i%c==0))
        {
            printf("%d ",i);
            count++;
        }
        if(count==5)
        break;
        i++;
    }
    return 0;


}
