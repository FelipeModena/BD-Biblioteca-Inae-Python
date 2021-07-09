from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import modifica
import database
import querys
from datetime import date
from datetime import timedelta

#ABA 1
#done
def Pesquisa():
    try:
        op11=optionVar11.get()
        op12=optionVar12.get()
        text=str(buscarEntry.get())

    except Exception as e:
        messagebox.showwarning("Erro", "Verifique se todos os campos estão preenchidos!")
    else:
        #abre nova janela
        resW = Toplevel()
        resW.title("RESULTADO DA CONSULTA") 
 
        if(op11 == 0 and op12 == 0):
            #nome do autor alf
            rows=querys.ordemAlfAutor(text)
            for row in rows:
                print(row)
            
        elif(op11 == 0 and op12 == 1):
            #nome autor alf invert
            rows=querys.ordemAlfCAutor(text)
            for row in rows:
                print(row)
            
        elif(op11 == 0 and op12 == 2):
            #nome do autor por ano de publi
            pass    

        elif(op11 == 0 and op12 == 3):
            #PESQUISA INVÁLIDA
            pass

        elif(op11 == 1 and op12 == 0):
            #sobrenome ordem alf
            rows=querys.ordemAlfSAutor(text)
            for row in rows:
                print(row)

        elif(op11 == 1 and op12 == 1):
            #sobrenome ordem alf invert
            rows=querys.ordemAlfCSAutor(text)
            for row in rows:
                print(row)

        elif(op11 == 1 and op12 == 2):
            #sobrenome ano de publi
            pass  

        elif(op11 == 1 and op12 == 3):
            #PESQUISA INVÁLIDA
            pass        

        elif(op11 == 2 and op12 == 0):
            #Título ordem alf
            rows=querys.ordemAlfLivro(text)
            for row in rows:
                print(row)

        elif(op11 == 2 and op12 == 1):
            #PESQUISA INVÁLIDA
            pass

        elif(op11 == 2 and op12 == 2):
            #Título ano de publi
            rows=querys.ordemPubliLivro(text)
            for row in rows:
                print(row)
                    
        elif(op11 == 2 and op12 == 3):
            #título edição ordemEdiLivro
            rows=querys.ordemEdiLivro(text)
            for row in rows:
                print(row)
            
        elif(op11 == 3 and op12 == 0):
            #palavra chave a-z
            rows=querys.ordemAlfPC(text)
            for row in rows:
                print(row)
            
        elif(op11 == 3 and op12 == 1):
            #palavra chave z-a
            rows=querys.ordemAlfDPC(text)
            for row in rows:
                print(row)
            
        elif(op11 == 3 and op12 == 2):
            #palavra chave ano publi
            rows=querys.ordemPubliPC(text)
            for row in rows:
                print(row)
                   
        elif(op11 == 3 and op12 == 3):
            #palavra chave edição
            rows=querys.ordemEdicPC(text)
            for row in rows:
                print(row)
                    
        elif(op11 == 4 and op12 == 0):
            #código a-z
            rows=querys.ordemAlfCodigo(int(text))
            for row in rows:
                print(row)

        elif(op11 == 4 and op12 == 1):
            #pesquisa inválida
            pass

        elif(op11 == 4 and op12 == 2):
            #código ano publi
            rows=querys.ordemPubliCodigo(int(text))
            for row in rows:
                print(row)
                    
        elif(op11 == 4 and op12 == 3):
            #código edição 
            rows=querys.ordemEdicCodigo(int(text))
            for row in rows:
                print(row)
        
        elif(op11 == 5 and op12 == 0):
            #Editora a-z
            rows=querys.ordemAlfEditora(text)
            for row in rows:
                print(row)
            
        elif(op11 == 5 and op12 == 1):
            #editora z-a
            rows=querys.ordemAlfDEditora(text)
            for row in rows:
                print(row)
           
        elif(op11 == 5 and op12 == 2):
            #editora ano publi
            rows=querys.ordemPubliEditora(text)
            for row in rows:
                print(row)
                     
        elif(op11 == 5 and op12 == 3):
            #editora por edição
            rows=querys.ordemEdicEditora(text)
            for row in rows:
                print(row)        

