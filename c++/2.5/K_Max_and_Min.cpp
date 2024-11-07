#include<bits/stdc++.h>
using namespace std;

int main(){

     int a,b,c;
     cin >> a >> b >> c;

     int min_value = a;
     int max_value = a;

     if (b < min_value)
     {
        min_value = b;
     }
     if (b > max_value)
     {
        max_value = b;
     }


      if (c < min_value)
     {
        min_value = c;
     }
     if (c > max_value)
     {
        max_value = c;
     }
     
     cout << min_value << " " << max_value;

    return 0;
}