
const dtToggleBtn = document.getElementById('dark-mode-toggle');


if (dtToggleBtn) {
    dtToggleBtn.addEventListener('click', () => {
        
        document.body.classList.toggle('dark-mode');
        
        
        if (document.body.classList.contains('dark-mode')) {
            dtToggleBtn.textContent = "☀️ Modo Claro";
        } else {
            dtToggleBtn.textContent = "🌙 Modo Noturno";
        }
    });
}


let currentFontSize = 100; 
const btnAumentar = document.getElementById('btn-aumentar');
const btnDiminuir = document.getElementById('btn-diminuir');

if (btnAumentar && btnDiminuir) {
    btnAumentar.addEventListener('click', () => {
        currentFontSize += 10; 
        document.body.style.fontSize = currentFontSize + '%';
    });

    btnDiminuir.addEventListener('click', () => {
        if (currentFontSize > 70) { 
            currentFontSize -= 10;
            document.body.style.fontSize = currentFontSize + '%';
        }
    });
}


const formContato = document.getElementById('form-contato');

if (formContato) {
    formContato.addEventListener('submit', function(event) {
        
        const nome = document.getElementById('nome').value.trim();
        const email = document.getElementById('email').value.trim();
        const mensagem = document.getElementById('mensagem').value.trim();
        
        
        if (nome === "" || email === "" || mensagem === "") {
            alert("Por favor, preencha todos os campos obrigatórios.");
            event.preventDefault();
        } else {
            alert("Obrigado, " + nome + "! A sua mensagem foi enviada com sucesso.");
        }
    });
}