#ABA 2
#done
def Emprestimo():
    try:
        funcResp=funcionarioresponsavelEntry.get()
        codLivro=int(codigolivroempresEntry.get())
        Cadastro=int(cpfempresEntry.get())
    except Exception as e:
        messagebox.showwarning("Erro", "Verifique se todos os campos estão preenchidos!")
    else:
        #empréstimo
        modifica.addEmprestimo(funcResp, Cadastro, codLivro)
        #abre nova janela
        dataD=str(date.today()+timedelta(days=7))
        a=querys.nomeLivroporCod(codLivro)
        resW = Toplevel()
        resW.title("EMPRÉSTIMO", "Empréstimo de\t"+a+"\t realizado com sucesso.\t Devolução: "+dataD)
#done
def Busca():
    try:
        op21=optionVar21.get()
        op22=optionVar22.get()
        text=str(buscar2Entry.get())
    except Exception as e:
        messagebox.showwarning("Erro", "Verifique se todos os campos estão preenchidos!")
    else:
        #abre nova janela
        resW = Toplevel()
        resW.title("RESULTADO DA CONSULTA") 
        #n socio a-z
        if(op21==0 and op22==0):
            a=querys.ordemAlfNome(int(text))
            for b in a:
                print(b)

        elif(op21==0 and op22==1):
            #pesquisa invalida
            pass
        
        #n do socio organizar por titulos
        elif(op21==0 and op22==2):
            a=querys.ordemAlfTit(int(text))
            for b in a:
                print(b)

        #n do socio organizar po data de emprestimo
        elif(op21==0 and op22==3):
            a=querys.ordemDEmp(int(text))
            for b in a:
                print(b)

        #n do socio organizar po data de devolução
        elif(op21==0 and op22==4):
            a=querys.ordemDDev(int(text))
            for b in a:
                print(b)

        #nome do socio a-z
        elif(op21==1 and op22==0):
            a=querys.ordemAlfNome(text)
            for b in a:
                print(b) 
       
        #nome do socio z-a
        elif(op21==1 and op22==1):
            a=querys.ordemAlfDNome(text)
            for b in a:
                print(b)
        
        #nome do socio organizar por titulo
        elif(op21==1 and op22==2):
            a=querys.ordemAlfTit(text)
            for b in a:
                print(b)

        #nome do socio organizar por data emprestimo
        elif(op21==1 and op22==3):
            a=querys.ordemDEmp(text)
            for b in a:
                print(b)

        #nome do socio organizar por data devolução
        elif(op21==1 and op22==4):
            a=querys.ordemDDev(text)
            for b in a:
                print(b)
        
        #data empréstimo nome a-z
        elif(op21==2 and op22==0):
            a=querys.ordemAlfNome(text)
            for b in a:
                print(b)
        
        #data empréstimo nome z-a
        elif(op21==2 and op22==1):
            a=querys.ordemAlfDNome(text)
            for b in a:
                print(b)
        
        #data empréstimo organiza por titulo
        elif(op21==2 and op22==2):
            a=querys.ordemAlfTit(text)
            for b in a:
                print(b)

        #data empréstimo organiza por hora
        elif(op21==2 and op22==3):
            #pesquisa inválida
            pass
        
        elif(op21==2 and op22==4):
            #pesquisa inválida
            pass
        
        #data devolução nome a-z
        elif(op21==3 and op22==0):
            a=querys.ordemAlfNome(text)
            for b in a:
                print(b)

        #data devolução nome z-a
        elif(op21==3 and op22==1):
            a=querys.ordemAlfDNome(text)
            for b in a:
                print(b)

        #data devolução título
        elif(op21==3 and op22==2):
            a=querys.ordemAlfTit(text)
            for b in a:
                print(b)
        
        elif(op21==3 and op22==3):
            #pesquisa inválida
            pass
        
        #data devolução organiza por hora
        elif(op21==3 and op22==4):
            #pesquisa inválida
            pass

        #titulo a-z
        elif(op21==4 and op22==0):
            a=querys.ordemAlfTit(text)
            for b in a:
                print(b)

        #titulo z-a
        elif(op21==4 and op22==1):
            a=querys.ordemAlfDTit(text)
            for b in a:
                print(b)
        
        elif(op21==4 and op22==2):
            #pesquisa inválida
            pass
        
        #titulo data de empréstimo
        elif(op21==4 and op22==3):
            a=querys.ordemDEmp(text)
            for b in a:
                print(b)

        #titulo date devolução
        elif(op21==4 and op22==4):
            a=querys.ordemDDev(text)
            for b in a:
                print(b)

        #codigo do livro nomes a-z
        elif(op21==5 and op22==0):
            a=querys.ordemAlfNome(int(text))
            for b in a:
                print(b) 

        #codigo do livro nomes z-a
        elif(op21==5 and op22==1):
            a=querys.ordemAlfDNome(int(text))
            for b in a:
                print(b) 

        elif(op21==5 and op22==2):
            #pesquisa inválida
            pass
        
        #codigo do livro emprestimo
        elif(op21==5 and op22==3):
            a=querys.ordemDEmp(int(text))
            for b in a:
                print(b)

        #codigo do livro devoluçaõ
        elif(op21==5 and op22==4):
            a=querys.ordemDDev(int(text))
            for b in a:
                print(b)

