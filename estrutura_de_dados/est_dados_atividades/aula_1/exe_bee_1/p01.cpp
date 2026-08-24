#include <stdio.h>
#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int contador_in = 0;
    int contador_out = 0;

    

    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;

        if (x >=10 && x <=20)
        {
            contador_in+=1;
        }

        else{

            contador_out+=1;
        }
        



    }

    cout <<contador_in<< " in"<< endl;
    cout <<contador_out<< " out"<<endl;
    
    return 0;
}