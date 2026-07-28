#include <iostream>

using namespace std;

int main(){
    string nome;
    cout << "Digite o seu nome: ";
    // Lê somente até o espaço em branco
    //cin >> nome;
    //Obtem toda a linha, 
    //incluindo espaços em branco
    getline(cin,nome); 

    cout << "Meu nome é: " << nome;
    return 0;
}