#ABA3
#done
def Cadastro():
    try:
        op=optionVar3.get()
        Nome=str(nomeEntry.get())
        Sobrenome=str(sobrenomeEntry.get())
        CPF=str(cpfEntry.get())
        DOB=str(nascimentoEntry.get())
        tel1=str(telefone1Entry.get())
        tel2=str(telefone2Entry.get())
        email1=str(email1Entry.get())
        email2=str(email2Entry.get())
        Rua=str(ruaEntry.get())
        Numero=int(numeroEntry.get())
        Complemento=str(complementoEntry.get())
        Cidade=str(cidadeEntry.get())
        CEP=str(cepEntry.get())
        CPFF=str(cpffEntry.get())
        CPTS=int(cptsEntry.get())
        Funcao=str(funcaoEntry.get())
        Salario=float(salarioEntry.get())

    except Exception as e:
        #messagebox.showwarning("Erro", "Verifique se todos os campos estão preenchidos!")
        print(e)
    
    else:
        #insere pessoa
        modifica.addPessoa(CPF, Nome, Sobrenome, DOB, Rua, Numero, Cidade, CEP, Complemento)
        #insere e-mail
        modifica.addEmail(CPF, email1)
        if(email2!='none1@none.com'):
            modifica.addEmail(CPF, email2)
        #insere telefone
        modifica.addFone(CPF, tel1)
        if(tel2!='none-none'):
            modifica.addFone(CPF, tel2)

        if(op==0):
            #insere socio
            modifica.addSocio(CPF)
            a=querys.codigoSocio(CPF)
            modifica.addCadastra(CPFF, a)
        elif(op==1):
            #insere funcionário
            modifica.addFuncionario(CPF, CPTS, Salario, Funcao)

#done
def RemoveCadastro():
    try:
        CPF=int(cpfEntry.get())
    except Exception as e:
        messagebox.showwarning("Erro", "Verifique se todos os campos estão preenchidos!")
    else:
        #deleta cadastro
        modifica.deletePessoa(CPF)
