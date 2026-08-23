#include <iostream>
#include <string>

int main()

{
    {
    int idade =30;
    double altura = 1.80;
    char sexo = 'M';
    bool programador = true;
    std::string nome = "Guilherme";



    std::cout <<"Nome: " << nome << "\n";
    std::cout << "Idade: " << idade << "\n";
    std::cout << "Altura: " << altura << "\n";
    std::cout << "Sexo: " << sexo << "\n";
    std::cout << "Programador: " << programador << "\n";
    }

    {
    std::string produto = "Notebook";
    double preco = 4500.90;
    int quantidade =8;
    bool disponivel = true;

    std::cout<<"Produto: " << produto <<"\n";
    std::cout<<"Preco: " << preco <<"\n";
    std::cout<<"Quantidade: " << quantidade <<"\n";
    std::cout<<"Disponivel: " << disponivel <<"\n";
    }

    return 0;


}