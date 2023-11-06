import tkinter as tk
import tkinter.messagebox
from RegistroDeAlunos.aluno import Aluno, AlunoDAO


class Container:
    def __init__(self, parent):
        self.myParent = parent
        self.container = tk.Frame(parent)
        self.container.pack()

        self.titulo = tk.Label(self.container, text="Cadastro de Alunos")
        self.titulo.config(font=("Arial", 20, "bold", "bold"), foreground="blue")

        self.lb_idt = tk.Label(self.container, text="Identificador:")
        self.lb_idt.config(font=("Arial", 12, "normal", "normal"), foreground="green")
        self.et_idt = tk.Entry(self.container)
        self.et_idt.config(font=("Arial", 12, "bold", "bold"), width=14)
        self.bt_idt = tk.Button(self.container, text="Consultar", command=self.consultar)
        self.bt_idt.configure(font=("Arial", 14, "normal", "normal"), foreground="blue")

        self.lb_nome = tk.Label(self.container, text="Nome:")
        self.lb_nome.config(font=("Arial", 12, "normal", "normal"), foreground="green")
        self.et_nome = tk.Entry(self.container)
        self.et_nome.config(font=("Arial", 12, "bold", "bold"), width=40)

        self.lb_nota1 = tk.Label(self.container, text="Nota 1:")
        self.lb_nota1.config(font=("Arial", 12, "normal", "normal"), foreground="green")
        self.et_nota1 = tk.Entry(self.container)
        self.et_nota1.config(font=("Arial", 12, "bold", "bold"), width=8)

        self.lb_nota2 = tk.Label(self.container, text="Nota 2:")
        self.lb_nota2.config(font=("Arial", 12, "normal", "normal"), foreground="green")
        self.et_nota2 = tk.Entry(self.container)
        self.et_nota2.config(font=("Arial", 12, "bold", "bold"), width=8)

        self.lb_faltas = tk.Label(self.container, text="Número de Faltas:")
        self.lb_faltas.config(font=("Arial", 12, "normal", "normal"), foreground="green")
        self.et_faltas = tk.Entry(self.container)
        self.et_faltas.config(font=("Arial", 12, "bold", "bold"), width=5)

        self.bt_novo = tk.Button(self.container, text="Novo", command=self.novo)
        self.bt_novo.configure(font=("Arial", 14, "normal", "normal"), foreground="blue")
        self.bt_salvar = tk.Button(self.container, text="Salvar", command=self.salvar)
        self.bt_salvar.configure(font=("Arial", 14, "normal", "normal"), foreground="blue")
        self.bt_excluir = tk.Button(self.container, text="Excluir", command=self.excluir)
        self.bt_excluir.configure(font=("Arial", 14, "normal", "normal"), foreground="blue")

        self.titulo.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.lb_idt.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.et_idt.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.bt_idt.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        self.lb_nome.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.et_nome.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="w")

        self.lb_nota1.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.et_nota1.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.lb_nota2.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.et_nota2.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.lb_faltas.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.et_faltas.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        self.bt_novo.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.bt_salvar.grid(row=6, column=1, padx=10, pady=10, sticky="w")
        self.bt_excluir.grid(row=6, column=2, columnspan=2, padx=10, pady=10, sticky="w")

        self.dao = AlunoDAO()

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
                self.et_nota1.insert(0, a.nota1)
                self.et_nota2.insert(0, a.nota2)
                self.et_faltas.insert(0, a.numero_faltas)
                self.et_nome.focus()
        else:
            tkinter.messagebox.showerror("Inválido", "Valor inválido para consulta por ID")
            self.et_idt.focus()

    def limpar(self):
        for entry in (self.et_idt, self.et_nome, self.et_nota1, self.et_nota2, self.et_faltas):
            entry.delete(0, len(entry.get()))

    def novo(self):
        self.limpar()
        self.et_idt.insert(0, "0")
        self.et_nome.focus()

    def vazio(self):
        if self.et_nome.get() == "":
            tkinter.messagebox.showerror("Nome Obrigatório", "Preencha o nome do aluno")
            self.et_nome.focus()
            return True

        if self.et_nota1.get() == "" or (not self.et_nota1.get().replace('.', '', 1).isdigit()):
            tkinter.messagebox.showerror("Nota 1 inválida", "Preencha uma nota válida")
            self.et_nota1.focus()
            return True

        if self.et_nota2.get() == "" or (not self.et_nota2.get().replace('.', '', 1).isdigit()):
            tkinter.messagebox.showerror("Nota 2 inválida", "Preencha uma nota válida")
            self.et_nota2.focus()
            return True

        if self.et_faltas.get() == "" or (not self.et_faltas.get().isdigit()):
            tkinter.messagebox.showerror("Número de Faltas inválido", "Preencha um número de faltas válido")
            self.et_faltas.focus()
            return True

        return False

    def salvar(self):
        if self.vazio():
            return

        if self.et_idt.get() == "0" or self.et_idt.get() == "":
            a = Aluno(nome=self.et_nome.get(), nota1=self.et_nota1.get(), nota2=self.et_nota2.get(), numero_faltas=self.et_faltas.get())
            self.dao.incluir(a)
            self.novo()
            tkinter.messagebox.showinfo("Inclusão", "Inclusão efetuada com sucesso!")
            self.et_nome.focus()
        else:
            idt = self.et_idt.get()
            if idt.isdigit():
                idt_int = int(idt)
                a = Aluno(idt=idt_int, nome=self.et_nome.get(), nota1=self.et_nota1.get(), nota2=self.et_nota2.get(), numero_faltas=self.et_faltas.get())
                self.dao.alterar(a)
                tkinter.messagebox.showinfo("Alteração", "Alteração efetuada com sucesso")
                self.et_nome.focus()
            else:
                tkinter.messagebox.showerror("Inválido", "Valor inválido no ID")
                self.et_idt.focus()

    def excluir(self):
        idt = self.et_idt.get()
        if idt.isdigit() and idt != "0":
            idt_int = int(idt)
            self.dao.excluir(idt_int)
            tkinter.messagebox.showinfo("Exclusão", "Exclusão efetuada com sucesso")
            self.novo()
        else:
            tkinter.messagebox.showerror("Inválido", "Valor inválido para exclusão por ID")
            self.et_idt.focus()


def main():
    raiz = tk.Tk()
    raiz.title("Cadastro de Alunos")
    apl = Container(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    main()