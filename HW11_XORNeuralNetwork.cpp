#include <iostream>

using namespace std;

double w1h, w2h, w1y, w2y, why;
double biash, biasy;

void setweights()
{
    // Set weights and bias below
    w1h = 1.0;
    w2h = 1.0;
    biash = 1.5;

    w1y = 1.0;
    w2y = 1.0;
    why = -2.0;
    biasy = 0.5;
    /*
    w1h = 0.0;
    w2h = 0.0;
    biash = 0.0;

    w1y = 0.0;
    w2y = 0.0;
    why = 0.0;
    biasy = 0.0;
    */
}

// Don't modify the follwing code
int main()
{
    int x1, x2;

    setweights();
    while(cin >> x1 >> x2){
        double neth = w1h * x1 + w2h * x2 - biash;
        double outh = neth > 0 ? 1.0 : 0.0;
        double nety = w1y * x1 + w2y * x2 + why * outh - biasy;
        int outy = nety > 0 ? 1 : 0;
        cout << x1 << " XOR " << x2 << " = " << outy << endl;
    }
    return 0;
}