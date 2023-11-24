from excel import LerExcel
from DataBase import MusicaDAO, Musica
import tkinter as tk
import tkinter.messagebox


class Interface:
    def __init__(self, parent):
        self.myParent = parent
        self.container = tk.Frame(parent)
        self.container.pack()

        self.titulo = tk.Label(self.container, text="Música")
        self.titulo.config(font=("Arial", 20, "bold", "bold"), foreground="blue")

        self.lb_idt = tk.Label(self.container, text="Identificador:")
        self.lb_idt.config(font=("Arial", 12, "normal", "normal"), foreground="green")
        self.et_idt = tk.Entry(self.container)
        self.et_idt.config(font=("Arial", 12, "bold", "bold"), width=5)
        self.bt_idt = tk.Button(self.container, text="Consultar", command=self.consultar)
        self.bt_idt.configure(font=("Arial", 14, "normal", "normal"), foreground="blue")

        self.lb_nome = tk.Label(self.container, text="Nome da Música:")
        self.lb_nome.config(font=("Arial", 12, "normal", "normal"), foreground="green")
        self.et_nome = tk.Entry(self.container)
        self.et_nome.config(font=("Arial", 12, "bold", "bold"), width=30)

        self.lb_valor = tk.Label(self.container, text="Nome do Artista:")
        self.lb_valor.config(font=("Arial", 12, "normal", "normal"), foreground="green")
        self.et_valor = tk.Entry(self.container)
        self.et_valor.config(font=("Arial", 12, "bold", "bold"), width=30)

        self.lb_us = tk.Label(self.container, text="Letra Inglês:")
        self.lb_us.config(font=("Arial", 12, "normal", "normal"), foreground="green")
        self.tx_us = tk.Text(self.container, height=5, width=40)
        self.tx_us.config(font=("Arial", 12, "bold", "bold"))

        self.lb_br = tk.Label(self.container, text="Letra Português:")
        self.lb_br.config(font=("Arial", 12, "normal", "normal"), foreground="green")
        self.tx_br = tk.Text(self.container, height=5, width=40)
        self.tx_br.config(font=("Arial", 12, "bold", "bold"))

        self.bt_novo = tk.Button(self.container, text="Novo", command=self.novo)
        self.bt_novo.configure(font=("Arial", 14, "normal", "normal"), foreground="blue")
        self.bt_salvar = tk.Button(self.container, text="Salvar", command=self.alterar)
        self.bt_salvar.configure(font=("Arial", 14, "normal", "normal"), foreground="blue")
        self.bt_excluir = tk.Button(self.container, text="Excluir", command=self.excluir)
        self.bt_excluir.configure(font=("Arial", 14, "normal", "normal"), foreground="blue")

        self.titulo.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.lb_idt.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.et_idt.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.bt_idt.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        self.lb_nome.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.et_nome.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="w")

        self.lb_valor.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.et_valor.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="w")

        self.lb_us.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.tx_us.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="w")

        self.lb_br.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.tx_br.grid(row=5, column=1, columnspan=2, padx=10, pady=10, sticky="w")

        self.bt_novo.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.bt_salvar.grid(row=6, column=1, padx=10, pady=10, sticky="w")
        self.bt_excluir.grid(row=6, column=2, columnspan=2, padx=10, pady=10, sticky="w")

        self.dao = MusicaDAO()


    def consultar(self):
        idt = self.et_idt.get()
        if idt.isdigit() and idt != "0":
            idt_int = int(idt)
            a = self.dao.consultar(idt_int)
            if a.idt == 0:
                tkinter.messagebox.showwarning("Não encontrado", "ID não encontrado na base de dados")
                self.et_idt.focus()
            else:
                self.limpar()
                self.et_idt.insert(0, str(a.idt))
                self.et_nome.insert(0, a.nome)
                self.tx_us.insert("1.0", a.texto_us)
                self.tx_br.insert("1.0", a.texto_br)
                self.et_valor.insert(0, a.artista)
                self.et_nome.focus()
        else:
            tkinter.messagebox.showerror("Inválido", "Valor inválido para consulta por ID")
            self.et_idt.focus()

    def limpar(self):
        for entry in (self.et_idt, self.et_nome, self.et_valor, self.tx_us, self.tx_br):
            if isinstance(entry, tk.Text):
                entry.delete("1.0", tk.END)
            else:
                entry.delete(0, tk.END)

    def novo(self):
        self.limpar()
        self.et_idt.insert(0, "0")
        self.et_nome.focus()

    def excluir(self):
        idt = self.et_idt.get()
        if idt.isdigit() and idt != "0":
            idt_int = int(idt)
            self.dao.excluir(idt_int)
            tkinter.messagebox.showinfo("Exclusão", "Exclusão efetuada com sucesso")
        else:
            tkinter.messagebox.showerror("Inválido", "Valor inválido para exclusão por ID")
            self.et_idt.focus()

    def alterar(self):
        if self.et_idt.get() == "0" or self.et_idt.get() == "":
            a = Musica(nome=self.et_nome.get(), artista=self.et_valor.get(), texto_us=self.tx_us.get("1.0", tk.END), texto_br=self.tx_br.get("1.0", tk.END))
            self.dao.incluir(a)
            tkinter.messagebox.showinfo("Inclusão", "Inclusão efetuada com sucesso!")
            self.et_nome.focus()
        else:
            idt = self.et_idt.get()
            if idt.isdigit():
                idt_int = int(idt)
                a = Musica(nome=self.et_nome.get(), artista=self.et_valor.get(), texto_us=self.tx_us.get("1.0", tk.END), texto_br=self.tx_br.get("1.0", tk.END), idt=self.et_idt.get())
                self.dao.alterar(a)
                tkinter.messagebox.showinfo("Alteração", "Alteração efetuada com sucesso")
                self.et_nome.focus()
            else:
                tkinter.messagebox.showerror("Inválido", "Valor inválido no ID")
                self.et_idt.focus()


