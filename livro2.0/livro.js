let livros = [
    { 
        titulo: "A Biblioteca da Meia-Noite",
        autor: "Matt Haig",
        editora: "Matt Haig",
        ano: 2020 , 
        sinopse: "conta a história de Nora Seed, uma mulher que se arrepende das escolhas que fez na vida. ",
        paginas: 37 ,
        genero:["romance"],
        preco: 47.00
    },

    { 
        titulo: "Café com deus pai 2025",
        autor: "Junior Rostirola",
        editora: "Velos ",
        ano: 2025, 
        sinopse: " Porções Diárias de Transformação é um livro que propõe uma jornada de devocionais diários ao longo do ano. ",
        paginas: 70 ,
        genero:["religioso"],
        preco: 78.00
    },

    { 
        titulo: "Ainda estou aqui",
        autor: "Walter Salles",
        editora: "Marcelo Rubens Paiva",
        ano: 2024 , 
        sinopse: "No Rio de Janeiro, a família Paiva - Rubens, Eunice e seus cinco filhos - vive à beira da praia em uma casa de portas abertas para os amigos.",
        paginas: 213 ,
        genero:["biografia"],
        preco: 127.00
    },

    { 
        titulo: "Olhos D'Água",
        autor: "Conceição Evaristo",
        editora: "Pallas",
        ano:2014, 
        sinopse: "Em Olhos d’água Conceição Evaristo ajusta o foco de seu interesse na população afro-brasileira abordando, sem meias palavras, a pobreza e a violência urbana que a acometem. ",
        paginas: 116 ,
        genero:["Contos Literatura e Ficção"],
        preco: 120.00
    },

    { 
        titulo: "Canção para ninar menino grande",
        autor: "Conceição Evaristo ",
        editora: "Pallas",
        ano: 2022 , 
        sinopse: "Trata-se de um mosaico afetuoso de experiências negras, um canto amoroso e dolorido. ",
        paginas: 136 ,
        genero:["Ficção Negra e Afro-americana"],
        preco: 100.00
    }
]


function mostraslivros(){
    livros.forEach((livro) => {
    console.log(livro.titulo + " -" +
                livro.autor + "ano:" +
                livro.ano + "paginas:" +
                livro.paginas + "preço:" +
                livro.preco)
    })
}
function criarArquivo(){
    let livrosTexto = JSON.stringify(livros);
    const fs = require('fs');
    fs.writeFileSync("livros.json", livrosTexto);
}
criarArquivo()
mostraslivros();