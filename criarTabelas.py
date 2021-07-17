import sqlite3

conn = sqlite3.connect('biblioteca.db')
c = conn.cursor()

c.execute("""PRAGMA foreign_keys = ON;""")

#deleta as tabelas
#c.execute("""DROP TABLE IF EXISTS pessoa""")
#c.execute("""DROP TABLE IF EXISTS socio""")
#c.execute("""DROP TABLE IF EXISTS funcionario""")
#c.execute("""DROP TABLE IF EXISTS fone""")
#c.execute("""DROP TABLE IF EXISTS email""")
#c.execute("""DROP TABLE IF EXISTS livro""")
#c.execute("""DROP TABLE IF EXISTS exemplar""")
#c.execute("""DROP TABLE IF EXISTS autor""")
#c.execute("""DROP TABLE IF EXISTS emprestimo""")
#c.execute("""DROP TABLE IF EXISTS devolucao""")
#c.execute("""DROP TABLE IF EXISTS cataloga""")
#c.execute("""DROP TABLE IF EXISTS cadastra""")
#print('All tables dropped')

#criar as tabelas
c.execute(""" CREATE TABLE IF NOT EXISTS pessoa(
        cpf TEXT UNIQUE NOT NULL PRIMARY KEY,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        dob TEXT NOT NULL,
        rua TEXT NOT NULL,
        numero INTEGER NOT NULL,
        cidade TEXT NOT NULL,
        cep TEXT,
        telefone TEXT,
        email TEXT
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS socio(
        numeroCadastro INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
        cpf TEXT UNIQUE NOT NULL,
        FOREIGN KEY(cpf) REFERENCES pessoa(cpf)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS funcionario(
        cpts TEXT NOT NULL UNIQUE PRIMARY KEY,
        salario FLOAT NOT NULL,
        funcao TEXT NOT NULL,
        dataContrato TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        FOREIGN KEY(cpf) REFERENCES pessoa(cpf)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS livro(
        isbn INTEGER NOT NULL UNIQUE PRIMARY KEY,
        titTrad TEXT NOT NULL,
        titOrig TEXT NOT NULL,
        editora TEXT NOT NULL,
        genero TEXT NOT NULL,
        numeroExemplar INTEGER 
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS exemplar(
        codigoExemplar INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        emprestado INTEGER NOT NULL,
        anoPubli INTEGER NOT NULL,
        edicao INTEGER NOT NULL,
        isbn INTEGER NOT NULL,
        FOREIGN KEY(isbn) REFERENCES livro(isbn)
            ON UPDATE CASCADE
            ON DELETE CASCADE 
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS autor(
        sobrenome TEXT NOT NULL,
        nome TEXT NOT NULL,
        isbn INTEGER NOT NULL,
        PRIMARY KEY(nome, isbn,sobrenome),
        FOREIGN KEY(isbn) REFERENCES livro(isbn)
            ON UPDATE CASCADE
            ON DELETE CASCADE    
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS emprestimo(
        codigoEmprestimo INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        socio INTEGER NOT NULL,
        funcionario TEXT NOT NULL,
        codigoExemplar TEXT NOT NULL,
        dataE TEXT NOT NULL,
        horaE TEXT NOT NULL
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS devolucao(
        codigoDevolucao INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        socio INTEGER NOT NULL,
        funcionario TEXT NOT NULL,
        codigoExemplar INTEGER NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL   
    )""")

#print('All tables created successfully')

conn.commit()
conn.close()