def migrar():
   ARQUIVO = "musicas.xlsx"
   PLANILHA = "Planilha1"
   artista = ""
   texto_br = ""
   texto_us = ""

   exc = LerExcel(ARQUIVO, PLANILHA)
   dao = MusicaDAO()
   nome = ""
   for linha in range(2, exc.get_max_linha()+1):
       teste = exc.cell_string(linha, 1)
       if teste != "None" and nome != "":
           m = Musica()
           m.nome = nome
           m.artista = artista
           m.texto_us = texto_us
           m.texto_br = texto_br
           dao.incluir(m)
           print("Importada música: ", nome)
           nome = teste
           artista = exc.cell_string(linha, 2)
           texto_us = exc.cell_string(linha, 3) + "\n"
           texto_br = exc.cell_string(linha, 4) + "\n"
       elif teste != "None":
           nome = teste
           artista = exc.cell_string(linha, 2)
           texto_us = exc.cell_string(linha, 3) + "\n"
           texto_br = exc.cell_string(linha, 4) + "\n"
       else:
           texto_us += exc.cell_string(linha, 3) + "\n"
           texto_br += exc.cell_string(linha, 4) + "\n"

   m = Musica()
   m.nome = nome
   m.artista = artista
   m.texto_us = texto_us
   m.texto_br = texto_br
   dao.incluir(m)
   print("Importada música: ", nome)
   print("Fim de importação")

   lista = dao.consultar_todos()
   for m in lista:
       print(m.nome, m.artista)
       print(m.texto_us)
       print(m.texto_br)
       print("-" * 50)



def main():
    migrar()
    raiz = tk.Tk()
    raiz.title("Consulta de Músicas")
    apl = Interface(raiz)
    raiz.mainloop()



if __name__ == "__main__":
   main()
