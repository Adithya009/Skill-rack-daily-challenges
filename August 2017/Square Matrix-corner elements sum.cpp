#include <iostream>
 
using namespace std;

int main()
{
 int n,i,j,sum=0;
 cin>>n;
 int a[n][n];
 for(i=0;i<n;i++)
  for(j=0;j<n;j++)
   cin>>a[i][j];
 sum+=a[0][0]+a[0][n-1]+a[n-1][0]+a[n-1][n-1];
 cout<<sum;
 return 0;

}
