from pathlib import Path
import sqlite3


class Aluno:
    def __init__(self, idt=0, nome="", nota1=0.0, nota2=0.0, numero_faltas=0):
        self.idt = idt
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.numero_faltas = numero_faltas

class AlunoDAO:
    def __init__(self):
        if Path("alunos.db").exists():
            self.cnx = sqlite3.connect("alunos.db")
        else:
            self.cnx = sqlite3.connect("alunos.db")
            crs = self.cnx.cursor()
            cmd = '''
            CREATE TABLE aluno(
                idt integer primary key autoincrement,
                nome varchar(50) not null,
                nota1 decimal(3,1) not null,
                nota2 decimal(3,1) not null,
                numero_faltas integer not null)
            '''
            crs.execute(cmd, [])
            self.cnx.commit()
            crs.close()

    def __del__(self):
        self.cnx.close()

    def incluir(self, a):
        cmd = "insert into aluno(nome, nota1, nota2, numero_faltas) values (?, ?, ?, ?)"
        crs = self.cnx.cursor()
        crs.execute(cmd, [a.nome, a.nota1, a.nota2, a.numero_faltas])
        self.cnx.commit()
        crs.close()

    def consultar(self, idt):
        cmd = "select * from aluno where idt=?"
        crs = self.cnx.cursor()
        crs.execute(cmd, [idt])
        dados = crs.fetchone()
        crs.close()
        if dados is None:
            return Aluno()
        else:
            return Aluno(dados[0], dados[1], dados[2], dados[3], dados[4])

    def alterar(self, a):
        cmd = "update aluno set nome=?, nota1=?, nota2=?, numero_faltas=? where idt=?"
        crs = self.cnx.cursor()
        crs.execute(cmd, [a.nome, a.nota1, a.nota2, a.numero_faltas, a.idt])
        self.cnx.commit()
        crs.close()

    def excluir(self, idt):
        cmd = "delete from aluno where idt=?"
        crs = self.cnx.cursor()
        crs.execute(cmd, [idt])
        self.cnx.commit()
        crs.close()
