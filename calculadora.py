print("Calculadora em Pyhton\n")
operador = input("Escolha um operador para realizar a operação(+ - * /)")
num1 = input("Digite o primeiro número: ")
num1 = int(num1)
num2 = input("Digite o segundo número: ")
num2 = int(num2)
resultado = 0

if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '/':
    resultado = num1 / num2
else:
    resultado = num1 * num2

print(f"Resultado {resultado}")