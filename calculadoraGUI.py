from tkinter import *


class Container:
   def __init__(self, parent):
       self.myParent = parent
       self.container = Frame(parent)
       self.container.pack()

       self.primeiro_numero_label = Label(self.container, text="Digite o primeiro número:")
       self.primeiro_numero_label.config(font=("Arial", 14, "normal", "normal"))
       self.primeiro_numero_entry = Entry(self.container)
       self.primeiro_numero_entry.config(font=("Arial", 14,"bold", "bold"))

       self.segundo_numero_label = Label(self.container, text="Digite o segundo número:")
       self.segundo_numero_label.config(font=("Arial", 14, "normal", "normal"))
       self.segundo_numero_entry = Entry(self.container)
       self.segundo_numero_entry.config(font=("Arial", 14, "bold", "bold"))

       self.somar_button = Button(self.container, text="Somar", command=self.somar)
       self.somar_button.config(font=("Verdana", 16, "normal", "normal"), foreground="blue")

       self.sub_button = Button(self.container, text="Subtrair", command=self.sub)
       self.sub_button.config(font=("Verdana", 16, "normal", "normal"), foreground="blue")

       self.multi_button = Button(self.container, text="Multiplicar", command=self.multi)
       self.multi_button.config(font=("Verdana", 16, "normal", "normal"), foreground="blue")

       self.div_button = Button(self.container, text="Dividir", command=self.div)
       self.div_button.config(font=("Verdana", 16, "normal", "normal"), foreground="blue")
       self.resultado_label = Label(self.container, text="")
       self.resultado_label.config(font=("Arial", 16, "normal", "normal"), foreground="green")

       self.primeiro_numero_label.grid(row=0, column=0, padx=10, pady=10)
       self.primeiro_numero_entry.grid(row=0, column=1, padx=10, pady=10)

       self.segundo_numero_label.grid(row=1, column=0, padx=10, pady=10)
       self.segundo_numero_entry.grid(row=1, column=1, padx=10, pady=10)

       self.somar_button.grid(row=2, column=0, padx=10, pady=10)
       self.sub_button.grid(row=3, column=0, padx=10, pady=10)
       self.multi_button.grid(row=2, column=1, padx=10, pady=10)
       self.div_button.grid(row=3, column=1, padx=10, pady=10)
       self.resultado_label.grid(row=2, column=3, padx=10, pady=10)

   def somar(self):
       primeiro_numero = int(self.primeiro_numero_entry.get())
       segundo_numero = int(self.segundo_numero_entry.get())
       soma = primeiro_numero + segundo_numero
       self.resultado_label.config(text=f"A soma é {soma}")

   def sub(self):
       primeiro_numero = int(self.primeiro_numero_entry.get())
       segundo_numero = int(self.segundo_numero_entry.get())
       sub = primeiro_numero - segundo_numero
       self.resultado_label.config(text=f"A diferença é {sub}")

   def multi(self):
       primeiro_numero = int(self.primeiro_numero_entry.get())
       segundo_numero = int(self.segundo_numero_entry.get())
       multi = primeiro_numero * segundo_numero
       self.resultado_label.config(text=f"A multiplicação é {multi}")

   def div(self):
       primeiro_numero = int(self.primeiro_numero_entry.get())
       segundo_numero = int(self.segundo_numero_entry.get())
       div = primeiro_numero / segundo_numero
       self.resultado_label.config(text=f"A divisão é {div}")

def main():
   raiz = Tk()
   raiz.title("Calculadora")
   apl = Container(raiz)
   raiz.mainloop()

if __name__ == "__main__":
   main()
