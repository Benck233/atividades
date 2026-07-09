<?php

$alunos = array("João", "Maria", "José", "Ana");

// Exemplo com FOR: usamos count() para saber o tamanho do array

echo "<strong>Lista de Alunos (usando for):</strong><br>";

for ($i =0; $i < count($alunos);$i++){
    echo"Índice $i: " . $alunos[$i] . "<br>";
}

echo"<br>";

$frutas = array(
    "Abacaxi",
    "Melancia",
    "Maracujá",
    "Morango",
    "Banana",
    "Abacate",
    "Carambola",
    "Kiwi",
    "Pitaya",
    "Manga"
);

echo "<strong>Lista de frutas (usando for):</strong><br>";

for($i = 0; $i<count($frutas);$i++){
    if ($frutas[$i] == "Abacate"){
        print"A fruta escolhida foi: $frutas[$i]";

    }
}

echo "<br> <br>";

// Exemplo com FOREACH: muito mais limpo para arrays

echo "<strong>Lista de Alunos (usando foreach):</strong><br>";
foreach ($alunos as $nome){
    echo "Nome: $nome <br>";
}

echo "<br>";

// Exemplo de Array Associativo
$perfil = array(
    "nome" =>"Alexandre",
    "idade" =>24,
    "cidade"=>"São Paulo"
);

foreach ($perfil as $chave => $valor){
    echo ucfirst($chave) .":$valor <br>";
}


echo "<br><br>";

$contador = 0;

while($contador <11){
    echo $contador . "<br>";

    $contador++;
}


echo "<br><br>";

?>