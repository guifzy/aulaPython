s = input('Qual o texto? ')

t = len(s)
lista = []
for ind in range(256):
   lista.append(0)

print(lista)

for ind in range(t):
   cod = ord(s[ind])
   lista[cod] += 1

print(lista)

for ind in range(256):
   if lista[ind] > 0:
       porc = (lista[ind] * 100) / t
       print (chr(ind), porc, '%')