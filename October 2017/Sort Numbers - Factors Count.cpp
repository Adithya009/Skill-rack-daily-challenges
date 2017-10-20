//Arieswaran
//This code is horrible, isn't it?
#include<iostream>
 
using namespace std;

int fuck(int &a,int &b) //swaping function
{
    int temp;
    temp=a;
    a=b;
    b=temp;
//    cout<<"Swaping\n"<<b<<" "<<a<<endl;
    return 0; //returns 0
}

int main()
{
  int n,i,f,j,t;
  cin>>n;
  int a[n][2];      //a[x][0] is the number a[x][1] is the factors count of the number
  for(i=0;i<n;i++)
  {
      cin>>a[i][0];      //reading the input
      f=0;               //factors count initializing to 0
      for(j=2;j<=a[i][0]/2;j++) //finding factors count
      {
          if(a[i][0]%j==0)  //if factor 
          f++;              //increases f by 1 
      }
      a[i][1]=f;            //assigning factors count to the array
  }
//  for(i=0;i<n;i++)
//  cout<<a[i][0]<<" "<<a[i][1]<<endl;
  for(i=0;i<n-1;i++)    //I hope it's bubble sort , not sure though
  {
    for(j=0;j<n-i-1;j++)
    {
        if(a[j][1]==a[j+1][1])
        {
            if(a[j][0]>a[j+1][0])
            {
                fuck(a[j][0],a[j+1][0]);
                fuck(a[j][1],a[j+1][1]);
            }
        }
        else if(a[j][1]>a[j+1][1])
        {
            fuck(a[j][0],a[j+1][0]);
            fuck(a[j][1],a[j+1][1]);
        }
    }
  }
  for(i=0;i<n;i++)  //Prints the numbers in sorted order
  cout<<a[i][0]<<" "; 
//  cout<<"Arieswaran";
  return 0;      //returns 0

}
