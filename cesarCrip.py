frase = input("Digite uma frase: ")
output = ""

for i in frase:
    code = ord(i)
    code += 2
    output += chr(code)

print("Sua frase criptografada: {}".format(output))
