<?php

ob_start(); // Inicia captura de saída
require("conexao.php"); // Importa sua conexão da etapa anterior
ob_clean(); // Descarta a mensagem de conexão sem exibir

// Recebendo os dados do formulário via $_POST

$nome = $_POST['txtNome'];
$email = $_POST['txtEmail'];
$senha =$_POST['txtSenha'];

// Segurança: Criptografando a senha antes de salvar
$senhaSegura =password_hash($senha, PASSWORD_DEFAULT);

// Comando SQL (Certifique-se que a tabela 'usuarios' existe com esses campos)
$sql = "INSERT INTO usuarios (nome, email, senha) VALUES ('$nome', '$email', '$senhaSegura')";

if(mysqli_query($conexao,$sql)){
    echo"Usuário cadastrado com sucesso! 🛡️";
}else{
    echo "Erro: " . mysqli_close($conexao);
}

mysqli_close($conexao);

?>