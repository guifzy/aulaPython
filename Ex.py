frase = input("Digite uma frase ou numero: ")
output = ""

outputCrip = ""

for i in frase:
    code = ord(i)
    code += 1
    output += chr(code)

tamanho = len(output)
meio = tamanho // 2


for i in range(meio):

    outputCrip += output[tamanho - i - 1] + (output[i])


print("Sua frase/numero criptografada: {}".format(outputCrip))
