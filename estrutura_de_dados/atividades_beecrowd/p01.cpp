#include <iostream>
#include <iomanip>
#include <algorithm>
#include "funcao_tempo.cpp"
#include "ordenar.cpp"
using namespace std;
/*Professor aqui tive um porblema com o compilador, pelo o que eu pesquisei
ao tentar usar como 
int n;
cin>>n;

int numero_atletas[n];

pelas minhas pesquisas isso dependendo do compilador da erro, entao fiz aquela gambiarra com MAX
*/


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
    cout<<"Digite o número de atletas"<<endl;
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
    double soma_tempo_atletas=0;
    
    for (int i = 0; i < numero_atletas; i++)
    {
        cin>>tempo_atletas[i];
        soma_tempo_atletas+=tempo_atletas[i];
        
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
    double melhor_tempo = tempo_atletas[0];
    double pior_tempo = tempo_atletas[0];
    
    for (int i = 1; i < numero_atletas; i++)
    {
        
        if (melhor_tempo>tempo_atletas[i])
        {
          melhor_tempo=tempo_atletas[i];  
        }
        else if (pior_tempo<tempo_atletas[i])
        {
            pior_tempo=tempo_atletas[i];
        }
    }

    double media_tempo=soma_tempo_atletas/numero_atletas;
    
    /*
    cout<<"execelente"<<execelente<<endl;
    cout<<"bom"<<bom<<endl;
    cout<<"melhorar"<<melhorar<<endl;
    cout<<"melhor_tempo"<<melhor_tempo<<endl;
    cout<<"pior_tempo"<<pior_tempo<<endl;
    cout<<"media_tempo"<<media_tempo<<endl;
    */
    sort(tempo_atletas, tempo_atletas + numero_atletas, ordenar);
    /*
    for (int i = 0; i < numero_atletas; i++)
    {
        cout<<tempo_atletas[i]<<endl;
    }
    */
    cout<<"Execelente: "<<execelente<<" atletas"<<endl;
    cout<<"Bom: "<<bom<<" atletas"<<endl;
    cout<<"Precisa Melhorar: "<<melhorar<<" atletas"<<endl;
    cout<<endl;
    cout<<"Melhor tempo: "<<fixed<<setprecision(2)<<melhor_tempo<<"s"<<endl;
    cout<<"Pior tempo: "<<fixed<<setprecision(2)<<pior_tempo<<"s"<<endl;
    cout<<"Tempo médio: "<<fixed<<setprecision(2)<<media_tempo<<"s"<<endl;


    cout<<"Tempos em ordem decrescente: ";
    for (int i = 0; i < numero_atletas; i++)
    {
        if (i > 0)
        {
            cout<<", ";
        }
        cout<<tempo_atletas[i];
    }

    return 0;
}