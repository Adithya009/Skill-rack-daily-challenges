//Arieswaran
void printPattern(int N)
{
    int i,j,a=1,f=0;
    for(i=0;i<N;i++)
    {
        f++;
        if(f%2!=0)
        a=i*N+1;
        else
        a=(i+1)*N;
        for(j=0;j<N;j++)
        {
            if(f%2!=0)
            {
                printf("%d ",a++);
            }
            else
            {
                printf("%d ",a--);
            }
            
        }
        printf("\n");
    }

}
