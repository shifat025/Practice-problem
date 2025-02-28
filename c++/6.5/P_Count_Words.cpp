#include<bits/stdc++.h>
using namespace std;

int main(){

     string s;
     getline(cin,s);
     int count = 0;
     bool word = false;

     for (int i = 0; i < s.length(); i++)
     {
        if((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z'))
        {
            if(!word)
            {
                count++;
                word = true;
            }
        }
        else
        {
            word = false;
        }
        

     }
     cout << count;
     

    return 0;
}