#done
def PesquisaDados():
    try:
        op=optionVar3.get()
        Nome=str(nomeEntry.get())
        Sobrenome=str(sobrenomeEntry.get())
        CPF=int(cpfEntry.get())
        Funcao=str(funcaoEntry.get())
    except Exception as e:
        messagebox.showwarning("Erro", "Verifique se todos os campos estão preenchidos!")
    else:
        if(op==0):
            #retorna dados de sócio
            if(Nome!='none'):
                text=Nome
            elif(Sobrenome!='none'):
                text=Sobrenome
            elif(CPF!='none'):
                text=CPF
            querys.pesquisaSocio(text)
        elif(op==1):
            #retorna dados funcionario
            if(Nome!='none'):
                text=Nome
            elif(Sobrenome!='none'):
                text=Sobrenome
            elif(CPF!='none'):
                text=CPF
            elif(Funcao!='none'):
                text=Funcao
            querys.pesquisaFuncionario(text)


#ABA 4
#done
def Catalogo():
    try:
        ISBN=int(isbnEntry.get())
        TituloO=str(titulooriEntry.get())
        TituloT=str(titulotradEntry.get())
        Editora=str(editoracatEntry.get())
        Genero=str(generoEntry.get())
        AnoP=int(anopublicEntry.get())
        Edicao=int(edicaocatEntry.get())
        AutorN1=str(nome1Entry.get())
        AutorN2=str(nome2Entry.get())
        AutorN3=str(nome3Entry.get())
        AutorS1=str(sobrenome1Entry.get())
        AutorS2=str(sobrenome2Entry.get())
        AutorS3=str(sobrenome3Entry.get())
        CPFF=int(cpfFuncEntry.get())
    
    except Exception as e:
        messagebox.showwarning("Erro", "Verifique se todos os campos estão preenchidos!")
    else:
        #adicona livro
        modifica.addLivro(ISBN, TituloT, TituloO, Editora, Genero, AnoP, Edicao)
        a=querys.codigoLivro
        modifica.addCataloga(CPFF, a)
        #adiciona autor
        modifica.addAutor(ISBN, AutorS1, AutorN1)
        if(AutorN2!='none'):
            modifica.addAutor(ISBN, AutorS2, AutorN2)
        if(AutorN3!='none'):
            modifica.addAutor(ISBN, AutorS3, AutorN3)
        #adiciona exemplar
        emp=0
        modifica.addExemplar(ISBN, emp) 
#done
def RemoverExemplar():
    try:    
        ISBN=int(isbnEntry.get())
        Codigo=int(codigoEntry.get())
    except Exception as e:
        messagebox.showwarning("Erro", "Verifique se todos os campos estão preenchidos!")
    else:
        #deleta exemplar com isbn fornecido
        modifica.deleteExemplar(Codigo)
        a=querys.volumes(ISBN)
        if(a==0):
            modifica.deleteLivro(ISBN)
#done
def RemoveLivro():
    try:    
        ISBN=int(isbnEntry)
    except Exception as e:
        messagebox.showwarning("Erro", "Verifique se todos os campos estão preenchidos!")
    else:
        #deleta livro com isbn fornecido
        modifica.deleteLivro(ISBN)

root = Tk()
root.title("Trabalho de Banco de Dados")
root.geometry('850x500')
#abas
tab_control = ttk.Notebook(root)
aba1 = ttk.Frame(tab_control)
aba2 = ttk.Frame(tab_control)
aba3 = ttk.Frame(tab_control)
aba4 = ttk.Frame(tab_control)
aba5 = ttk.Frame(tab_control)
tab_control.add(aba1, text='Consulta')
tab_control.pack(expand=1, fill='both')
tab_control.add(aba2, text='Emprestimo')
tab_control.pack(expand=1, fill='both')
tab_control.add(aba3, text='Cadastro')
tab_control.pack(expand=1, fill='both')
tab_control.add(aba4, text='Catalogar')
tab_control.pack(expand=1, fill='both')

#variaveis
#aba1
optionVar11 = IntVar()
optionVar12 = IntVar()
#aba2
optionVar21 = IntVar()
optionVar22 = IntVar()
#aba3
optionVar3 = IntVar()

