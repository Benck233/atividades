#include <iostream>

int main()
{
    int a = 10;
    int b = 3;

    std::cout << "Soma: " << a + b << "\n";
    std::cout << "Subtração: " << a - b << "\n";
    std::cout << "Multiplicação: " << a * b << "\n";
    std::cout << "Divisão: " << a / b << "\n";
    std::cout << "Resto: " << a % b << "\n";

    std::cout << (a > b) << "\n";
    std::cout << (a == b) << "\n";

    return 0;
}

