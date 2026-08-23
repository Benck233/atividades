<?php
// Criando um array indexado de frutas
$frutas = array("Maça","Banana","Morango");

// Adicionando um item ao final do array automaticamente

$frutas[] = "Laranja";

// Exibindo um valor específico (lembre-se: começa do 0)

echo "A segunda fruta é:" .$frutas[1]."<br>";// Exibirá Banana

// Função útil para ver o conteúdo completo de um array (ótimo para testes)
print_r($frutas);