# Radio Buttons
#aba1
nomeautorRB = Radiobutton(aba1, text="Nome do Autor", variable=optionVar11, value=0)
sobrenomeautorRB = Radiobutton(aba1, text="Sobrenome do Autor", variable=optionVar11, value=1)
titulotraduzidoRB = Radiobutton(aba1, text="Titulo Traduzido", variable=optionVar11, value=2)
palavrachaveRB = Radiobutton(aba1, text="Palavra Chave", variable=optionVar11, value=3)
codigolivroRB = Radiobutton(aba1, text="Codigo do Livro", variable=optionVar11, value=4)
editoraRb = Radiobutton(aba1, text="Editora", variable=optionVar11, value=5)
ordemalfabeticaRB = Radiobutton(aba1, text="A-Z", variable=optionVar12, value=0)
ordemalfabeticainvRB = Radiobutton(aba1, text="Z-A", variable=optionVar12, value=1)
anodepublicacaoRB = Radiobutton(aba1, text="Ano De Publicacao", variable=optionVar12, value=2)
edicaoRB = Radiobutton(aba1, text="Edicao", variable=optionVar12, value=3)
#aba2
nsocioRB = Radiobutton(aba2, text="Numero do socio", variable=optionVar21, value=0)
nomsocioRB = Radiobutton(aba2, text="Nome do socio", variable=optionVar21, value=1)
dataemprestRB = Radiobutton(aba2, text="Data de Emprestimo", variable=optionVar21, value=2)
datadevRB = Radiobutton(aba2, text="Data de Devolucao", variable=optionVar21, value=3)
titRB = Radiobutton(aba2, text="Titulo", variable=optionVar21, value=4)
codlivRB = Radiobutton(aba2, text="Codigo do Livro", variable=optionVar21, value=5)
azRB = Radiobutton(aba2, text="A-Z", variable=optionVar22, value=0)
zaRB = Radiobutton(aba2, text="Z-A", variable=optionVar22, value=1)
tituRB = Radiobutton(aba2, text="Titulo", variable=optionVar22, value=2)
datadeemprestRB = Radiobutton(aba2, text="Data de Emprestimo", variable=optionVar22, value=3)
datadedevRB = Radiobutton(aba2, text="Data de Devolucao", variable=optionVar22, value=4)
#aba3
socioRB = Radiobutton(aba3, text="Socio", variable=optionVar3, value=0)
funcionarioRB = Radiobutton(aba3, text="Funcionario", variable=optionVar3, value=1)

# Entradas
#aba1
buscarEntry = Entry(aba1, width=30)
buscarEntry.insert(0, 'none')
#aba2
cpfempresEntry = Entry(aba2, width=12)
cpfempresEntry.insert(0, 1111)
funcionarioresponsavelEntry = Entry(aba2, width=20)
funcionarioresponsavelEntry.insert(0, 1111)
codigolivroempresEntry = Entry(aba2, width=12)
codigolivroempresEntry.insert(0, 111)
buscar2Entry = Entry(aba2, width=20)
buscar2Entry.insert(0, 'none')
#aba3
nomeEntry = Entry(aba3, width=20)
nomeEntry.insert(0, 'none')
sobrenomeEntry = Entry(aba3, width=30)
sobrenomeEntry.insert(0, 'none')
cpfEntry = Entry(aba3, width=12)
cpfEntry.insert(0, "none")
nascimentoEntry = Entry(aba3, width=10)
nascimentoEntry.insert(0, 'none')
telefone1Entry = Entry(aba3, width=11)
telefone1Entry.insert(0, 'none-none')
telefone2Entry = Entry(aba3, width=11)
telefone2Entry.insert(0, 'none-none')
email1Entry = Entry(aba3, width=50)
email1Entry.insert(0, 'none@none.com')
email2Entry = Entry(aba3, width=50)
email2Entry.insert(0, 'none1@none.com')
ruaEntry = Entry(aba3, width=50)
ruaEntry.insert(0, 'none')
numeroEntry = Entry(aba3, width=6)
numeroEntry.insert(0, 1)
complementoEntry = Entry(aba3, width=10)
complementoEntry.insert(0, 'none')
cidadeEntry = Entry(aba3, width=20)
cidadeEntry.insert(0, 'none')
cepEntry = Entry(aba3, width=10)
cepEntry.insert(0, 'none')
cptsEntry = Entry(aba3, width=10)
cptsEntry.insert(0, 11111111)
funcaoEntry = Entry(aba3, width=10)
funcaoEntry.insert(0, 'none')
salarioEntry = Entry(aba3, width=10)
salarioEntry.insert(0, 11.11)
cpffEntry=Entry(aba3, width=12)
cpffEntry.insert(0, 'none')

