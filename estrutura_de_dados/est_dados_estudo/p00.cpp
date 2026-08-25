#include <iostream>
#include "funcoes.cpp"
#include <cassert>
using namespace std;



int main(){
int primo;
cout<<"Digite um numero primo: "<<endl;
cin >> primo;

bool resultado = testador_primo(primo);

assert(resultado == true);


}