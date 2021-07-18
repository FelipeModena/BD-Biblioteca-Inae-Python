import sqlite3

# ------ ORDENAR EXEMPLAR ------

#por estado de empréstimo
def ordemEmprestado(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE ISBN=?
                ORDER BY Emprestado;
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
print(ordemEmprestado("8585466294"))

#por ano de publicação
def ordemPubliAno(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE ISBN=?
                ORDER BY Publicacao;
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemPubliAno("8585466294"))

#por edição
def ordemEdiLivro(titulo):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE ISBN=?
                ORDER BY Edicao
            """, (titulo, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemEdiLivro("8585466294"))

#livro por código
def ordemAlfCodigo(cod):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewExemplar
                WHERE Codigo=?
            """, (cod, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfCodigo(1))

#por editora
def ordemEditora(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewLivro
                WHERE ISBN=?
                ORDER BY Editora
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemEditora("8585466294"))
