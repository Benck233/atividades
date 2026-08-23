#include <iostream>

int main()
{
    {
    int contador = 1;

    while (contador <= 5)
    {
        std::cout << contador << "\n";
        contador++;
    }

    }
    
    {
    int contador_2 = 1;

    while (contador_2 <= 10)
    {
        std::cout << contador_2 <<"\n";
        contador_2++;
    }

    }
    
    {
        int contador_3 = 1;
        int resultado;
        std::cout <<"Digite um valor inteiro""\n";
        std::cin >> resultado;
        while (contador_3 <=resultado)
        {
            std::cout<<contador_3 << "\n";
            contador_3++;
        }
        

    }

    
}