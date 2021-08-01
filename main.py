from PyQt5 import uic, QtWidgets
import insert
from datetime import date

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
    print("Salva livros")

#Página de empréstimos e devoluções
def emprestar():
    print("emprestado")


def devolver():
    print("devolvido")

#Página de pesquisa de catálogo
def pesquisarCatalogo():
    print("pesquisar catálogo")

#Página de pesquisa de pessoas
def pesquisarPessoas():
    print("pesquisar pessoas")



app=QtWidgets.QApplication([])
tela= uic.loadUi('BDBiblioteca.ui')

tela.CadastrarPessoa.clicked.connect(salvarPessoas)
tela.CadastraLivro.clicked.connect(salvarLivros)
tela.Emprestar.clicked.connect(emprestar)
tela.Devolver.clicked.connect(devolver)
tela.PesquisarCatalogo.clicked.connect(pesquisarCatalogo)
tela.PesquisaPessoas.clicked.connect(pesquisarPessoas)


tela.show()
app.exec()