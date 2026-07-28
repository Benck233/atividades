//Entrada e saída de dados em c++

#include <iostream>

using namespace std;

int main(){
    int idade;
    float altura;

    cout << "Digite a sua idade: "; //print
    cin  >> idade; //input

    cout << "Digite a sua altura em metros: ";
    cin >> altura;

    cout << "Eu tenho " << idade << " anos"
         << " e " << altura << "m de altura"
         << endl;

    return 0;
}