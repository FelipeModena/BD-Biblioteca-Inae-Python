import sqlite3

# ------ PESQUISAS POR EMPRÉSTIMOS ------

#pesquisar emprestimos por cadastro do sócio ordem a-z titulo
def cadastroLivroTitulo(valor):
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

#pesquisar emprestimos por codigo z-a titulo
def codigoCadastroTit(valor):
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