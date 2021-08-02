import sqlite3

# ------ PESQUISAS POR EMPRÉSTIMOS ------

#pesquisar emprestimos por cadastro do sócio ordem a-z titulo
def codigoLivro1(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Cadastro=?
                ORDER BY Titulo
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por cadastro do sócio ordem z-a titulo
def codigoLivroTit(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Cadastro=?
                ORDER BY Titulo DESC
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por cadastro do sócio ordem data cres
def codigoLivroData(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Cadastro=?
                ORDER BY DataEmprestimo
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
    
#pesquisar emprestimos por cadastro do sócio ordem data decresc
def codigoLivroDataD(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Cadastro=?
                ORDER BY DataEmprestimo DESC
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por nome do sócio ordem a-z titulo
def nomeLivroTitulo(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Nome=?
                ORDER BY Titulo
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por nome do sócio ordem z-a titulo
def nomeLivroTitD(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Cadastro=?
                ORDER BY Titulo DESC
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por nome do sócio ordem data cres
def nomeLivroData(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Nome=?
                ORDER BY DataEmprestimo 
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por nome do sócio ordem data decresc
def momeLivroDataD(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Nome=?
                ORDER BY DataEmprestimo DESC
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por sobrenome do sócio ordem a-z titulo
def sobrenomeLivroTitulo(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Sobrenome=?
                ORDER BY Titulo
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por sobrenome do sócio ordem z-a titulo
def sobrenomeLivroTitD(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Sobrenome=?
                ORDER BY Titulo DESC
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por sobrenome do sócio ordem data cres
def SobrenomeLivroDataE(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Sobrenome=?
                ORDER BY DataEmprestimo
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por sobrenome do sócio ordem data decresc
def SobrenomeLivroDataED(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Sobrenome=?
                ORDER BY DataEmprestimo DESC
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por codigo exemplar ordem a-z nome socio
def codigoLivroNome(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Codigo=?
                ORDER BY Nome
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por codigo exemplar ordem z-a nome socio
def codigoLivroNomeD(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Codigo=?
                ORDER BY Nome DESC
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por codigo exemplar ordem a-z sobrenome socio
def codigoLivro(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Codigo=?
                ORDER BY Sobrenome
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por codigo exemplar ordem z-a sobrenome socio
def codigoLivro(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Codigo=?
                ORDER BY Sobrenome DESC
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por codigo exemplar ordem data cresc
def codigoLivro(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Codigo=?
                ORDER BY DataEmprestimo
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por codigo exemplar ordem data decresc
def codigoLivro(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Codigo=?
                ORDER BY DataEmprestimo DESC
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por titulo livro ordem a-z nome socio
def codigoLivro(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Titulo=?
                ORDER BY Nome
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por titulo livro ordem z-a nome socio
def codigoLivro(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Titulo=?
                ORDER BY Nome DESC
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por titulo livro ordem a-z sobrenome socio
def codigoLivro(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Titulo=?
                ORDER BY Sobrenome
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por titulo livro ordem z-a sobrenome socio
def codigoLivro(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Titulo=?
                ORDER BY Sobrenome DESC
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por titulo livro ordem data cresc
def codigoLivro(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Titulo=?
                ORDER BY DataEmprestimo
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

#pesquisar emprestimos por ctitulo livro ordem data decresc
def codigoLivro(valor):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewEmprestimos
                WHERE Titulo=?
                ORDER BY DataEmprestimo DESC
            """, (valor,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

