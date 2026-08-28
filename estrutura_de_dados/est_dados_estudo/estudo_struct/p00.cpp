#include <iostream>
#include <string>
using namespace std;

struct Aluno
{
    string nome;
    int idade;
    float nota;
};

void varios_aluno(){

    Aluno alunos[4]={{"Bobber", 20, 10},
    {"Ana", 19, 8.5},
    {"Joao", 21, 7},
    {"Maria", 18, 9}};

    int quantidade_alunos = 4;

    for (int i = 0; i <quantidade_alunos ; i++)
    {
        cout<<alunos[i].nome<<" ";
        cout<<alunos[i].idade<<" ";
        cout<<alunos[i].nota<<endl;
    }
    

}

int main(){
    /*
    Aluno aluno;

    aluno.nome = "Bobber";
    aluno.idade = 20;
    aluno.nota = 10;

    cout<<aluno.nome<<endl;
    cout<<aluno.idade<<endl;
    cout<<aluno.nota<<endl;
    
    */
    varios_aluno();

    return 0;
}
