<?php
// Declaração da função
function calcularDesconto($valorTotal,$porcentagem){
    $desconto = ($valorTotal * $porcentagem)/100;
    $valorFinal = $valorTotal - $desconto;

    return $valorFinal; // Devolve o resultado final
}

// Chamada da função e exibição do resultado

$precoProduto = 100;
$precoComDesconto = calcularDesconto($precoProduto, 15);

echo "O preço original era R$ $precoProduto.<br>";
echo "Com 15% de desconto, fica: R$ $precoComDesconto";