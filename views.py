import sqlite3

conn = sqlite3.connect('biblioteca.db')
c = conn.cursor()

c.execute("""PRAGMA foreign_keys = ON;""")

#criar as views
#view com informações dos livros para qualquer busca (isbn, nomes, autor, edição, )
c.execute("""CREATE VIEW IF NOT EXISTS viewLivro AS
                SELECT
                    livro.isbn AS ISBN,
                    livro.titTrad AS Titulo,
                    livro.titOrig AS TituloOriginal,
                    livro.genero AS Genero,
                    livro.editora AS Editora,
                    autor.nome AS Nome,
                    autor.sobrenome AS sobrenome,
                    (SELECT count(*)
                        FROM exemplar
                        WHERE exemplar.isbn=livro.isbn AND exemplar.emprestado=0) AS exemplares
                FROM
                    livro
                INNER JOIN exemplar ON exemplar.isbn = livro.isbn
                INNER JOIN autor ON autor.isbn = livro.isbn
                GROUP BY
                    livro.isbn;
        """)

c.execute("""CREATE VIEW IF NOT EXISTS viewExemplar AS
                SELECT
                    exemplar.codigoExemplar AS Codigo,
                    livro.isbn AS ISBN,
                    livro.titTrad AS Titulo,
                    livro.titOrig AS TituloOriginal,
                    autor.sobrenome AS Sobrenome,
                    autor.nome AS Nome,  
                    livro.genero AS Genero,
                    livro.editora AS Editora,
                    exemplar.edicao AS Edicao,  
                    exemplar.anoPubli AS Publicacao,
                    exemplar.emprestado AS Emprestado
                FROM
                    livro
                INNER JOIN exemplar ON exemplar.isbn = livro.isbn
                INNER JOIN autor ON autor.isbn = livro.isbn;
        """)

#view de empréstimos
c.execute("""CREATE VIEW IF NOT EXISTS viewEmprestimos AS
                SELECT 
                    emprestimo.codigoEmprestimo AS Codigo,
                    emprestimo.socio AS Cadastro,
                    pessoa.nome AS Nome,
                    pessoa.sobrenome AS Sobrenome,
                    emprestimo.codigoExemplar AS Codigo,
                    livro.titTrad AS Titulo,
                    emprestimo.dataE AS DataEmprestimo,
                    emprestimo.horaE AS HoraEmprestimo
                FROM
                    socio, emprestimo, livro, exemplar
                INNER JOIN socio ON socio.cpf = pessoa.cpf
                INNER JOIN emprestimo ON emprestimo.socio = socio.numeroCadastro
                INNER JOIN livro ON livro.isbn = exemplar.isbn
                INNER JOIN exemplar ON exemplar.codigoExemplar = emprestimo.codigoExemplar;
        """)

#view de funcionários-> dados de pessoa + salário, cpts, data de contratação
c.execute("""CREATE VIEW IF NOT EXISTS viewFuncionario AS
                SELECT 
                    pessoa.cpf AS CPF,
                    pessoa.nome AS Nome,
                    pessoa.sobrenome AS Sobrenome,
                    pessoa.dob AS DataNascimento,
                    funcionario.cpts AS CPTS,
                    funcionario.funcao AS Funcao,
                    funcionario.salario AS Salario,
                    funcionario.dataContrato AS DataContrato,
                    pessoa.rua AS Rua,
                    pessoa.numero AS Numero,
                    pessoa.cidade AS Cidade,
                    pessoa.CEP AS CEP,
                    pessoa.email AS Email,
                    pessoa.telefone AS Telefone
                FROM
                    pessoa
                INNER JOIN funcionario ON funcionario.cpf = pessoa.cpf;
        """)

#view de sócios -> nome, sobrenome, dob, endereço, código, contatos.
c.execute("""CREATE VIEW IF NOT EXISTS viewSocio AS
                SELECT 
                    socio.numeroCadastro AS Cadastro,
                    pessoa.cpf AS CPF,
                    pessoa.nome AS Nome,
                    pessoa.sobrenome AS Sobrenome,
                    pessoa.dob AS DataNascimento,
                    pessoa.email AS Email,
                    pessoa.telefone AS Telefone,
                    pessoa.rua AS Rua,
                    pessoa.numero AS Numero,
                    pessoa.cidade AS Cidade,
                    pessoa.CEP AS CEP
                FROM
                    pessoa
                INNER JOIN socio ON socio.cpf = pessoa.cpf;
        """)

conn.commit()
conn.close()