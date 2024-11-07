#include<bits/stdc++.h>
using namespace std;

int main(){

     int n;
     cin >> n;

     int array[1000];

     for (int i = 0; i < n; i++)
     {
        cin >> array[i];
     }
     
     for (int i = 0; i < n; i++)
     {
        if (array[0] < array[i])
        {
            array[0] = array[i];
        }
        
     }
     cout << array[0];

    return 0;
}