#include <iostream>
 
using namespace std;

int main()
{
    int r,c,s=0,i,j;
    cin>>r>>c;
    int a[r][c];
    for(i=0;i<r;i++)
    for(j=0;j<c;j++)
    cin>>a[i][j];
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            if(i==0||j==0||i==(r-1)||j==(c-1))
            s+=a[i][j];
        }
    }
    cout<<s;
    return 0;

}
