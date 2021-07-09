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
        complemento TEXT
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS socio(
        numeroCadastro INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
        cpf TEXT,
        FOREIGN KEY(cpf) REFERENCES pessoa(cpf)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS funcionario(
        cpts INTEGER NOT NULL UNIQUE PRIMARY KEY,
        salario FLOAT NOT NULL,
        funcao TEXT NOT NULL,
        dataContato TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        FOREIGN KEY(cpf) REFERENCES pessoa(cpf)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS fone(
        telefone TEXT NOT NULL, 
        cpf TEXT NOT NULL,
        PRIMARY KEY(cpf, telefone)
        FOREIGN KEY(cpf) REFERENCES pessoa(cpf)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS email(
        email TEXT NOT NULL, 
        cpf TEXT NOT NULL,
        PRIMARY KEY(cpf, email)
        FOREIGN KEY(cpf) REFERENCES pessoa(cpf)
            ON UPDATE CASCADE
            ON DELETE CASCADE 
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS livro(
        isbn INTEGER NOT NULL UNIQUE PRIMARY KEY,
        titTrad TEXT NOT NULL,
        titOrig TEXT NOT NULL,
        locEst INTEGER AUTO INCREMENT,
        locSecao INTEGER AUTO INCREMENT,
        editora TEXT NOT NULL,
        genero TEXT NOT NULL,
        anoPubli INTEGER NOT NULL,
        edicao INTEGER NOT NULL,
        volumes INTEGER 
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS exemplar(
        locPrat INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        emprestado INTEGER NOT NULL,
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
        registo INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        numeroCadastro INTEGER NOT NULL,
        cpfFunc TEXT NOT NULL,
        locPrat INTEGER NOT NULL,
        dataE TEXT NOT NULL,
        horaE TEXT NOT NULL
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS devolucao(
        registo INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        numeroCadastro INTEGER NOT NULL,
        cpfFunc TEXT NOT NULL,
        locPrat INTEGER NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL,
        isbn INTEGER NOT NULL    
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS cataloga(
        registo INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        cpfFunc TEXT NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL  
    )""")

c.execute(""" CREATE TABLE IF NOT EXISTS cadastra(
        registo INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        numeroCadastro INTEGER NOT NULL,
        cpfFunc TEXT NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL  
    )""")

#print('All tables created successfully')

#criar as views
#view com informações dos livros para qualquer busca (isbn, nomes, autor, edição, )
c.execute("""CREATE VIEW IF NOT EXISTS viewLivro AS
                SELECT
                    livro.isbn,
                    locPrat AS Código,
                    livro.titTrad AS Título,
                    livro.locEst AS Estante,
                    livro.locSecao AS Seção,
                    autor.sobrenome AS Sobrenome,
                    autor.nome AS Nome,  
                    livro.editora AS Editora,
                    livro.edicao AS Edição,  
                    livro.anoPubli AS Publicação,
                    (SELECT count(*)
                        FROM exemplar
                        WHERE exemplar.isbn=livro.isbn AND exemplar.emprestado=0)
                FROM
                    livro
                INNER JOIN exemplar ON exemplar.isbn = livro.isbn
                INNER JOIN autor ON autor.isbn = livro.isbn;
        """)

#view com contagem dos volumes disponíveis de um livro
"""c.execute(CREATE VIEW IF NOT EXISTS contaExemplar AS
                SELECT count(isbn) as exemplares                
                FROM
                    exemplar
                WHERE emprestado=false;
        )"""

#view de empréstimos
c.execute("""CREATE VIEW IF NOT EXISTS viewEmprestimos AS
                SELECT 
                    socio.numeroCadastro AS Cadastro,
                    pessoa.nome AS Nome,
                    pessoa.sobrenome AS Sobrenome,
                    livro.titTrad AS Título,
                    exemplar.locPrat AS Código,
                    emprestimo.dataE AS DataEmpréstimo,
                    devolucao.data AS DataDevolução
                FROM
                    pessoa, emprestimo
                INNER JOIN socio ON socio.cpf = pessoa.cpf
                INNER JOIN emprestimo ON emprestimo.cpfSocio = pessoa.cpf
                INNER JOIN devolucao ON devolucao.cpfSocio = pessoa.cpf
                INNER JOIN livro ON livro.isbn = emprestimo.isbn
                INNER JOIN exemplar ON exemplar.isbn = emprestimo.isbn;
        """)

#view de funcionários-> dados de pessoa + salário, cpts, data de contratação
c.execute("""CREATE VIEW IF NOT EXISTS viewFuncionario AS
                SELECT 
                    pessoa.cpf AS CPF,
                    pessoa.nome AS Nome,
                    pessoa.sobrenome AS Sobrenome,
                    funcionario.cpts AS CPTS,
                    funcionario.funcao AS Função,
                    funcionario.salario AS Salário,
                    email.email AS Email,
                    fone.telefone AS Telefone,
                    pessoa.rua AS Rua,
                    pessoa.numero AS Número,
                    pessoa.cidade AS Cidade
                FROM
                    pessoa
                INNER JOIN funcionario ON funcionario.cpf = pessoa.cpf
                INNER JOIN email ON email.cpfSocio = pessoa.cpf
                INNER JOIN fone ON fone.cpfSocio = pessoa.cpf;
        """)

#view de sócios -> nome, sobrenome, dob, endereço, código, contatos.
c.execute("""CREATE VIEW IF NOT EXISTS viewSocio AS
                SELECT 
                    socio.numeroCadastro AS Cadastro,
                    pessoa.cpf AS CPF,
                    pessoa.nome AS Nome,
                    pessoa.sobrenome AS Sobrenome,
                    email.email AS Email,
                    fone.telefone AS Telefone,
                    pessoa.rua AS Rua,
                    pessoa.numero AS Número,
                    pessoa.cidade AS Cidade
                FROM
                    pessoa
                INNER JOIN socio ON socio.cpf = pessoa.cpf
                INNER JOIN email ON email.cpfSocio = pessoa.cpf
                INNER JOIN fone ON fone.cpfSocio = pessoa.cpf;
        """)

#criar os triggers

#mudar "emprestado" quando é feito empréstimo
#c.execute("""DROP TRIGGER IF EXISTS mudaEmprestadoE""")
c.execute("""CREATE TRIGGER IF NOT EXISTS mudaEmprestadoE
            AFTER INSERT ON emprestimo
                BEGIN
                    UPDATE exemplar 
                        SET emprestado = 1
                    WHERE exemplar.locPrat=new.locPrat;
                END;
    """)

#mudar "emprestado" quando é feita devolução 
#.execute("""DROP TRIGGER IF EXISTS mudaEmprestadoD""")
c.execute("""CREATE TRIGGER IF NOT EXISTS mudaEmprestadoD
            AFTER INSERT ON devolucao
                BEGIN
                    UPDATE exemplar 
                        SET emprestado = 0
                    WHERE exemplar.locPrat=new.locPrat;
                END;
    """)

#validar e-mail
c.execute("""CREATE TRIGGER IF NOT EXISTS verificaEmail
            BEFORE INSERT ON email
            BEGIN
                SELECT
                    CASE
                        WHEN new.email NOT LIKE '%_@_%._%' THEN
                        RAISE(ABORT, 'ENDEREÇO DE E-MAIL INVÁLIDO')
                     END;
            END;
        """)

#validar telefone
c.execute("""CREATE TRIGGER IF NOT EXISTS verificaFone
            BEFORE INSERT ON fone
            BEGIN
                SELECT
                    CASE
                        WHEN new.telefone NOT LIKE '%_-_%' THEN
                        RAISE(ABORT, 'TELEFONE INVÁLIDO')
                     END;
            END;
        """)

#deletar exemplares quando deleta livro
c.execute("""CREATE TRIGGER IF NOT EXISTS deletaExemplar 
            AFTER DELETE ON livro
                BEGIN
                    DELETE FROM exemplar WHERE exemplar.isbn=old.isbn;
                END;
    """)

#diminuir contador
c.execute("""CREATE TRIGGER IF NOT EXISTS decreaseCounter 
            AFTER DELETE ON exemplar
                BEGIN
                    UPDATE livro
                        SET volumes=volumes-1 
                        WHERE livro.isbn=old.isbn;
                END;
    """)
conn.commit()
conn.close()