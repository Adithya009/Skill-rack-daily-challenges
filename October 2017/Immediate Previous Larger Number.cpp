//Arieswaran
//It's been a long day , without you my friend
#include <iostream>
 
using namespace std;

int main()
{
    int n,i,j,f;
    cin>>n;
    int a[n];
    for(i=0;i<n;i++)
    cin>>a[i];
    for(i=0;i<n;i++)
    {
        f=0;
        for(j=i-1;j>=0;j--)
        {
            if(a[i]<a[j])
            {
                cout<<a[j]<<" ";
                f=1;
                break;
            }
        }
        if(f==0)
        cout<<0<<" ";
    }
    return 0;


}
