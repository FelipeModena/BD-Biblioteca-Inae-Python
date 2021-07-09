import sqlite3
import database

#Colocar em todas as funções:
'''conn = sqlite3.connect('biblioteca.db')
c = conn.cursor()
conn.commit()
conn.close()'''

#adicionar nas tabelas

def addPessoa(cpf, nome, sobrenome, dob, rua, numero, cidade, cep, complemento):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""INSERT INTO pessoa VALUES (?,?,?,?,?,?,?,?,?)
                ON CONFLICT(cpf) DO NOTHING;
            """, (cpf, nome, sobrenome, dob, rua, numero, cidade, cep, complemento, ))
    conn.commit()
    conn.close()

def addSocio(cpf):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""INSERT INTO socio VALUES (?)""", (cpf,))
    conn.commit()
    conn.close()

def addFuncionario(cpf, cpts, salario, funcao):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""INSERT INTO funcionario VALUES (?,?,?,?,DATE('now'))""", (cpf, cpts, salario, funcao))
    conn.commit()
    conn.close()

def addFone(cpf, fone):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""INSERT INTO fone 
                VALUES (?,?);
            """, (fone, cpf))
    conn.commit()
    conn.close()

def addEmail(cpf, email):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""INSERT INTO email VALUES (?,?)  
            """, (email, cpf, ))
    conn.commit()
    conn.close()

def addLivro(isbn, titTrad, titOrig, editora, genero, anoPubli, edicao):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""INSERT INTO livro VALUES (?,?,?,?,?,?,?,)
                ON CONFLICT(isbn) DO UPDATE SET exemplares=exemplares+1;""", (isbn, titTrad, titOrig, editora, genero, anoPubli, edicao))
    conn.commit()
    conn.close()

def addExemplar(isbn, emp):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""INSERT INTO exemplar VALUES (?,?,)""", (isbn, emp))
    conn.commit()
    conn.close()

def addAutor(isbn, sobrenome, nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""INSERT INTO autor VALUES (?,?,?,)
                ON CONFLICT(isbn) DO NOTHING;
            """, (isbn, sobrenome, nome))
    conn.commit()
    conn.close()

def addEmprestimo(cpfFunc, cadastro, locPrat):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""INSERT INTO emprestimo VALUES (?,?,?,DATE('now'),DATETIME('now','localtime'),DATE('now', '+7 days'))""", (cpfFunc, cadastro, locPrat,))
    conn.commit()
    conn.close()

def addDevolucao(cpfFunc, cpfSocio, isbn, locPrat):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""INSERT INTO devolucao VALUES (?,?,?,DATE('now'),DATETIME('now','localtime'),)""", (cpfFunc, cpfSocio, locPrat))
    conn.commit()
    conn.close()
    
def addCataloga(cpfFunc, locPrat):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""INSERT INTO cataloga VALUES (?,?,DATE('now'),DATETIME('now','localtime'),)""", (locPrat, cpfFunc))
    conn.commit()
    conn.close()

def addCadastra(cpfFunc, cadastro):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""INSERT INTO acdastra VALUES (?,?,DATE('now'),DATETIME('now','localtime'),)""", (cadastro, cpfFunc,))
    conn.commit()
    conn.close()


#deleta da tabela

def deleteExemplar(locPrat):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""DELETE FROM exemplar WHERE locPrat=(?)""", (locPrat, ))
    conn.commit()
    conn.close()
    
def deleteLivro(isbn):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""DELETE FROM livro WHERE isbn=(?)""", (isbn, ))
    conn.commit()
    conn.close()

def deletePessoa(cpf):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""DELETE FROM pessoa WHERE cpf=(?)""", (cpf, ))
    conn.commit()
    conn.close()



