# Utilizando alguma estrutura de loop, imprima todos os número de 0 até 100;

from random import randint
for i in range(0, 100):
    print(i)

# Modifique o código do item anterior para imprimir apenas os números pares. Note que o resto da divisão de um número par por 2 é igual a zero, algo que o operador modulo “%” pode te retornar;
for i in range(0, 100, 2):
    print(i)

# criar uma lista com 100 números aleatórios:
lista = [randint(1, 100) for _ in range(100)]

# Com um loop for, imprima:

# Todos os números da lista;

for numeros in lista:
    print(numeros)


# Todos os números maiores que 10 da lista;

for numeros in lista:
    if numeros > 10:
        print(numeros)

# Todos os números maiores que 10 e menores que 30 da lista;

for numeros in lista:
    if numeros > 10 and numeros < 30:
        print(numeros)

# O dobro de todos os números que forem menores que 50

for numeros in lista:
    if numeros < 50:
       print(numeros*2)

# Utilizando de um loop while, conte:

# Quantos números ímpares possui a lista;


# Quantos números maiores que 50;

contagem = 0
while True:
     contagem += 1
     lista = randint(0, 100)
     if lista < 50:
           print(f"Tem {contagem} números maiores que 50")
           break
