//SideBar Expandida
document.addEventListener('DOMContentLoaded', () => {
    const trocarBtn = document.querySelector('.trocar-btn');
    const sidebar = document.querySelector('.sidebar');
    const conteudo = document.querySelector('.content');

    trocarBtn.addEventListener('click', () => {
        sidebar.classList.toggle('expanded');
        conteudo.classList.toggle('sidebar-expanded');
    });
});

//Seleção dos botões da Seção Cadastrar
document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.user-type-button');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            
            buttons.forEach(btn => btn.classList.remove('selected'));
            
            button.classList.add('selected');
        });
    });
});

// Recarregar pagina (Nem precisa de explicação)
function recarregarPagina() {
    location.reload();
}


document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('form-modal');
    const alunoCard = document.getElementById('aluno-card');
    const closeModal = document.getElementById('close-modal');

    alunoCard.addEventListener('click', () => {
        modal.classList.add('active');
    });

    closeModal.addEventListener('click', () => {
        modal.classList.remove('active');
    });

    // Adicione mais eventos de clique para os outros cards (professor-card, admin-card)
});
