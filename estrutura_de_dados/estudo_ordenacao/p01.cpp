//questao da olimpiada de informatica - 2014 Fase 1 Modalidade Universitária (PU) beecrow | 2456
#include <iostream>
using namespace std;


int main(){
int vet[6];

for (int i = 0; i < 5; i++)
{
   do
    {
        cin>>vet[i];
    } while (vet[i] > 13 || vet[i] < 1); 
     
}


bool crescente = true;
bool decresente = true;

for (int  i = 0; i < 4; i++)
{
    if (vet[i] > vet[i +1])
    {
        crescente = false;
    }

    if (vet[i] < vet[i+1])
    {
        decresente = false;
    }
    
}

if (crescente && !decresente)
{
    cout<<"C"<<endl;
}

else if (decresente && !crescente)
{
    cout<<"D"<<endl;
}

else{
    cout<<"N"<<endl;
}




return 0;



}