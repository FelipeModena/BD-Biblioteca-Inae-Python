import datetime
from PyQt5 import uic, QtWidgets
import insert
from datetime import date, datetime
import queryLivro

#----------------------- FUNÇÕES DE CADA PÁGINA DA INTERFACE ----------------------------
#Página de cadastro de pessoas
def salvarPessoas():
    nome=tela.InsertNome.text()
    sobrenome=tela.InsertSobrenome.text()
    cpf=tela.InsertCPF.text()
    rua=tela.InsertRua.text()
    dataNascimento=tela.InsertNascimento.text()
    numero=tela.InsertNumero.text()
    cidade=tela.InsertCidade.text()
    cep=tela.InsertCEP.text()
    telefone=tela.InsertTelefone.text()
    email=tela.InsertEmail.text()
    cpts=tela.InsertCPTS.text()
    salario=tela.InsertSalario.text()
    funcao=tela.InsertFuncao.text()
    funcionario=False
    socio=False
    data=date.today().strftime("%d/%m/%Y")
    pessoa=[(cpf, nome, sobrenome, dataNascimento, rua, numero, cidade, cep, telefone, email)]
    sociol=[(cpf,),]
    funcionariol=[(cpts, salario, funcao, data, cpf)]
    if(tela.Socio_2.isChecked()):
        socio=True
    elif(tela.Funcionario.isChecked()):
        funcionario=True
    if(nome=="" or sobrenome=="" or cpf=="" or rua=="" or dataNascimento=="" or numero=="" or cidade=="" or cep=="" or telefone=="" or email==""):
        print("Informações obrigatórias não foram preenchidas.")
    if(socio):
        insert.addMPessoa(pessoa)
        insert.addMSocio(sociol)
        print("Sócio cadastrado com sucesso!")
    elif(funcionario):
        if(funcao=='' or salario=='' or cpts==''):
            print("Informações obrigatórias não foram preenchidas.")
        else:
            insert.addMPessoa(pessoa)
            insert.addMFuncionario(funcionariol)
            print("Funcionário cadastrado com sucesso")
    elif(not(socio) and not(funcionario)):
        print("É necessário selecionar se deseja inserir um sócio ou um funcionário.")
    tela.InsertNome.clear()
    tela.InsertSobrenome.clear()
    tela.InsertCPF.clear()
    tela.InsertRua.clear()
    tela.InsertNascimento.clear()
    tela.InsertNumero.clear()
    tela.InsertCidade.clear()
    tela.InsertCEP.clear()
    tela.InsertTelefone.clear()
    tela.InsertEmail.clear()
    tela.InsertCPTS.clear()
    tela.InsertSalario.clear()
    tela.InsertFuncao.clear()

#Página de cadastro de livros
def salvarLivros():
    ano=tela.InsertAnoPublicacao.text()
    tituloTraduzido=tela.InsertTituloTraduzido.text()
    genero=tela.InsertGenero.text()
    tituloOriginal=tela.InsertTituloOriginal.text()
    editora=tela.InsertEditora.text()
    isbn=tela.InsertISBN.text()
    edicao=tela.InsertEdicao.text()
    sobrenome1=tela.InsertSobrenomeAutor1.text()
    nome1=tela.InsertNomeAutor1.text()
    sobrenome2=tela.InsertSobrenomeAutor2.text()
    nome2=tela.InsertNomeAutor2.text()
    sobrenome3=tela.InsertSobrenomeAutor3.text()
    nome3=tela.InsertNomeAutor3.text()
    autor1=False
    autor2=False
    autor3=False
    livro=[(isbn, tituloTraduzido, tituloOriginal, editora, genero, 0)]
    exemplar=[(0, ano, edicao, isbn)]
    autor=[()]
    exists=False
    rows=queryLivro.livroExiste(isbn)

    if(len(rows) > 0):
        exists=True

    if(tela.radioButton.isChecked()):
        autor1=True
    elif(tela.radioButton_2.isChecked()):
        autor2=True
    elif(tela.radioButton_3.isChecked()):
        autor3=True

    if(autor1):
        autor=[(sobrenome1, nome1, isbn)]
    elif(autor2):
        autor=[(sobrenome1, nome1, isbn), (sobrenome2, nome2, isbn)]
    elif(autor3):
        autor=[(sobrenome1, nome1, isbn),(sobrenome2, nome2, isbn),(sobrenome3, nome3, isbn)]

    if(ano=="" or tituloTraduzido=="" or genero=="" or tituloOriginal=="" or editora=="" or isbn=="" or edicao==""):
        print("Informações necessárias não foram fornecidas.")
    elif(not(autor1) and not(autor2) and not(autor3)):
        print("Informe quantos autores deseja inserir.")
    elif(not exists):
        insert.addMLivro(livro)
        insert.addMExemplar(exemplar)
        insert.addMAutor(autor)
        print("Livro, exemplar e autor inseridos com sucesso!")
    elif(exists):
        insert.addMExemplar(exemplar)
        print("Exemplar adicionado com sucesso")
    
    ano=tela.InsertAnoPublicacao.clear()
    tituloTraduzido=tela.InsertTituloTraduzido.clear()
    genero=tela.InsertGenero.clear()
    tituloOriginal=tela.InsertTituloOriginal.clear()
    editora=tela.InsertEditora.clear()
    isbn=tela.InsertISBN.clear()
    edicao=tela.InsertEdicao.clear()
    sobrenome1=tela.InsertSobrenomeAutor1.clear()
    nome1=tela.InsertNomeAutor1.clear()
    sobrenome2=tela.InsertSobrenomeAutor2.clear()
    nome2=tela.InsertNomeAutor2.clear()
    sobrenome3=tela.InsertSobrenomeAutor3.clear()
    nome3=tela.InsertNomeAutor3.clear()

