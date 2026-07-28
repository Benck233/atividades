#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    float a,b;
    cin >> a >> b;

    // fixed - Garante o ponto flutuante
    //setprecision(quantidadede casas)
    //setprecision define a precisão
    cout << "O resultado é: "
         << fixed
         << setprecision(3)
         << a/b << endl;

    return 0;
}