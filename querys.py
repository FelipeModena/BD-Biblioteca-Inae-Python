import sqlite3

#querys 
#ABA 1 - pesquisa por livros
#nome autor a-z
def ordemAlfAutor(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Nome=?
                ORDER BY Título
            """, (nome, ))
   
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return rows

#nome autor z-a
def ordemAlfCAutor(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Nome=?
                ORDER BY Título DESC;
            """, (nome, ))
   
    rows = c.fetchall()
  #  for row in rows:
   #     print(row)

    conn.commit()
    conn.close()
    return rows

#nome por ano de publicação
def ordemPubliAutor(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Nome=?
                ORDER BY anoPubli;
            """, (nome, ))
   
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return rows

#sobrenome autor a-z
def ordemAlfSAutor(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Sobrenome=?
                ORDER BY Título;
            """, (nome, ))
   
    rows = c.fetchall()
   # for row in rows:
    #    print(row)

    conn.commit()
    conn.close()
    return rows

#sobrenome autor z-a
def ordemAlfCSAutor(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Sobrenome=?
                ORDER BY Título DESC;
            """, (nome, ))
   
    rows = c.fetchall()
   # for row in rows:
    #    print(row)

    conn.commit()
    conn.close()
    return rows

#sobrenome por ano de publicação
def ordemPubliSAutor(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Sobrenome=?
                ORDER BY anoPubli;
            """, (nome, ))
   
    rows = c.fetchall()
   # for row in rows:
    #    print(row)

    conn.commit()
    conn.close()
    return rows

#título ordem alfabética
def ordemAlfLivro(titulo):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Título LIKE ? 
                ORDER BY Título;
            """, (titulo, ))
   
    rows = c.fetchall()
   # for row in rows:
    #    print(row)

    conn.commit()
    conn.close()
    return rows

#título por ano de publicação
def ordemPubliLivro(titulo):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Título LIKE ? 
                ORDER BY anoPubli;
            """, (titulo, ))
   
    rows = c.fetchall()
   # for row in rows:
    #    print(row)

    conn.commit()
    conn.close()
    return rows

#título por edição
def ordemEdiLivro(titulo):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Título LIKE ? 
                ORDER BY Edição;
            """, (titulo, ))
   
    rows = c.fetchall()
   # for row in rows:
    #    print(row)

    conn.commit()
    conn.close()
    return rows

#palavra chave a-z
def ordemAlfPC(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Título LIKE ? OR Nome LIKE ? OR Sobrenome LIKE ? OR Editora LIKE ? 
                ORDER BY Título;
            """, (text, text, text, text, ))
   
    rows = c.fetchall()
   # for row in rows:
    #    print(row)

    conn.commit()
    conn.close()
    return rows

#palavra chave z-a
def ordemAlfDPC(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Título LIKE ? OR Nome LIKE ? OR Sobrenome LIKE ? OR Editora LIKE ? 
                ORDER BY Título DESC;
            """, (text, text, text, text, ))
   
    rows = c.fetchall()
   # for row in rows:
    #    print(row)

    conn.commit()
    conn.close()
    return rows

#palavra chave ano publi
def ordemPubliPC(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Título LIKE ? OR Nome LIKE ? OR Sobrenome LIKE ? OR Editora LIKE ? 
                ORDER BY anoPubli;
            """, (text, text, text, text, ))
   
    rows = c.fetchall()
   # for row in rows:
    #    print(row)

    conn.commit()
    conn.close()
    return rows

#palavra chave edição
def ordemEdicPC(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Título LIKE ? OR Nome LIKE ? OR Sobrenome LIKE ? OR Editora LIKE ? 
                ORDER BY Edição;
            """, (text, text, text, text, ))
   
    rows = c.fetchall()
   # for row in rows:
    #    print(row)

    conn.commit()
    conn.close()
    return rows

#livro por código (a-z)
def ordemAlfCodigo(cod):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Código=?
                ORDER BY Título;
            """, (cod, ))
   
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return rows

#livro por código ano de publicação
def ordemPubliCodigo(cod):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Código=?
                ORDER BY anoPubli;
            """, (cod, ))
   
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return rows

#livro por código edição
def ordemEdicCodigo(cod):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Código=?
                ORDER BY Edição;
            """, (cod, ))
   
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return rows

#editora a-z
def ordemAlfEditora(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Editora=?
                ORDER BY Título;
            """, (nome, ))
   
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return rows

#editora z-a
def ordemAlfDEditora(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Editora=?
                ORDER BY Título DESC;
            """, (nome, ))
   
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return rows

#editora ano de publicação
def ordemPubliEditora(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Editora=?
                ORDER BY anoPubli;
            """, (nome, ))
   
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return rows

#editora edição
def ordemEdicEditora(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE Editora=?
                ORDER BY Edição;
            """, (nome, ))
   
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return rows

#sócio n cadastro(a-z)
def ordemAlfNumCadastro(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM socio
                WHERE numeroCadastro
                INNER JOIN emprestimo ON emprestimo.cpfSocio=socio.cpf;    
                ORDER BY nome;    
            """, (nome, ))
    rows = c.fetchall()
    #for row in rows:
    #    print(row)
    conn.commit()
    conn.close()
    return rows

#sócio nome a-z
def ordemAlfNomeCadastro(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM socio
                WHERE nome=? OR sobrenome=?
                INNER JOIN emprestimo ON emprestimo.cpfSocio=socio.cpf;    
                ORDER BY cpf;    
            """, (nome, nome, ))
    rows = c.fetchall()
    #for row in rows:
    #    print(row)
    conn.commit()
    conn.close()
    return rows