#Página de empréstimos e devoluções
def emprestar():
    codigoExemplar=tela.InsertCodigoExemplar.text()
    socio=tela.InsertSocio.text()
    funcionario=tela.InsertFuncionario.text()
    data=date.today().strftime("%d/%m/%Y")
    hora=datetime.now().strftime("%H:%M:%S")
    emprestimo = [(socio, funcionario, codigoExemplar, data, hora)]

    if(codigoExemplar==" " or socio==" " or funcionario==" "):
        print("Informações necessárias não foram fornecidas.")
    else:
        insert.addMEmprestimo(emprestimo)
        print("Emprestimo realizado com sucesso.")
    codigoExemplar=tela.InsertCodigoExemplar.clear()
    socio=tela.InsertSocio.clear()
    funcionario=tela.InsertFuncionario.crear()

def devolver():
    codigoExemplar=tela.InsertCodigoExemplar.text()
    socio=tela.InsertSocio.text()
    funcionario=tela.InsertFuncionario.text()
    data=date.today().strftime("%d/%m/%Y")
    hora=datetime.now().strftime("%H:%M:%S")
    devolucao = [(socio, funcionario, codigoExemplar, data, hora)]

    if(codigoExemplar==" " or socio==" " or funcionario==" "):
        print("Informações necessárias não foram fornecidas.")
    else:
        insert.addMDevolucao(devolucao)
        print("Devolução realizada com sucesso.")
    codigoExemplar=tela.InsertCodigoExemplar.clear()
    socio=tela.InsertSocio.clear()
    funcionario=tela.InsertFuncionario.crear()

#Página de pesquisa de catálogo
def pesquisarCatalogo():
    pesquisa=tela.InsertPesquisa.text()
    tipo=str(tela.SelecionaPesquisarPor.currentText())
    ordem=str(tela.SelecionaOrdenarPor.currentText())
    
    resposta=[]

    if(tipo=="Título"):
        if(ordem=="A-Z"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Z-A"):
            resposta=queryLivro.ordemAlfDLivro(pesquisa)

        elif(ordem=="Ano de Publicação"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Edição"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

    elif(tipo=="Nome Autor"):
        if(ordem=="A-Z"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Z-A"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Ano de Publicação"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Edição"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

    elif(tipo=="Sobrenome Autor"):
        if(ordem=="A-Z"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Z-A"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Ano de Publicação"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Edição"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

    elif(tipo=="Editora"):
        if(ordem=="A-Z"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Z-A"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Ano de Publicação"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Edição"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

    elif(tipo=="Palavra Chave"):
        if(ordem=="A-Z"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Z-A"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Ano de Publicação"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

        elif(ordem=="Edição"):
            resposta=queryLivro.ordemAlfLivro(pesquisa)

    respostaLivros.show()
    respostaLivros.tableWidget.setRowCount(len(resposta))
    respostaLivros.tableWidget.setColumnCount(8)
    
    for i in range(0, len(resposta)):
        for j in range (0, 8):
            respostaLivros.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(resposta[i][j])))



#Página de pesquisa de pessoas
def pesquisarPessoas():
    print("pesquisar pessoas")



app=QtWidgets.QApplication([])
tela= uic.loadUi('BDBiblioteca.ui')
respostaLivros=uic.loadUi('resposta_livros.ui')


tela.CadastrarPessoa.clicked.connect(salvarPessoas)
tela.CadastraLivro.clicked.connect(salvarLivros)
tela.Emprestar.clicked.connect(emprestar)
tela.Devolver.clicked.connect(devolver)
tela.PesquisarCatalogo.clicked.connect(pesquisarCatalogo)
tela.PesquisaPessoas.clicked.connect(pesquisarPessoas)


tela.show()
app.exec()