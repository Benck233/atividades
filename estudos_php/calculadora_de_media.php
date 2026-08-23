<?php

$nota_1= 8.5;
$nota_2=6.0;
$media= ($nota_1+$nota_2)/2; // Parênteses garantem que a soma ocorra antes da divisão [13]

echo "Media: $media <br>"; 


if ($media >= 7){
print"Status: Aprovado";
}

elseif ($media >= 5 && $media <7){
    echo"Status: Recuperação. Estude mais";
}

else{
    print"Reprovado";
}

?>