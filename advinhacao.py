import random

print("|----------------------------|")
print("|     Jogo da advinhação     |")
print("|----------------------------|")
x = 0
while x == 0:
    numTentativas = 0
    rand_num = random.randint(0, 100)

    while x == 0:
        tentativa = int(input("\nDigite um número: "))
        numTentativas += 1

        if tentativa == rand_num:
            numTentativas += 1
            print("Acertou!\n")
            print(f"O número era: {rand_num}")
            print(f"Número de tentativas: {numTentativas}")

            print("Deseja jogar novamente? ")
            print("|---------------------|")
            print("|       1-Sim         |")
            print("|       2-Não         |")
            print("|---------------------|")
            opcao = int(input())
            if opcao == 1:
                break
            else:
                print("Programa encerrado!")
                x = 1
        else:
            if tentativa < rand_num:
                print(f"Número é maior que {tentativa}")
            elif tentativa > rand_num:
                print(f"Número é menor que {tentativa}")


