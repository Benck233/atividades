#include <iostream>
#include <string>
using namespace std;

namespace um {

        int x = 1;


}

namespace dois {

    int x =2;


}

namespace cpf{

    string Laura_grando = "040.861.000.02" ;

    }

 
int main(){
//"namespaces" servem para diferenciar nomes
    
    int x = 0;
    cout<<"tempo para a bomba explodir" <<endl;
    cout<< x <<" " <<endl <<um::x <<endl <<dois::x; 
    cout<<endl;
    cout<<"Seu cpf " <<cpf::Laura_grando;

    return 0;

} 