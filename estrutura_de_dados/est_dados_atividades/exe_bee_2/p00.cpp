#include <iostream>
using namespace std;


int main(){

 int vetor[10];

 cin >> vetor[0];
 
    for (int i = 1; i < 10; i++)
    {
        vetor[i]= vetor[i-1]*2;
    }
    
    for(int i =0; i < 10; i++){

        cout << "N[" << i << "] = " << vetor[i] << endl;

    }


    return 0;
}