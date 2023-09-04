codigo_criptografado = input("Digite o código criptografado: ")
tamanhoC = len(codigo_criptografado)
meioC= tamanhoC // 2

parte1 = codigo_criptografado[meioC:]
parte2 = codigo_criptografado[:meioC]

frase_descriptografada = ""

for i in range(meioC):
    char1 = parte1[i]
    char2 = parte2[tamanhoC - i - 1]

    code1 = ord(char1)
    code2 = ord(char2)

    code1 -= 1
    code2 -= 1

    frase_descriptografada += chr(code2) + chr(code1)

if tamanhoC % 2 != 0:
    meio_char = codigo_criptografado[meioC]
    code_meio = ord(meio_char)
    code_meio -= 1
    frase_descriptografada += chr(code_meio)

print("Sua frase descriptografada: {}".format(frase_descriptografada))
