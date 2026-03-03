#include <iostream>
using namespace std;

int main(){
    const double PI = 3.14159; //quando const for usada, o valor nunca muda, ou seja nao é editavel;
    
    double raio /*circunferencia*/ = 10;
    raio = 12;
    double circunferencia = 2 *PI * raio;



    cout<<circunferencia <<"cm";


    const int velocidade_da_luz = 299792458;

    const int Largura = 1920;
    const int Altura = 1080;


    return 0;

}