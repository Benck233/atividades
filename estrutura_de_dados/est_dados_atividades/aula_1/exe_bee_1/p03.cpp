#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    double nota_1=0;
    double nota_2=0;
    double nota_3=0;

    cin>>nota_1;
    cin>>nota_2;
    cin>>nota_3;

    double media = (nota_1*2+nota_2*3+nota_3*5)/10;
    
    cout<<fixed<<setprecision(1);
    cout<<"MEDIA = " <<media<<endl;


    return 0;
}