#aba4
isbnEntry = Entry(aba4, width=20)
isbnEntry.insert(0, 111111111)
titulooriEntry = Entry(aba4, width=40)
titulooriEntry.insert(0, 'none')
titulotradEntry = Entry(aba4, width=40)
titulotradEntry.insert(0, 'none')
editoracatEntry = Entry(aba4, width=20)
editoracatEntry.insert(0, 'none')
generoEntry = Entry(aba4, width=15)
generoEntry.insert(0, 'none')
anopublicEntry = Entry(aba4, width=5)
anopublicEntry.insert(0, 1111)
edicaocatEntry = Entry(aba4, width=5)
edicaocatEntry.insert(0, 1)
nome1Entry = Entry(aba4, width=20)
nome1Entry.insert(0, 'none')
nome2Entry = Entry(aba4, width=20)
nome2Entry.insert(0, 'none')
nome3Entry = Entry(aba4, width=20)
nome3Entry.insert(0, 'none')
sobrenome1Entry = Entry(aba4, width=20)
sobrenome1Entry.insert(0, 'none')
sobrenome2Entry = Entry(aba4, width=20)
sobrenome2Entry.insert(0, 'none')
sobrenome3Entry = Entry(aba4, width=20)
sobrenome3Entry.insert(0, 'none')
codigoEntry = Entry(aba4, width=20)
codigoEntry.insert(0, 1111)
cpfFuncEntry=Entry(aba4, width=12)
cpfFuncEntry.insert(0, 'none')

# Botoes
#aba1
pesquisar = Button(aba1, text="Pesquisar", command=Pesquisa).grid(row=12, column=3)
#aba2
finalizar = Button(aba2, text="Finalizar", command=Emprestimo).grid(row=5, column=3)
buscar = Button(aba2, text="Pesquisar", command=Busca).grid(row=18, column=3)
#aba3
cadastrar = Button(aba3, text="Cadastrar", command=Cadastro).grid(row=26, column=2, sticky=E+W)
removerC = Button(aba3, text="Remover Cadastro", command=RemoveCadastro).grid(row=27, column=2, sticky=E+W)
pesquisaC = Button(aba3, text="Pesquisar", command=PesquisaDados).grid(row=28, column=2, sticky=E+W)
#aba4
catalogar = Button(aba4, text="Catalogar", command=Catalogo).grid(row=12, column=2, sticky=E+W)
removerE = Button(aba4, text="Deletar exemplar", command=RemoverExemplar).grid(row=13, column=2, sticky=E+W)
removerL = Button(aba4, text="Remover todos", command=RemoveLivro).grid(row=14, column=2, sticky=E+W)


