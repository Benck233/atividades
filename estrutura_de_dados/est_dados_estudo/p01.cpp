#include <iostream>
#include "funcoes_celcius.cpp"
#include "funcoes_Fahrenheit.cpp"
using namespace std;

int main(){
    float celcius;
    float fahrenheit;
    char escolha;
    cout <<"Escolha entre Celcius e Fahrenheit (C/F)"<<endl;
    cin >> escolha;
    escolha =toupper(escolha);

    if (escolha == 'C')
    {
        cout<<"Digite a temperatura em Celsius: "<<endl;
        cin >> celcius;
        float resultado;
        resultado = conversor_celcius(celcius);
        cout<<"O valor de Celsius para Fahrenheit é: "<<resultado<<endl;
    }

    else if (escolha == 'F')
    {
        cout<<"Digite a temperatura em Fahrenheit: "<<endl;
        cin >> fahrenheit;
        float resultado;
        resultado = conversor_fahrenheit(fahrenheit);
        cout<<"O valor de Fahrenheit para Celcius é: "<<resultado<<endl;
    }
}