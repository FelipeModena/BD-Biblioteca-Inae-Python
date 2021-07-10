import sqlite3
import database

def addMPessoa(many):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.executemany("""INSERT INTO pessoa VALUES (?,?,?,?,?,?,?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMSocio():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    many=[("076.728.597-22"),
            ("214.755.103-14"),
            ("420.272.234-52")]
    c.executemany("""INSERT INTO socio VALUES (?,)""", (many))
    conn.commit()
    conn.close()

def addMFuncionario(many):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.executemany("""INSERT INTO funcionario VALUES (?,?,?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMFone():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    many=[("825.029.244-80", "(61) 3524-3325"),
            ("084.313.437-29", "(81) 2608-9355"),
            ("311.572.890-53", "(82) 3597-2148"),
            ("076.728.597-22", "(79) 3611-1671"),
            ("214.755.103-14", "(55) 3921-9146"),
            ("420.272.234-52", "(68) 3631-2439")]
    c.executemany("""INSERT INTO fone VALUES (?,)""", (many))
    conn.commit()
    conn.close()

def addMEmail():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    many=[("825.029.244-80", "claudiogui@graficajardim.com.br"),
            ("084.313.437-29", "thiagovitorcarvalho__@advocaciand.adv.br"),
            ("311.572.890-53", "luizacaroline@rubens.adm.br"),
            ("076.728.597-22", "victor-97@vieiradarocha.adv.br"),
            ("214.755.103-14", "soniacarolinadarocha_@murosterrae.com.br"),
            ("420.272.234-52", "laviniasdamata@land.com.br")]
    c.executemany("""INSERT INTO email VALUES (?,)""", (many))
    conn.commit()
    conn.close()

def addMLivro():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    many=[("8585466294", "Fábulas de Esopo", "Fábulas de Esopo", "Companhia das Letrinhas", "Infantil", 1994, 12, 1),
            ("8574061557", "Histórias à Brasileira", "Historias à Brasileira", "Companhia das Letrinhas", "Infantil", 2004, 2, 1),
            ("8574062197","Arca de Noé, A", "Arca de Noé, A", "Companhia das Letrinhas", "Religioso", 2004, 2, 1),
            ("8565484572", "Laços, Turma da Mônica", "Laços, Turma da Mônica", "Panini", "Quadrinhos", 2014, 1, 1),
            ("8537809667", "Mágico de Oz, O", "Wizard of Oz, The", "Aventura", "Zahar", 2013, 1, 1)]
    c.executemany("""INSERT INTO livro VALUES (?,)""", (many))
    conn.commit()
    conn.close()

def addMExemplar(many):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.executemany("""INSERT INTO exemplar VALUES (?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMAutor(many):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.executemany("""INSERT INTO autor VALUES (?,?,?)""", (many))
    conn.commit()
    conn.close()

def addMCataloga():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    many=[("37099909617", "11r/11r/2011", "12:12:12"),
            ("13859726373", "12r/12r/2012", "13:13:13"),
            ("24908114106", "13r/13r/2013", "14:14:14")]
    c.executemany("""INSERT INTO cataloga VALUES (?,)""", (many))
    conn.commit()
    conn.close()

def addMCadastra():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    many=[(1, "37099909617", "11r/11r/2011", "12:12:12"),
            (2, "13859726373", "12r/12r/2012", "13:13:13"),
            (3, "24908114106", "13r/13r/2013", "14:14:14")]
    c.executemany("""INSERT INTO cadastra VALUES (?,)""", (many))
    conn.commit()
    conn.close()


# # autor=[
# #       ( "Esopo",      "Esopo"     ,"8585466294" ),
# #       ( "Machado",    "Ana Maria" ,"8574061557" ),
# #       ( "Moraes, de", "Vinícius"  ,"8574062197" ),
# #       ( "Cafaggi",    "Lu"        ,"8565484572" ),
# #       ( "Cafaggi",    "Vítor"     ,"8565484572" ),
# #       ( "Baum",       "L. Frank"  ,"8537809667" )
# #     ]
# # addMAutor(autor)



# addMCadastra()
# addMCataloga()
# addMEmail()

exemplar=[
    ("1",1,"8585466294"),
    ("2",1,"8585466294"),
    ("3",1,"8585466294"),
    ("4",1,"8585466294"),
    ("5",1,"8585466294"),
]
addMExemplar(exemplar)


pessoa=[
     ("99999999911","pessoNome1","pessoaSobrenome1","12-12-2012","rua 1",134,"Valinhos","09340000"," "),
     ("99999999912","pessoNome2","pessoaSobrenome2","12-12-2012","rua 1",134,"Valinhos","09340000"," "),
     ("99999999913","pessoNome3","pessoaSobrenome3","12-12-2012","rua 1",134,"Valinhos","09340000"," "),
     ("99999999914","pessoNome4","pessoaSobrenome4","12-12-2012","rua 1",134,"Valinhos","09340000"," "),
     ("99999999915","pessoNome5","pessoaSobrenome5","12-12-2012","rua 1",134,"Valinhos","09340000"," "),
     ("99999999916","pessoNome6","pessoaSobrenome6","12-12-2012","rua 1",134,"Valinhos","09340000"," "),
     ("99999999917","pessoNome7","pessoaSobrenome7","12-12-2012","rua 1",134,"Valinhos","09340000"," "),
     ("99999999918","pessoNome8","pessoaSobrenome8","12-12-2012","rua 1",134,"Valinhos","09340000"," "),
 ]
addMPessoa(pessoa)

funcionario=[
    ("1231232",1.32,"bibliotecario","12-12-2012","99999999917"),
    ("1231231",1.211,"almoxarife","12-12-2012","99999999918"),
    ("1234566",1.3333,"faxina","12-12-2012","99999999916"),
]
addMFuncionario(funcionario)

# addMFone()



# livro=[
#     (""),
# ]
# addMLivro(livro)



# cadastra=[
#     (""),
# ]
# addMSocio()
