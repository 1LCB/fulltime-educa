// SideBar Expandida
var TEACHERS_LIST;

function list_teachers() {
    console.log(TEACHERS_LIST)
}

document.addEventListener('DOMContentLoaded', () => {
    const trocarBtn = document.querySelector('.trocar-btn');
    const sidebar = document.querySelector('.sidebar');
    const conteudo = document.querySelector('.content');

    trocarBtn.addEventListener('click', () => {
        sidebar.classList.toggle('expanded');
        conteudo.classList.toggle('sidebar-expanded');
    });

    // Fazendo a requisição para o endpoint
    const accessToken = sessionStorage.getItem('access_token'); // Obtendo o access_token do sessionStorage
    
    fetch('http://localhost:8090/api/teacher', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${accessToken}`, // Incluindo o access_token no cabeçalho
            'Content-Type': 'application/json' // Definindo o tipo de conteúdo como JSON
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json(); // Convertendo a resposta para JSON
    })
    .then(data => {
        console.log(data); // Printando os dados recebidos
        const secao2 = document.querySelector('.secao2'); // Selecionando o container "secao2"

        // Limpa o conteúdo existente, se necessário
        secao2.innerHTML = ''; // Opcional: limpa antes de adicionar novos elementos

        // Iterando sobre o array de objetos recebido

        TEACHERS_LIST = data; //TEACHERS LIST #############################################

        data.forEach(teacher => {
            const cardiTotal = document.createElement('div');
            cardiTotal.classList.add('cardi-total');

            const cardi = document.createElement('div');
            cardi.classList.add('cardi');

            const imagemArea = document.createElement('div');
            imagemArea.classList.add('imagem-area');
            // Aqui você pode adicionar a imagem se a URL estiver disponível
            if (teacher.image_path) {
                imagemArea.style.backgroundImage = `url(http://localhost:8090/api/teacher/picture/${teacher.image_path})`; // Define a imagem de fundo
            }

            const infos = document.createElement('div');
            infos.classList.add('infos');

            const h1 = document.createElement('h1');
            h1.textContent = teacher.name; // Nome do professor

            const h2 = document.createElement('h2');
            h2.textContent = teacher.email; // E-mail do professor

            infos.appendChild(h1);
            infos.appendChild(h2);
            cardi.appendChild(imagemArea);
            cardi.appendChild(infos);
            cardiTotal.appendChild(cardi);

            const cardiBtns = document.createElement('div');
            cardiBtns.classList.add('cardi-btns');

            const editarBtn = document.createElement('button');
            editarBtn.classList.add('editar-btn');
            const editarIcon = document.createElement('img');
            editarIcon.src = 'img/icons/editar_icon.svg'; // Caminho para o ícone de editar
            editarIcon.alt = 'icone de editar';
            editarBtn.appendChild(editarIcon);

            const deletarBtn = document.createElement('button');
            deletarBtn.classList.add('deletar-btn');
            const deletarIcon = document.createElement('img');
            deletarIcon.src = 'img/icons/deletar_icon.svg'; // Caminho para o ícone de deletar
            deletarIcon.alt = 'icone de deletar';
            deletarBtn.appendChild(deletarIcon);

            cardiBtns.appendChild(editarBtn);
            cardiBtns.appendChild(deletarBtn);
            cardiTotal.appendChild(cardiBtns);
            secao2.appendChild(cardiTotal); // Adiciona o "cardi-total" à seção
        });
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
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

window.addEventListener("load", () => {
    const cards = document.getElementsByClassName("cardi-total")
    const secao2 = document.querySelector(".secao2")

    if (cards.length >= 3) {
        secao2.style.flexWrap = "wrap";
        console.log("wrap")
    } else {
        secao2.style.flexWrap = "nowrap";
        console.log("nowrap")
    }
})