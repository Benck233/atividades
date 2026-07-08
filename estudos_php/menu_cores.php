<?php

$cor_favorita ="vermelho";

switch ($cor_favorita) {

    case "vermelho":
        echo "Você escolheu a cor da paixão.";
        break; // O break é essencial para o PHP parar de ler os próximos casos [17, 18]


    case "azul":
        echo "Você escolheu a cor do céu.";
        break;
    
    default:
        echo "Cor não identificada";

    
}

?>