#include <iostream>
 
using namespace std;

int main()
{
    int n,i,m=1,j,c=0;
    cin>>n;
    int a[n][n];
    for(i=0;i<n;i++)
    {
        if(i%2==0)
        {
            for(j=0;j<n;j++)
            {
                a[c][j]=m++;
            }
        }
        else
        {
            for(j=0;j<n;j++)
            {
                a[n-c-1][j]=m++;
            }
            c++;
        }
        
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        cout<<a[i][j]<<" ";
        cout<<endl;
    }
    return 0;


}