#-----------------------------------------------------------------
# Inserções na tela
# Labels
#aba1
pesquisaLabel = Label(aba1, text='Pesquisar por:').grid(row=1, column=1, sticky=W)
mostraLabel = Label(aba1, text='Mostrar por:').grid(row=7, column=1, sticky=W)
buscaLabel = Label(aba1, text='Buscar:').grid(row=12, column=1, sticky=W)
#aba2
espacoLabel2 = Label(aba2, text=' ').grid(row=1, column=1, sticky=E)
cpfempresLabel = Label(aba2, text='CPF').grid(row=2, column=1, sticky=E)
funcionarioresponsavelLabel = Label(aba2, text='Funcionario Responsavel').grid(row=3, column=1, sticky=E)
codigolivroempresLabel = Label(aba2, text='Codigo do Livro').grid(row=4, column=1, sticky=E)
pesquisarporLabel = Label(aba2, text='Pesquisar por:').grid(row=7, column=1, sticky=E)
ordenarLabel = Label(aba2, text='Ordenar por:').grid(row=13, column=1, sticky=E)
buscar2Label = Label(aba2, text='Buscar').grid(row=18, column=1, sticky=E)
espacoLabel = Label(aba2, text=' ').grid(row=6, column=1, sticky=E)
#aba3
nomeLabel = Label(aba3, text="Nome").grid(row=3, column=1, sticky=E)
sobrenomeLabel = Label(aba3, text="Sobrenome ").grid(row=5, column=1, sticky=E)
cpfLabel = Label(aba3, text='CPF').grid(row=7, column=1, sticky=E)
nascimentoLabel = Label(aba3, text='Data de Nascimento').grid(row=7, column=3, sticky=W)
telefoneLabel = Label(aba3, text='Telefone').grid(row=11, column=1, sticky=E)
emailLabel = Label(aba3, text='Email').grid(row=13, column=1, sticky=E)
ruaLabel = Label(aba3, text='Rua').grid(row=17, column=1, sticky=E)
numeroLabel = Label(aba3, text='Numero').grid(row=17, column=3, sticky=W)
complementoLabel = Label(aba3, text='Complemento').grid(row=17, column=3, sticky=E)
cidadeLabel = Label(aba3, text='Cidade').grid(row=19, column=1, sticky=E)
cepLabel = Label(aba3, text='CEP').grid(row=21, column=1, sticky=E)
cptsLabel = Label(aba3, text='CPTS').grid(row=22, column=1, sticky=E)
funcaoLabel = Label(aba3, text='Funcao').grid(row=23, column=1, sticky=E)
salarioLabel = Label(aba3, text='Salario').grid(row=24, column=1, sticky=E)
cpffLabel = Label(aba3, text="Funcionário responsável:").grid(row = 25, column=1, sticky=E)

#aba4
isbnLabel = Label(aba4, text="ISBN").grid(row=6, column=1, sticky=E)
titulooriLabel = Label(aba4, text="Titulo Original").grid(row=1, column=1, sticky=E)
titulotradLabel = Label(aba4, text="Titulo Traduzido").grid(row=2, column=1, sticky=E)
editoracatLabel = Label(aba4, text="Editora").grid(row=7, column=1, sticky=E)
generoLabel = Label(aba4, text="Genero").grid(row=10, column=1, sticky=E)
anopublicLabel = Label(aba4, text="Ano de Publicacao").grid(row=8, column=1, sticky=E)
edicaocatLabel = Label(aba4, text="Edicao").grid(row=9, column=1, sticky=E)
nome1Label = Label(aba4, text="Nome do Autor").grid(row=3, column=1, sticky=E)
nome2Label = Label(aba4, text="Nome do Autor").grid(row=4, column=1, sticky=E)
nome3Label = Label(aba4, text="Nome do Autor").grid(row=5, column=1, sticky=E)
sobrenome1Label = Label(aba4, text="Sobrenome do Autor").grid(row=3, column=3, sticky=E)
sobrenome2Label = Label(aba4, text="Sobrenome do Autor").grid(row=4, column=3, sticky=E)
sobrenome3Label = Label(aba4, text="Sobrenome do Autor").grid(row=5, column=3, sticky=E)
codigoLabel = Label(aba4, text="Código").grid(row=6, column= 3, sticky=E)
cpfFuncLabel = Label(aba4, text="Funcionário responsável:").grid(row = 11, column=1, sticky=E)

