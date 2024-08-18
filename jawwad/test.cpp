#include <iostream>
using namespace std;

int main(){
    int n, a = 0, multiplier = 1;
    cout << "Enter the number: ";
    cin >> n;
    while(n > 0){
        a += (n % 2) * multiplier;
        multiplier *= 10;
        n /= 2;
    }
    cout << "Binary: " << a << endl;
    return 0;
}