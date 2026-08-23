<?php
// Definindo as credenciais
$host =  "localhost";
$usuario = "root";
$senha = "";
$banco = "estudo_php";

// Criando a conexão usando a biblioteca mysqli

$conexao = mysqli_connect($host, $usuario, $senha, $banco);

// Verificando se houve erro

if(!$conexao){
    die("Falha na conexão: " . mysqli_connect_error());
}

echo "Conectado com sucesso! ✅";
?>