#include<bits/stdc++.h>
using namespace std;

void sort_string(string &s)
{

   sort(s.begin(), s.end());
    
}

int main(){

     int n;
     cin >> n;
     cin.ignore();
     string s[n];
     for (int i = 0; i < n; i++)
     {
        getline(cin,s[i]);
     }
     
      for (int i = 0; i < n; i++) 
      {
        sort_string(s[i]);
      }

    // Output the sorted strings
    for (int i = 0; i < n; i++) 
    {
        cout << s[i] <<endl;
    }

    return 0;
}