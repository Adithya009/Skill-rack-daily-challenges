//Arieswaran
#include<stdio.h>

int main()
{
    char c;
    scanf("%c",&c);
    switch(c)
    {
        case 'r':
        case 'R':
        printf("RED");
        break;
        case 'g':
        case 'G':
        printf("GREEN");
        break;
        case 'b':
        case 'B':
        printf("BLUE");
        break;
        default:
        printf("UNDEFINED");
    }
    return 0;


}
