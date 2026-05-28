#include <iostream>
#include <string>
#include <cmath>

void sortArray(long arr[], int n);

int main()
{

    int n;
    std::cout<<"input the array size:   ";
    std::cin>> n;
    
    long arr[n];

    std::cout<<"assign values to array";
    for(int i=0; i<n; i++)
    std::cin>> arr[i];

    //sorting part
    sortArray(arr, n);

    for(long ar : arr)
    std::cout<< ar << " ";


    return 0;

}

void sortArray(long arr[], int n)
 {
    long temp;
    for(int i=0;i<n-1;i++)
    {
        for(int j=0;j<n-1-i;j++)
        {
            if(arr[j]>arr[j+1])
            {
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
 }