# Entrys
#aba1
buscarEntry.grid(row=12, column=2, sticky=W + E)
#aba2
cpfempresEntry.grid(row=2, column=2, sticky=W + E)
funcionarioresponsavelEntry.grid(row=3, column=2, sticky=W + E)
codigolivroempresEntry.grid(row=4, column=2, sticky=W + E)
buscar2Entry.grid(row=18, column=2, sticky=W + E)
#aba3
nomeEntry.grid(row=3, column=2, sticky=W + E)
sobrenomeEntry.grid(row=5, column=2, sticky=W + E)
cpfEntry.grid(row=7, column=2, sticky=W + E)
nascimentoEntry.grid(row=7, column=3)
telefone1Entry.grid(row=11, column=2, sticky=W)
telefone2Entry.grid(row=11, column=2)
email1Entry.grid(row=13, column=2)
email2Entry.grid(row=13, column=3)
ruaEntry.grid(row=17, column=2)
numeroEntry.grid(row=17, column=3)
complementoEntry.grid(row=17, column=4, sticky=W)
cidadeEntry.grid(row=19, column=2, sticky=W)
cepEntry.grid(row=21, column=2, sticky=W)
cptsEntry.grid(row=22, column=2, sticky=W)
funcaoEntry.grid(row=23, column=2, sticky=W)
salarioEntry.grid(row=24, column=2, sticky=W)
cpffEntry.grid(row=25, column=2, sticky=W)

#aba4
isbnEntry.grid(row=6, column=2, sticky=W)
titulooriEntry.grid(row=1, column=2, sticky=W)
titulotradEntry.grid(row=2, column=2, sticky=W)
editoracatEntry.grid(row=7, column=2, sticky=W)
generoEntry.grid(row=10, column=2, sticky=W)
anopublicEntry.grid(row=8, column=2, sticky=W)
edicaocatEntry.grid(row=9, column=2, sticky=W)
nome1Entry.grid(row=3, column=2, sticky=W)
nome2Entry.grid(row=4, column=2, sticky=W)
nome3Entry.grid(row=5, column=2, sticky=W)
sobrenome1Entry.grid(row=3, column=4, sticky=W)
sobrenome2Entry.grid(row=4, column=4, sticky=W)
sobrenome3Entry.grid(row=5, column=4, sticky=W)
codigoEntry.grid(row=6, column = 4, sticky =W)
cpfFuncEntry.grid(row=11, column=2, sticky=W)

#RadioButton
#aba1
nomeautorRB.grid(row=1, column=2, sticky=W)
sobrenomeautorRB.grid(row=2, column=2, sticky=W)
titulotraduzidoRB.grid(row=3, column=2, sticky=W)
palavrachaveRB.grid(row=4, column=2, sticky=W)
codigolivroRB.grid(row=5, column=2, sticky=W)
editoraRb.grid(row=6, column=2, sticky=W)
ordemalfabeticaRB.grid(row=7, column=2, sticky=W)
ordemalfabeticainvRB.grid(row=8, column=2, sticky=W)
anodepublicacaoRB.grid(row=9, column=2, sticky=W)
edicaoRB.grid(row=10, column=2, sticky=W)
#aba2
nsocioRB.grid(row=7, column=2, sticky=W)
nomsocioRB.grid(row=8, column=2, sticky=W)
dataemprestRB.grid(row=9, column=2, sticky=W)
datadevRB.grid(row=10, column=2, sticky=W)
titRB.grid(row=11, column=2, sticky=W)
codlivRB.grid(row=12, column=2, sticky=W)
azRB.grid(row=13, column=2, sticky=W)
zaRB.grid(row=14, column=2, sticky=W)
tituRB.grid(row=15, column=2, sticky=W)
datadeemprestRB.grid(row=16, column=2, sticky=W)
datadedevRB.grid(row=17, column=2, sticky=W)
#aba3
socioRB.grid(row=1, column=2, sticky=W)
funcionarioRB.grid(row=1, column=2, sticky=E)


optionVar11=IntVar()
optionVar12=IntVar()
optionVar3=IntVar()
optionVar2=IntVar()
optionVar21=IntVar()
optionVar22=IntVar()

root.mainloop()