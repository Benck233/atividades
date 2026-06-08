const btnGerar = document.getElementById("btn-gerar");

btnGerar.addEventListener("click", () => {

    const tamanho = parseInt(document.getElementById("tamanho-senha").value);

    const incluirNumeros = document.getElementById("incluir-numeros").checked;
    const incluirEspeciais = document.getElementById("incluir-especiais").checked;

    let caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    if (incluirNumeros) {
        caracteres += "0123456789";
    }

    if (incluirEspeciais) {
        caracteres += "!@#$%&*()-_=+?";
    }

    let senha = "";

    for (let i = 0; i < tamanho; i++) {
        const indiceAleatorio = Math.floor(Math.random() * caracteres.length);
        senha += caracteres[indiceAleatorio];
    }

    document.getElementById("campo-senha").value = senha;
});