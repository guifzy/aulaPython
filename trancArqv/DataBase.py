from pathlib import Path
import sqlite3


class Musica:

   def __init__(self, idt=0, nome="", artista="", texto_us="", texto_br=""):
       self.idt = idt
       self.nome = nome
       self.artista = artista
       self.texto_us = texto_us
       self.texto_br = texto_br


class MusicaDAO:

   def __init__(self):
       if Path("musicas.db").exists():
           self.cnx = sqlite3.connect("musicas.db")
       else:
           self.cnx = sqlite3.connect("musicas.db")
           crs = self.cnx.cursor()
           cmd = '''
           CREATE TABLE musica(
             idt integer primary key autoincrement,
             nome varchar(50) not null,
             artista varchar(50) not null,
             texto_us text not null,
             texto_br text not null)
           '''
           crs.execute(cmd, [])
           self.cnx.commit()
           crs.close()

   def __del__(self):
       self.cnx.close()

   def incluir(self, m):
       cmd = "insert into musica(nome, artista, texto_us, texto_br) values (?, ?, ?, ?)"
       crs = self.cnx.cursor()
       crs.execute(cmd, [m.nome, m.artista, m.texto_us, m.texto_br])
       self.cnx.commit()
       crs.close()

   def consultar(self, idt):
       cmd = "select * from musica where idt=?"
       crs = self.cnx.cursor()
       crs.execute(cmd, [idt])
       dados = crs.fetchone()
       crs.close()
       if dados is None:
           return Musica()
       else:
           return Musica(dados[0], dados[1], dados[2], dados[3], dados[4])

   def consultar_todos(self):
       cmd = "select * from musica"
       crs = self.cnx.cursor()
       crs.execute(cmd, [])
       lista = []
       for dados in crs.fetchall():
           m = Musica(dados[0], dados[1], dados[2], dados[3], dados[4])
           lista.append(m)
       crs.close()
       return lista

   def alterar(self, m):
       cmd = "update musica set nome=?, artista=?, texto_us=?, texto_br=? where idt=?"
       crs = self.cnx.cursor()
       crs.execute(cmd, [m.nome, m.artista, m.texto_us, m.texto_br, m.idt])
       self.cnx.commit()
       crs.close()

   def excluir(self, idt):
       cmd = "delete from musica where idt=?"
       crs = self.cnx.cursor()
       crs.execute(cmd, [idt])
       self.cnx.commit()
       crs.close()
