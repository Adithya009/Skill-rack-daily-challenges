#include <iostream>
 
using namespace std;

int main()
{
    int n,s=0;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    cin>>a[i];
    for(int i=0;i<n;i++)
    if(a[i]>9&&a[i]<=99)
    s+=a[i];
    cout<<s;
    return 0;

}
