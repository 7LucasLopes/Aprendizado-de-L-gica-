import os 
os.system("cls")

while True:
    perguntas = [["Seu animal gosta de bananas? ", "macaco"]]

    print("Pense em um animal...")

    acertou = False
    for i in perguntas:
        resposta = input(f"{i[0]} (s/n): ")
        if resposta.lower() == "s":
            print(f"Você pensou em {i[1]}!")
            acertou = True
            break
    

    if not acertou:
        animal = input("Desisto! Em qual animal você pensou? ")
        novapergunta = input("Para esse animal, qual pergunta você faria? ")
        perguntas.append(["novapergunta", "animal"])
    
    resposta = input("Quer jogar novamente? (s/n)")
    if resposta.lower() != "s":
        print("Ok! Foi bom jogar com você!")
        break
