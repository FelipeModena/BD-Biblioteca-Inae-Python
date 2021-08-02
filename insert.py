import sqlite3

def addMPessoa(many):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.executemany("""INSERT INTO pessoa VALUES (?,?,?,?,?,?,?,?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMSocio(many):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.executemany("""INSERT INTO socio(cpf) VALUES (?)""", (many))
    conn.commit()
    conn.close()

def addMFuncionario(many):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.executemany("""INSERT INTO funcionario VALUES (?,?,?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMLivro(many):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.executemany("""INSERT INTO livro VALUES (?,?,?,?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMExemplar(many):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.executemany("""INSERT INTO exemplar(emprestado, anoPubli, edicao, isbn) VALUES (?,?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMAutor(many):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.executemany("""INSERT INTO autor VALUES (?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMDevolucao(many):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.executemany("""INSERT INTO devolucao(socio, funcionario, codigoExemplar, data, hora) VALUES (?,?,?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMEmprestimo(many):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.executemany("""INSERT INTO emprestimo(socio, funcionario, codigoExemplar, dataE, horaE) VALUES (?,?,?,?,?)""", (many))
    conn.commit()
    conn.close()


livro=[
     ("8585466294", "Fábulas de Esopo", "Fábulas de Esopo", "Companhia das Letrinhas", "Infantil", 0),
            ("8574061557", "Histórias à Brasileira", "Historias à Brasileira", "Companhia das Letrinhas", "Infantil", 0),
            ("8574062197","Arca de Noé, A", "Arca de Noé, A", "Companhia das Letrinhas", "Religioso", 0),
            ("8565484572", "Laços, Turma da Mônica", "Laços, Turma da Mônica", "Panini", "Quadrinhos", 0),
            ("8537809667", "Mágico de Oz, O", "Wizard of Oz, The", "Aventura", "Zahar", 0),
]
#addMLivro(livro)

exemplar=[
    (0, 1999, 1, "8585466294"),
    (0, 1999, 2, "8585466294"),
    (0, 1999, 1, "8585466294"),
    (0, 1999, 3, "8585466294"),
    (0, 1999, 1, "8585466294"),
]
#addMExemplar(exemplar)

autor=[
    ( "Esopo",      "Esopo"     ,"8585466294" ),
    ( "Machado",    "Ana Maria" ,"8574061557" ),
    ( "Moraes, de", "Vinícius"  ,"8574062197" ),
    ( "Cafaggi",    "Lu"        ,"8565484572" ),
    ( "Cafaggi",    "Vítor"     ,"8565484572" ),
    ( "Baum",       "L. Frank"  ,"8537809667" )
]
#addMAutor(autor)

pessoa=[
     ("99999999911","pessoNome1","pessoaSobrenome1","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999912","pessoNome2","pessoaSobrenome2","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999913","pessoNome3","pessoaSobrenome3","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999914","pessoNome4","pessoaSobrenome4","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999915","pessoNome5","pessoaSobrenome5","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999916","pessoNome6","pessoaSobrenome6","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999917","pessoNome7","pessoaSobrenome7","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
     ("99999999918","pessoNome8","pessoaSobrenome8","12-12-2012","rua 1",134,"Valinhos","09340000","9123-1234", "asdas@Sgdfd.com"),
]
#addMPessoa(pessoa)

funcionario=[
    ("1231232",1.32,"bibliotecario","12-12-2012","99999999917"),
    ("1231231",1.211,"almoxarife","12-12-2012","99999999918"),
    ("1234566",1.3333,"faxina","12-12-2012","99999999916"),
]
#addMFuncionario(funcionario)

socio=[
    ("99999999911", ),
    ("99999999912", ),
    ("99999999913", ),
    ("99999999914", ),
]
#addMSocio(socio)
