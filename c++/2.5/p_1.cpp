#include<bits/stdc++.h>
using namespace std;

int* get_array(int n){
    int* arr = new int[n];

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    return arr;
    

}

int main(){

     int N; 
     cin >> N;

     int* ar = get_array(N);

     for (int i = 0; i < N; i++)
     {
        cout << ar[i] << " " ;
     }
     

    return 0;
}