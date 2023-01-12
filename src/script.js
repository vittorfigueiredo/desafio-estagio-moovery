// Variáveis globais
const inputLink = document.querySelector('#inputLink')
const btn = document.querySelector('#urlGenerate')
const links = document.querySelector('.links')
const error = document.querySelector('.error')
const url = document.querySelector('.url')

// Criação global de elemento HTML
const linkUrl = document.createElement('a')

// Consumo da API
function API() {
    const value = inputLink.value
    $.getJSON(`https://is.gd/create.php?format=simple&url=${value}`, {
        url: value,
        format: 'json',
    }).done(function(data) {
        let novoLink = data.shorturl
        linkUrl.innerText = novoLink

        // Verifica se o valor do input estar vazio se sim, continua vazio e nao aparece undefined
        if (value == '') {
            novoLink = ''
        }
    })

    // Evento de click do botão encurtar URL
    btn.addEventListener('click', () => {

        // Tratamento de erro, caso o usuario nao digitar nada no input
        if (!inputLink.value) {
            error.style.display = 'flex'
            return
        }

        error.style.display = 'none'
        links.style.display = 'flex'


        url.appendChild(linkUrl)

        linkUrl.href = inputLink.value
    })

}

// Função deletar todas url e limpar input
function deletar() {
    const btnDelete = document.querySelector('#deletar')
    btnDelete.addEventListener('click', () => {
        let confirmar = confirm('Tem certeza disso?')
            // Verificar se o usuario quer realmente apagar
        if (confirmar == true) {
            links.style.display = 'none'
            linkUrl.innerText = ''
            inputLink.value = ''
        } else {
            return
        }
    })
}

API()
deletar()