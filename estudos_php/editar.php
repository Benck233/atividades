<?php
require("conexao.php");
$id = $_GET['id']; // Pega o ID da URL [6]

$sql = "SELECT * FROM usuarios WHERE id = $id";
$resultado = mysqli_query($conexao, $sql);
$usuario = mysqli_fetch_array($resultado); // Recupera os dados atuais [7, 8]
?>

<form action="processa_edicao.php" method="POST">
    <input type="hidden" name="id" value="<?= $usuario['id'] ?>"> <!-- Campo oculto para o ID [9] -->
    <label>Nome:</label>
    <input type="text" name="nome" value="<?= $usuario['nome'] ?>"><br>
    <label>E-mail:</label>
    <input type="email" name="email" value="<?= $usuario['email'] ?>"><br>
    <button type="submit">Salvar Alterações</button>
</form>