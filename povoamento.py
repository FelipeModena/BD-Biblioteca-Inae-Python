import sqlite3
import database

def addMPessoa():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    many=[("076.728.597-22", "Victor", "da Costa", "24r/04r/1974", "D2", 995, "Bauru", "49070-790", "none"),
            ("214.755.103-14", "Sônia", "Carolina da Rocha", "25r/03r/1975", "Av. Getúlio Vargas", 996, "Bauru", "98801-027", "ap 12"),
            ("420.272.234-52", "Lavínia", "da Mata", "03r/09r/1974", "Travessa Pilates", 536, "Bauru", "69918-258"),
            ("825.029.244-80", "Claudio", "Santos", "10r/09r/1960", "DF", 484, "Bauru", "72578-000"),
            ("084.313.437-29", "Thiago", "Carvalho", "06r/08r/1977", "Pindaí", 677, "Bauru", "52191-120"),
            ("311.572.890-53", "Luiza", "Teixeira", "18r/11r/1982", "Pedro Álvares", 883, "Bauru", "57072-312")]
    c.executemany("""INSERT INTO pessoa VALUES (?,)""", (many))
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

def addMFuncionario():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    many=[("37099909617", 1500.0, "Secretario", "1/1/2001", "825.029.244-80"),
           ("13859726373", 2000.0, "Bibliotecario", "2/2/2002", "084.313.437-29"),
            ("24908114106", 1500.0, "Segurança", "3/3/2003", "311.572.890-53")]
    c.executemany("""INSERT INTO funcionario VALUES (?,)""", (many))
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

def addMExemplar():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    many=[(0, "8585466294"), 
            (0, "8574061557"), 
            (0, "8574062197"), 
            (0, "8565484572"), 
            (0, "8537809667")]
    c.executemany("""INSERT INTO exemplar VALUES (?,)""", (many))
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


many=[
      ( "Esopo",      "Esopo"     ,"8585466294" ),
      ( "Machado",    "Ana Maria" ,"8574061557" ),
      ( "Moraes, de", "Vinícius"  ,"8574062197" ),
      ( "Cafaggi",    "Lu"        ,"8565484572" ),
      ( "Cafaggi",    "Vítor"     ,"8565484572" ),
      ( "Baum",       "L. Frank"  ,"8537809667" )
    ]
addMAutor(many)

addMCadastra()

addMCataloga()

addMEmail()

addMExemplar()

addMFone()

addMFuncionario()

addMLivro()

addMPessoa()

addMSocio()
