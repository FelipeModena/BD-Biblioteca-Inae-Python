import sqlite3

#deleta da tabela

def deleteExemplar(codigo):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""DELETE FROM exemplar WHERE codigoExemplar=(?)""", (int(codigo[0][0]), ))
    conn.commit()
    conn.close()
    
def deleteLivro(isbn):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""DELETE FROM livro WHERE isbn=(?)""", (int(isbn[0][0]), ))
    conn.commit()
    conn.close()

def deletePessoa(cpf):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""DELETE FROM pessoa WHERE cpf=(?)""", (int(cpf[0][0]), ))
    conn.commit()
    conn.close()

# deleteExemplar(1)
# deleteLivro("8585466294")
#deletePessoa("99999999917")