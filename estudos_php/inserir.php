<?php
require("conexao.php"); // Reutiliza o código de conexão que acabamos de criar

// Comando SQL para inserir um produto (exemplo)
$sql = "INSERT INTO produtos (nome,preco) VALUES ('Teclado Mecânico',250.00)";


// Comando SQL para inserir um produto (exemplo)
if (mysqli_query($conexao,$sql)){
    echo "<br>Produto cadastrado com sucesso!";
}
else{
    echo "Erro ao cadastrar: " . mysqli_error($conexao);
}

// Fecha a conexão após o uso
mysqli_close($conexao);
?>