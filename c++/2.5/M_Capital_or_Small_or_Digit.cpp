#include<bits/stdc++.h>
using namespace std;

int main(){

     char X;
     cin >> X;

     if(65 <= X <=90){
        cout << "ALPHA" << endl;
        cout << "IS CAPITAL";
     }
     else if (X >= 97 && X <= 122){
        cout << "ALPHA" << endl;
        cout << "IS SMALL";
     }
     else
     {
        cout << "IS DIGIT";
     }
     

    return 0;
}