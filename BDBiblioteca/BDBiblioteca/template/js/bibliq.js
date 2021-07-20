

$("#form-emprestimo").submit(function (event) {
    event.preventDefault();
    console.log($("#form-emprestimo").serialize());
})
$("#form-pesquisa").submit(function (event) {
    event.preventDefault();
    console.log($("#form-pesquisa").serialize());
})
$("#form-adicionar").submit(function (event) {
    event.preventDefault();
    console.log($("#form-adicionar").serialize());
})
$("#form-cadastro-socio").submit(function (event) {
    event.preventDefault();
    console.log($("#form-cadastro-socio").serialize());
})