'''numeros = [0,2,3,4,5,7]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# Exibe os números
for par in pares:
    print(par) '''

numeros = [0,2,3,4,5,7]
pares = filter(lambda valor: valor % 2 == 0, numeros)

for par in pares:
    print(par)