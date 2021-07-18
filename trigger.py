import sqlite3

conn = sqlite3.connect('biblioteca.db')
c = conn.cursor()

c.execute("""PRAGMA foreign_keys = ON;""")

#criar os triggers

#mudar "emprestado" quando é feito empréstimo
#c.execute("""DROP TRIGGER IF EXISTS mudaEmprestadoE""")
c.execute("""CREATE TRIGGER IF NOT EXISTS mudaEmprestadoE
            AFTER INSERT ON emprestimo
                BEGIN
                    UPDATE exemplar 
                        SET emprestado = 1
                    WHERE exemplar.codigoExemplar=new.codigoExemplar;
                END;
    """)

#mudar "emprestado" quando é feita devolução 
#.execute("""DROP TRIGGER IF EXISTS mudaEmprestadoD""")
c.execute("""CREATE TRIGGER IF NOT EXISTS mudaEmprestadoD
            AFTER INSERT ON devolucao
                BEGIN
                    UPDATE exemplar 
                        SET emprestado = 0
                    WHERE exemplar.codigoExemplar=new.codigoExemplar;
                END;
    """)

#validar e-mail
c.execute("""CREATE TRIGGER IF NOT EXISTS verificaEmail
            BEFORE INSERT ON pessoa
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
            BEFORE INSERT ON pessoa
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

#deletar autor quando deleta livro
c.execute("""CREATE TRIGGER IF NOT EXISTS deletaAutor 
            AFTER DELETE ON livro
                BEGIN
                    DELETE FROM autor WHERE autor.isbn=old.isbn;
                END;
    """)

#deletar funcionario quando deleta pessoa
c.execute("""CREATE TRIGGER IF NOT EXISTS deletaFuncionario 
            AFTER DELETE ON pessoa
                BEGIN
                    DELETE FROM funcionario WHERE funcionario.cpf=old.cpf;
                END;
    """)

#deletaar socio quando deleta pessoa
c.execute("""CREATE TRIGGER IF NOT EXISTS deletaSocio
            AFTER DELETE ON pessoa
                BEGIN
                    DELETE FROM socio WHERE socio.cpf=old.cpf;
                END;
    """)

#diminuir contador
c.execute("""CREATE TRIGGER IF NOT EXISTS decreaseCounter 
            AFTER DELETE ON exemplar
                BEGIN
                    UPDATE livro
                        SET numeroExemplar=numeroExemplar-1 
                        WHERE livro.isbn=old.isbn;
                END;
    """)

#aumentar contador
c.execute("""CREATE TRIGGER IF NOT EXISTS increaseCounter 
            AFTER INSERT ON exemplar
                BEGIN
                    UPDATE livro
                        SET numeroExemplar=numeroExemplar+1 
                        WHERE livro.isbn=new.isbn;
                END;
    """)

conn.commit()
conn.close()