import sqlite3

# ------ PESQUISAS POR SÓCIO ------

#todos os socios
def todoSocio():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewSocio  
                ORDER BY nome;    
            """)
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(todoSocio())

#sócio n cadastro(a-z)
def ordemAlfNumCadastro(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewSocio
                WHERE Cadastro=?  
                ORDER BY nome;    
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfNumCadastro(1))

#sócio nome a-z
def ordemAlfNomeCadastro(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewSocio
                WHERE Nome=?    
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfNomeCadastro("pessoNome1",))

#sócio nome z-a
def ordemAlfDNomeCadastro(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewSocio
                WHERE Nome=?  
                ORDER BY Nome 
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfDNomeCadastro("pessoNome1",))

#socio sobrenome a-z
def ordemAlfSobrenomeCadastro(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewSocio
                WHERE Sobrenome=?  
                ORDER BY Sobrenome;    
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfSobrenomeCadastro("pessoaSobrenome1",))

#socio sobrenome z-a
def ordemAlfDSobrenomeCadastro(nome):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewSocio
                WHERE Sobrenome=?  
                ORDER BY Sobrenome DESC   
            """, (nome, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(ordemAlfDSobrenomeCadastro("pessoaSobrenome1",))

#sócio por CPF
def pesquisaSocioCPF(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewSocio
                WHERE CPF=?
            """, (text, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(pesquisaSocioCPF("99999999911"))

#sócio por email
def pesquisaSocioEmail(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewSocio
                WHERE Email=?
            """, (text, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(pesquisaSocioEmail("asdas@Sgdfd.com"))

# ------ PESQUISAS POR EMPREGADO ------

#todos os funcionario
def todoFuncionario():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewFuncionario  
                ORDER BY nome;    
            """)
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(todoFuncionario())

#funcionario por nome
def pesquisaFuncionarioNome(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewFuncionario
                WHERE Nome=? 
            """, (text, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(pesquisaFuncionarioNome("pessoNome6"))

#funcionario por sobrenome
def pesquisaFuncionarioSobrenome(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewFuncionario
                WHERE Sobrenome=? 
            """, (text, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(pesquisaFuncionarioSobrenome("pessoaSobrenome6"))

#funcionario por CPF
def pesquisaFuncionarioCPF(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewFuncionario
                WHERE CPF=? 
            """, (text, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(pesquisaFuncionarioCPF("99999999916"))

#funcionario por CPTS
def pesquisaFuncionarioCPTS(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewFuncionario
                WHERE CPTS=? 
            """, (text, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(pesquisaFuncionarioCPTS("1234566"))

#funcionario por função
def pesquisaFuncionarioFuncao(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewFuncionario
                WHERE Funcao=? 
            """, (text, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(pesquisaFuncionarioFuncao("bibliotecario"))

#funcionario por email
def pesquisaFuncionarioEmail(text):
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM viewFuncionario
                WHERE Email=? 
            """, (text, ))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(pesquisaFuncionarioEmail("asdas@Sgdfd.com"))