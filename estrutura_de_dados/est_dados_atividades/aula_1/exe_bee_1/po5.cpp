#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int horas = 0;
    cin>>horas;
    int velocidade=0;
    cin>>velocidade;
    double distancia_percorrida=velocidade*horas;
    double litros_necessario=distancia_percorrida/12;



    cout<<fixed<<setprecision(3);
    cout<<litros_necessario<<endl;


    return 0;
}