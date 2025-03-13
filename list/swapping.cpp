#include <iostream>
using namespace std;

int main() {
    int a = 10;
    int b = 20;
    int c;
    
    cout << "Before swapping." << endl;
    cout << "a = " << a << ", b = " << b << endl;

    // c=a;
    // a=b;
    // b=c;

    swap(a,b);

    // a,b=b,a   this is the best way to swap two numbers in python.

    cout << "After swapping." << endl;
    cout << "a = " << a << ", b = " << b << endl;
    return 0;
}