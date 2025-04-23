let livros = require("./livros.json")
function mostralivros(){
    livros.forEach((livro) => {
        console.log(livro.titulo + " - " + 
            livro.autor + "\nAno: " + 
            livro.ano + "\nPáginas: " +
            livro.paginas + "\nPreço: R$ " +
            livro.preco +
            "\n"
        )
    })
}


function adicionaLivro(titulo, autor, editora, ano, sinopse, paginas, genero, preco){
        livros.push({
            título: titulo,
            autor: autor,
            editora: editora,
            ano: ano,
            sinopse: sinopse,
            paginas: paginas,
            genero: genero,
            preco: preco,

        });
        console.log("Livro adicionado com sucesso!");
}


adicionaLivro("Meu diario", "Hayssa Kroin", "HayHay",  2016,
 " Meu diario é um livro que conta do meu dia", "fantasia", 47);

// JSON = javaScript object notation
// GERA UM ARQUIVO JSON DOS LIVROS 
function criarArquivo(){
    let livrotexto = JSON.stringify(livros);
    const fs = require('fs');
    fs.writeFileSync("livros.json",livrotexto);
}

//criarArquivo()
mostraslivros();