import random

CONST_MAXLINHAS = 3
MAX_APOSTA = 100
MIN_APOSTA = 1
LINHAS = 3
COLUNAS = 3

dic_simbolos = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def giros_maquina(linhas, colunas, simbolos):
    todos_simbolos = []

    for simbolo, num_simbolos in simbolos.items():
            for _ in range(num_simbolos):
                todos_simbolos.append(simbolo)

    matriz = []

    for _ in range(linhas):
        novaLinha = []
        cloneSimbolo = todos_simbolos[:]
        for _ in range(colunas):
            valor = random.choice(cloneSimbolo)
            cloneSimbolo.remove(valor)
            novaLinha.append(valor)
        matriz.append(novaLinha)

    return matriz

def print_maquina(matriz):
    for i in matriz:
        for j, valores in enumerate(i):
            if j != len(i) - 1:
                print(valores, end="| ")
            else:
                print(valores, end="")
        print()

def deposito():

    while True:
        amount = input("Digite a quantidade que deseja depositar: \nR$ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(f"Seu depósito deve ser maior que {amount}!")
        else:
            print("Digite um número válido!")
    print(f"Despósito realizado com o valor de R${amount}\n")
    return amount

def aposta_por_linha():
    while True:
        linhas = input("Digite a quantidade de linhas que deseja apostar(1 - " +  str(CONST_MAXLINHAS) + "): ")
        if linhas.isdigit():
            linhas = int(linhas)
            if linhas > 0:
                break
            else:
                print(f"Sua aposta deve ser maior que {linhas} linhas!")
        else:
            print("Digite uma aposta válida!")

    print(f"Quantidade de linhas registradas com sucesso!\n{linhas} linhas.\n")
    return linhas

def aposta(balanca, linha):
    while True:
        aposta = input("Digite a quantidade que deseja apostar por linha:\nR$ ")
        if aposta.isdigit():
            aposta = int(aposta)
            total = aposta * linha

            if aposta >= MIN_APOSTA and aposta <= MAX_APOSTA:
                if total <= balanca:
                    break
                else:
                    print(f"Saldo insuficiênte para realizar sua aposta!\nSeu saldo atual: R${balanca}")
            else:
                print(f"Sua aposta deve ser entre R${MIN_APOSTA} e R${MAX_APOSTA}")
        else:
            print("Digite uma aposta válida!")

    print(f"Aposta realizada com o valor de R${aposta}\n")
    return aposta

def main():
    balanca = deposito()
    linhas = aposta_por_linha()
    apostas = aposta(balanca, linhas)
    aposta_total = apostas * linhas
    valores_maquina = giros_maquina(LINHAS, COLUNAS, dic_simbolos)

    print(f"Você está apostando R${apostas} em {linhas} linhas!\nTotal apostado: R${aposta_total}")
    print(f"Saldo atual: R${balanca - aposta_total}")
    print_maquina(valores_maquina)


if __name__ == "__main__":
    main()

