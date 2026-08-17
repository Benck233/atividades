#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int codigo=0;
    int quantidade =0;
    double preco=0;
     

    cin>> codigo;
    cin>>quantidade;

    if (codigo ==1)
    {
        preco=4.00;
    }
    else if (codigo ==2)
    {
        preco=4.50;
    }
    else if(codigo ==3){

        preco=5.0;
    }
    else if(codigo ==4){

        preco=2.0;
    }
    else if(codigo ==5){

        preco=1.50;
    }
    double preco_final=preco*quantidade; 
    
    cout<<fixed<<setprecision(2);
    cout<<"Total: R$ "<<preco_final<<endl;



    return 0;
}