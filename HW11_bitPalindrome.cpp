#include <bits/stdc++.h>

using namespace std;

double wh1[10]={0};
double wh2[10]={0};
double w1y=0, w2y=0;
double biash1=0, biash2=0, biasy=0;

void setweights()
{
  for(int i=0;i<5;i++){
    wh1[i] = pow(2, i);
    wh2[i] = -wh1[i];
  }
  for(int i=5;i<10;i++){
    wh1[i] = -pow(2, 10-i-1);
    wh2[i] = -wh1[i];
  }
  biash1 = biash2 = -1.0;
  w1y = w2y = biasy = 1.0;
}


// Don't modify any code below
int main()
{
    int val, x[10];

    setweights();
    while(cin >> val){
        for(int i=0, mask=0x01; i<10; i++, mask <<=1)
            x[i] = val & mask ? 1 : 0;
        double net1=0, net2=0;
        for(int i=0; i<10; i++){
            net1 += wh1[i] * x[i];
            net2 += wh2[i] * x[i];
        }
        net1 -= biash1;
        net2 -= biash2;
        int outh1 = net1 > 0 ? 1 : 0;
        int outh2 = net2 > 0 ? 1 : 0;
        double nety = w1y * outh1 + w2y * outh2 - biasy;
        int y = nety > 0 ? 1 : 0;
        for(int i=0; i<10; i++) cout << x[9-i];
        cout << (y ? " is " : " is not ") << " a 10-bit palindrome.\n";
    }
    return 0;
}