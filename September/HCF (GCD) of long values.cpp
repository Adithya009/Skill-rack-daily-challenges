#include <iostream>
 
using namespace std;

long int gcd(long int a,long int b)
{
    return b==0?a:gcd(b,a%b);
}

int main()
{
    long int a,b,hcf;
    cin>>a>>b;
    hcf=gcd(a,b);
    cout<<hcf;


}
