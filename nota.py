import os 
os.system("cls")

print("Vamos avaliar a sua nota para ver se você foi aprovado!")
print()
NotaAluno = float(input("Qual foi a sua nota?"))

if NotaAluno > 7:
    print("Você foi aprovado7!!! ")
else:
    if NotaAluno < 5:
     print("Você foi reprovado!")
    else:
       print("Você está de recuperação!")
