#include <iostream>

int main()
{
    int idade;

    std::cout << "Digite sua idade: ";
    std::cin >> idade;

    if (idade >= 18)
    {
        std::cout << "Maior de idade\n";
    }
    else
    {
        std::cout << "Menor de idade\n";
    }

    return 0;
}