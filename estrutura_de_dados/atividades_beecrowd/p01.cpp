#include <iostream>
#include <algorithm>
#include "funcao_tempo.cpp"
using namespace std;



//talvez usa assim
/*int main(){
    cout<<"digite uma entrada"<<endl;
    const int MAX =1000;
    int n;
    cin>>n;
    int numero_atletas= n;
    int tempo_atletas[MAX];

    if(n > MAX){
        cout<<"Quantidade invalida";
        retunr 1;
    }
    
    for (int i = 0; i < n; i++)
    {
        cin>>tempo_atletas[i];
    }
    
    
    


    return 0;
}*/

int main(){
    cout<<"digite uma entrada"<<endl;
    int numero_atletas;
    cin>>numero_atletas;
    const int MAX =1000;
    
    if(numero_atletas > MAX){
        cout<<"Quantidade invalida";
        return EXIT_FAILURE;
    }

    double tempo_atletas[MAX];
    int execelente=0;
    int bom=0;
    int melhorar=0;
    
    for (int i = 0; i < numero_atletas; i++)
    {
        cin>>tempo_atletas[i];
        
        int resultado = testar_tempo_atleta(tempo_atletas[i]);

        if (resultado == 1)
        {
            execelente++;
        }
        
        else if (resultado ==2)
        {
            bom++;
        }
        
        else if (resultado ==3)
        {
            melhorar++;
        }
        

    }
    
    cout<<execelente<<endl;
    cout<<bom<<endl;
    cout<<melhorar<<endl;
    
    
    
    


    return 0;
}