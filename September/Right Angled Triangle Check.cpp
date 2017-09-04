#include <iostream>
 
using namespace std;

int main()
{
    int a,b,c,j,m;
    cin>>a>>b>>c;
    if(a>b&&a>c)
    {
        j=a*a;
        m=(b*b)+(c*c);
    }
    else if (b>c)
    {
        j=b*b;
        m=(a*a)+(c*c);
    }
    else
    {
        j=c*c;
        m=(a*a)+(b*b);
    }
    if(j==m)
    cout<<"YES";
    else
    cout<<"NO";
    return 0;


}
