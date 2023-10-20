import tkinter as tk
from tkinter import ttk
import requests
import json

class Container:
    def __init__(self, parent):
        self.myParent = parent
        self.container = tk.Frame(parent)
        self.container.pack()

        self.titulo = ttk.Label(self.container, text="Consultar CEP")
        self.titulo.config(font=("Arial", 14, "bold"))

        self.uf = ttk.Label(self.container, text="UF:")
        self.uf.config(font=("Arial", 14, "normal"))

        self.muni = ttk.Label(self.container, text="Município:")
        self.muni.config(font=("Arial", 14, "normal"))

        self.logra = ttk.Label(self.container, text="Logradouro:")
        self.logra.config(font=("Arial", 14, "normal"))

        # consulta UF
        self.ufEntry = ttk.Entry(self.container)
        self.ufEntry.config(font=("Arial", 14), width=30)

        # consulta município
        self.muniEntry = ttk.Entry(self.container)
        self.muniEntry.config(font=("Arial", 14), width=30)

        # consulta logradouro
        self.lograEntry = ttk.Entry(self.container)
        self.lograEntry.config(font=("Arial", 14), width=30)

        self.consultar_button = tk.Button(self.container, text="Consultar o CEP", command=self.consultar)
        self.consultar_button.config(font=("Verdana", 16), foreground="blue")

        self.resultado_label = ttk.Label(self.container, text="")
        self.resultado_label.config(font=("Comic Sans ms", 16), foreground="green")

        self.titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.uf.grid(row=1, column=0, padx=10, pady=10)
        self.ufEntry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        self.muni.grid(row=2, column=0, padx=10, pady=10)
        self.muniEntry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        self.logra.grid(row=3, column=0, padx=10, pady=10)
        self.lograEntry.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

        self.consultar_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.resultado_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def consultar(self):
        uf = self.ufEntry.get()
        muni = self.muniEntry.get()
        logra = self.lograEntry.get()
        retorno = ""

        if uf and muni and logra:
            uf = uf.upper()
            muni = muni.replace(" ", "%20")
            logra = logra.replace(" ", "%20")

            response = requests.get(f'https://viacep.com.br/ws/{uf}/{muni}/{logra}/json/')
            endereco = json.loads(response.text)

            if isinstance(endereco, list) and endereco:
                endereco = endereco[0]
                if "erro" in endereco:
                    retorno = "CEP não encontrado!"
                else:
                    retorno = f'''
CEP: {endereco['cep']}
Logradouro: {endereco['logradouro']}
Complemento: {endereco['complemento']}
Bairro: {endereco['bairro']}
Localidade: {endereco['localidade']}
UF: {endereco['uf']}
DDD: {endereco['ddd']}
'''
            else:
                retorno = "CEP não encontrado!"

        self.resultado_label.config(text=retorno)


def main():
    raiz = tk.Tk()
    raiz.title("Consulta CEP")
    apl = Container(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    main()
