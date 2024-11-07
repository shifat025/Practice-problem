#include<bits/stdc++.h>
using namespace std;

int small_number(int A[], int n){

    int min_result = INT_MAX;

    for (int i = 0; i < n-1; i++)
    {
        for(int j = i + 1; j < n; j++)
        {
            min_result = min(min_result, A[i] + A[j] + (j-i));
        }
    }
    return min_result;
    

    
}

int main(){
     int T;
     cin >> T;

     while (T--)
     {
        int n;
        cin >> n;
        int A[n];
        for (int i = 0; i < n; i++)
        {
            cin >> A[i];
        }
        cout << small_number(A,n) << endl;
     }
     

    return 0;
}