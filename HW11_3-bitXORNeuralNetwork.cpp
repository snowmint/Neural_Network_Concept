#include <bits/stdc++.h>

using namespace std;

double w11, w12, w13;
double w21, w22, w23;
double w31, w32, w33;
double w1y, w2y, w3y;

double biash1, biash2, biash3, biasy;

void setweights()
{
    // Set weights and biases here

    w11 = w12 = w13 = 1;
    w21 = w22 = w23 = 1;
    w31 = w32 = w33 = 1;
    w1y = 1;
    w2y = -1;
    w3y = 1;
    biash1 = 0;
    biash2 = 1;
    biash3 = 2;
}


// Don't modify the code below
int main()
{
    int x1, x2, x3;

    setweights();
    while(cin >> x1 >> x2 >> x3){
        double neth1 = w11*x1 + w21*x2 + w31*x3 - biash1;
        double neth2 = w12*x1 + w22*x2 + w32*x3 - biash2;
        double neth3 = w13*x1 + w23*x2 + w33*x3 - biash3;
        //printf("%.2lf, %.2lf, %.2lf\n", neth1, neth2, neth3);
        int outh1 = neth1 > 0 ? 1 : 0;
        int outh2 = neth2 > 0 ? 1 : 0;
        int outh3 = neth3 > 0 ? 1 : 0;
        
        double nety = w1y*outh1 + w2y*outh2 + w3y*outh3 - biasy;
        //printf("%.2lf\n", nety);
        int outy = nety > 0 ? 1 : 0;
        printf("XOR(%d, %d, %d) = %d\n", x1, x2, x3, outy);
    }
    return 0;
}