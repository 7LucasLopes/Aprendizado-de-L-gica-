import os
os.system("cls")

"""Essa é a lista"""
numeros = []

"""Esse é uma repetição"""
while True:
    entrada = input("Digite um número: ").lower()

    if entrada == 'sair':
        break

    try:
        numero = int(entrada)
        numeros.append(numero)
    except:
        print("Digite um número válido!")

"""Essa função defini o maior número da lista"""
def maior_numero(numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

"""Essa função defini o menor número da lista"""
def menor_numero(numeros):
    menor = numeros[0]
    for i in numeros:
        if i < menor:
            menor = i
    return menor

"""Essa função defini a soma total dos números da lista"""
def soma_numeros(numeros):
    soma = 0
    for i in numeros:
        soma += i
    return soma

"""Essa função defini a média dos números da lista"""
def media_numeros(numeros):
    media = soma_numeros(numeros) / len(numeros)
    return media

"""Esses são os resultados"""
print(f"O maior número é o : {maior_numero(numeros)}")
print(f"O menor número é o : {menor_numero(numeros)}")
print(f"A soma de todos os números é: {soma_numeros(numeros)}")
print(f"A média dos núemros é: {media_numeros(numeros)}")