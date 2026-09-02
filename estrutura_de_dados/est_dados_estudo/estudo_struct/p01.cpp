#include <iostream>
#include <string>
using namespace std;

struct Aluno {
    string nome;
    int idade;
    float nota;
};

void mostrarmaiornota(Aluno alunos[], int quantidade);

void mostrarAlunos(Aluno alunos[], int quantidade);

int main() {
    Aluno alunos[4];

    for (int i = 0; i < 4; i++) {
        cout << "Nome do aluno " << i + 1 << ": ";
        cin >> alunos[i].nome;

        cout << "Idade: ";
        cin >> alunos[i].idade;

        cout << "Nota: ";
        cin >> alunos[i].nota;
    }

    mostrarAlunos(alunos, 4);

    mostrarmaiornota(alunos, 4);



    return 0;
}

void mostrarAlunos(Aluno alunos[], int quantidade) {
    cout << "\nAlunos cadastrados:\n";

    for (int i = 0; i < quantidade; i++) {
        cout << "\nNome: " << alunos[i].nome << endl;
        cout << "Idade: " << alunos[i].idade << endl;
        cout << "Nota: " << alunos[i].nota << endl;
    }
}






void mostrarmaiornota(Aluno alunos[], int quantidade){
    cout << "\nAluno com maior nota:\n";
    
    float maior_nota_aluno=0;
    string nome_aluno_com_maior_nota;

    for (int i = 0; i < quantidade; i++)
    {
        
        if (alunos[i].nota>maior_nota_aluno)
        {
            maior_nota_aluno=alunos[i].nota;
            nome_aluno_com_maior_nota=alunos[i].nome;
        }
        

    }

    cout<<nome_aluno_com_maior_nota<<": ";
    cout<<maior_nota_aluno <<endl;

}