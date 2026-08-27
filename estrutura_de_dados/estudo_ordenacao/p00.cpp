#include <iostream>
using namespace std;

template <typename T>
void bubblesort(T vet[], int n){
bool troca;

do
{
    troca = false;
    for (int i = 0; i < n - 1; i++)
    {
        if (vet[i] >vet[i+1])
        {
            swap(vet[i], vet[i+1]);
            troca=true;
            
        }
        
    }


} while (troca);

    



}



int main(){
    cout<<"Digite 3 valores: "<<endl;
    int vet[3];
    int vet_antigo[3];

    
    for(int i = 0; i < 3; i++){
        cin >> vet[i];
    }
    
    for (int i = 0; i < 3; i++)
    {
        vet_antigo[i] = vet[i];
    }
    

    bubblesort(vet, 3);

    for (int i = 0; i < 3; i++)
    {
        cout <<vet[i]<<endl;
    }
    
    cout<<endl;

    for (int i = 0; i < 3; i++)
    {
        cout <<vet_antigo[i]<<endl;
    }
    


    return 0;    
}