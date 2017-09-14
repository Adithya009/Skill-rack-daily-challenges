void printPattern(int n)
{
    int i,j,m;
    for(i=1;i<=n;i++)
    {
        for(j=0;j<=n;j++)
        {
            if(i%2==0)
            {
                if(j==0)
                printf("%d ",i+1);
                else
                printf("%d ",i);
                
            }
            else
            {
                if(j==n)
                printf("%d ",i+1);
                else
                printf("%d ",i);
            }
        }
        printf("\n");
        
    }

}
