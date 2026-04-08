import os
os.system("cls")

lista = None


def exibeLista(lista):
    if not lista:
        print("Lista vazia.")
        return
    elemento = lista

    while elemento != None:
        print(elemento['valor'], end=' ')
        elemento = elemento['proximo']
    
    print('.')

def adicionanoFim(elemento):
    global lista
    if not lista:
        lista = {'valor': elemento, 'proximo': None}
        return
    atual = lista
    while atual['proximo']:
        atual = atual['proximo']
    atual['proximo'] = {'valor': elemento, 'proximo': None}

print("Adicioando o 5...")
adicionanoFim(5)
print("Adicioando o 8...")
adicionanoFim(8)
print("Adicioando o 13...")
adicionanoFim(13)
exibeLista(lista)
