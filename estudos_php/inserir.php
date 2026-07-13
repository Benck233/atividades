<?php
require("conexao.php");

// Comando SQL para inserir um produto (exemplo)
$sql = "INSERT INTO produtos (nome,preco) VALUES ('Teclado Mecânico',250.00)";

if (mysqli_query($conexao, $sql)) {
    echo "<br>Produto cadastrado com sucesso!";
} else {
    echo "Erro ao cadastrar: " . mysqli_error($conexao);
}

mysqli_close($conexao);
?>