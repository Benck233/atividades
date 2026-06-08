let tamanhoFonte = 16;

document.getElementById("btn-acessibilidade").addEventListener("click", () => {
    tamanhoFonte += 2;

    if (tamanhoFonte > 24) {
        tamanhoFonte = 16;
    }

    document.body.style.fontSize = tamanhoFonte + "px";
});