<?php

require("conexao.php"); // Importa a conexão estabelecida anteriormente

// 1. Criar a consulta SQL para buscar todos os usuários

$sql = "SELECT id, nome, email FROM usuarios ORDER BY nome";

// 2. Executar a consulta

$resultado = mysqli_query($conexao, $sql);

// 3. Verificar se existem registros

if (mysqli_num_rows($resultado) > 0) {
    print "<h2>Lista de Usuários</h2>";
    echo "<table border='1'>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>E-mail</th>
            </tr>";
    
    // 4. Usar um laço (while) para percorrer cada linha do resultado
    while ($usuario = mysqli_fetch_array($resultado)) {
        echo "<tr>";
        echo "<td>" . $usuario['id'] . "</td>";
        echo "<td>" . $usuario['nome'] . "</td>";
        echo "<td>" . $usuario['email'] . "</td>";
        echo "</tr>";
    }
    echo "</table>";
} 

else {
    echo "Nenhum usuário encontrado. ❌"; 
}

  // 5. Fechar a conexão 
  mysqli_close($conexao);
?>
