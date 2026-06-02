"""Nesse arquivo foi trabalhado o conceito de código limpo, por isso os uso de comentários."""
import os
os.system("cls")

""" Essa é a lista"""

numeros = []

"""Essa loop é para o usuário digitar os números"""

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

"""Essa função é para definir o maior número"""

def maior_numero(numeros):
    maior = numeros[0]
    for number in numeros:
        if number > maior:
            maior = number
    return maior

"""Essa função é para definir o menor número"""

def menor_numero(numeros):
    menor = numeros[0]
    for i in numeros:
        if i < menor:
            menor = i
    return menor

"""Essa é uam função para soma """

def soma_total(numeros):
    total = 0
    for i in numeros:
        total += i
    return total


"""Essa função é para definir a média dos números"""

def media_numeros(numeros):
    media = soma_total(numeros) / len(numeros)
    return media

print()

"""Essa parte é para exibir as repostas"""
print(f"Esse é o maior número: {maior_numero(numeros)}")
print(f"Esse é o menor número: {menor_numero(numeros)}")
print(f"Essa é a média: {media_numeros(numeros):.2f}")
print(f"Essa é a soma total dos números: {soma_total(numeros)}")
