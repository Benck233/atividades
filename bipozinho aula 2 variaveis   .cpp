#include <iostream>
using namespace std;


int main() {
    using namespace std;

    //soma
    int a = 10 ;
    int b = 12 ;
    cout<<a+b; cout<<endl;
    
    //subtração
    int c=10,d=12;
    cout<<d-c; cout<<endl;


    
    // int = somente numeros inteiros (somente) 

    int idade = 18 ;
    int ano = 2018 ;
    int dias = 23 ;

    //double = (codigo que inclui os decimais por exemplo(5,5))

    double contabancaria = 230.67 ;
    cout <<"conta bancaria " <<contabancaria ;
    cout <<endl ;
    double preçodoabacate = 10.99;
    cout <<"abacate custa " <<preçodoabacate ;

    //char = mostra somente um caracter


    char nota = '9' ; cout<<endl ;
    cout<<"nota : ";
    cout<< nota ;

    //bolean (verdadeiro ou falso)

    bool estudandante = false;
    bool energia = true;
    bool raçãodegato = false;

    //string (frase ou texto, sem limite(armazena varios char (exemplo: dinossauro (armazenara os char das letras,d,i,n,o,s,s,a,u,r,o) )))))

     string bobber ="boba do rato ja exestiu" ; 
     cout<<bobber; cout<<endl ;
    
   cout<< "sua conta possui " ;cout<<  contabancaria ; cout<<"$";

    /* ou pode se otimizar os "cout" (cout<< "sua conta possui " <<  contabancaria <<"$";) depois do primeiro cout
    podemos retirar os ";" e utilizar somente os "<<" para usando os "cout" */
    

    return 0;
}