#include <iostream>
#include <algorithm>
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
    int n;
    cin>>n;
    int numero_atletas= n;
    int tempo_atletas[n];
    
    for (int i = 0; i < n; i++)
    {
        cin>>tempo_atletas[i];
    }
    
    
    


    return 0;
}