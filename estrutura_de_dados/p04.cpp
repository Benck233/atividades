// exemplo de if e else -
#include <iostream>

using namespace std;

int main(){
    int n;
    cout << "Informe um número inteiro: ";
    cin >> n;

    //n > 10 AND n <20
    if(n >= 10 && n < 20){
        cout << "Ok!" << endl;
        
    }
    else{
        cout << "Não!" << endl;
    }

    return 0;
}