#sócio nome z-a
def ordemAlfDNomeCadastro(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM socio
                WHERE nome=? OR sobrenome=?
                INNER JOIN emprestimo ON emprestimo.cpfSocio=socio.cpf;   
                ORDER BY cpf DESC;     
            """, (nome, nome, ))
    rows = c.fetchall()
    #for row in rows:
     #   print(row)
    conn.commit()
    conn.close()
    return rows

#ABA 2 - empréstimo e pesquisa por empréstimos 
#nome do livro pelo código
def nomeLivroporCod(titulo):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT isbn FROM exemplar
                WHERE locPrat=?    
            """, (titulo, ))
    a=c.fetchone()[0]
    c.execute("""SELECT titTrad FROM livro
                WHERE isbn=?
    """, (a,))
    rows = c.fetchone()[0]
    #for row in rows:
     #   print(row)
    conn.commit()
    conn.close()
    return rows
 
def dataEmprestimo(data):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM emprestimo
                WHERE dataE=? 
                INNER JOIN socio ON socio.cpf=emprestimo.cpfSocio;   
                INNER JOIN funcinario ON funcionario.cpf=emprestimo.cpfSocio;     
            """, (data,))
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()

def dataDevolucao(data):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM devolucao
                WHERE data=? 
                INNER JOIN socio ON socio.cpf=devolucao.cpfSocio;   
                INNER JOIN funcinario ON funcionario.cpf=devolucao.cpfSocio;     
            """, (data, ))
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()

def livrosEmprestados(cpf):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM emprestimo
                WHERE cpfSocio=? 
                INNER JOIN socio ON socio.cpf=emprestimo.cpfSocio; 
                ORDER BY dataE    
            """, (cpf, ))
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()

def ordemAlfNome(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimo
                WHERE Cadastro=? OR Nome=? OR Sobrenome=? OR Título=? OR Código=? OR DataEmpréstimo=? OR DataDevolução=? 
                ORDER BY Nome   
            """, (text, text, text, text, text, text, text))
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()

def ordemAlfDNome(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimo
                WHERE Cadastro=? OR Nome=? OR Sobrenome=? OR Título=? OR Código=? OR DataEmpréstimo=? OR DataDevolução=? 
                ORDER BY Nome DESC
            """, (text, text, text, text, text, text, text))
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()

def ordemAlfTit(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimo
                WHERE Cadastro=? OR Nome=? OR Sobrenome=? OR Título=? OR Código=? OR DataEmpréstimo=? OR DataDevolução=? 
                ORDER BY Nome Título
            """, (text, text, text, text, text, text, text))
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()

def ordemAlfDTit(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimo
                WHERE Cadastro=? OR Nome=? OR Sobrenome=? OR Título=? OR Código=? OR DataEmpréstimo=? OR DataDevolução=? 
                ORDER BY Nome Título DESC
            """, (text, text, text, text, text, text, text))
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()

def ordemDEmp(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimo
                WHERE Cadastro=? OR Nome=? OR Sobrenome=? OR Título=? OR Código=? OR DataEmpréstimo=? OR DataDevolução=? 
                ORDER BY Nome DataEmpréstimo
            """, (text, text, text, text, text, text, text))
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()

def ordemDDev(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimo
                WHERE Cadastro=? OR Nome=? OR Sobrenome=? OR Título=? OR Código=? OR DataEmpréstimo=? OR DataDevolução=? 
                ORDER BY Nome DataDevolução
            """, (text, text, text, text, text, text, text))
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()


#devolve volumes
def volumes(isbn):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT volumes FROM livro
                WHERE isbn=?
            """, (isbn,))
    rows = c.fetchone()[0]
    conn.commit()
    conn.close()
    return rows

#devolve codigo socio
def codigoSocio(cpf):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT numeroCadastro FROM socio
                WHERE cpf=?
            """, (cpf,))
    rows = c.fetchone()
    conn.commit()
    conn.close()
    return rows

#devolve codigo livro
def codigoLivro(isbn):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT locPrat FROM exemplar
                WHERE isbn=?
                LIMIT 1;
            """, (isbn,))
    rows = c.fetchone()[0]
    conn.commit()
    conn.close()
    return rows

def pesquisaSocio(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewSocio
                WHERE Cadastro=? OR CPF=? OR Nome=? OR Sobrenome=?
            """, (text, text, text, text ))
    a=c.fetchone()[0]
    c.execute("""SELECT titTrad FROM livro
                WHERE isbn=?
    """, (a,))
    rows = c.fetchall()
    #for row in rows:
     #   print(row)
    conn.commit()
    conn.close()
    return rows

def pesquisaFuncionario(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewFuncionario
                WHERE CPF=? OR Nome=? OR Sobrenome=?
            """, (text, text, text, ))
    rows = c.fetchall()
    #for row in rows:
     #   print(row)
    conn.commit()
    conn.close()
    return rows
