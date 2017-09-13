#include <iostream>
 
using namespace std;

int main()
{
    int n,min=101,hcf=1,flag;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    cin>>a[i];
    for(int i=0;i<n;i++)
    if(a[i]<min)
    min=a[i];
    for(int i=2;i<=min;i++)
    {
        flag=1;
        for(int j=0;j<n;j++)
        if (a[j]%i!=0)
        {
            flag=0;
            break;
        }
        if(flag==1)
        hcf=i;
    }
    cout<<hcf;
    return 0;


}
