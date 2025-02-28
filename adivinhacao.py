import random

print("1 - nivel fácil")
print("2 - nivel médio")
print("3 - nivel dificíl")
opcao = int(input("Digite a opção desejada:"))
if (opcao == 1):
    print("Você escolheu fácil")
    numero_max = 10
    limite_tentativas = 5

elif (opcao == 2):
    print("Você escolheu médio")
    numero_max = 50
    limite_tentativas = 10

elif (opcao == 3):
    print("Você escolheu dificíl")
    numero_max = 100
    limite_tentativas = 10
else:
    print("Opção inválida")


sorteio = random.randint(1, numero_max)
#print(sorteio)
print("### JOGO DA ADIVINHAÇÃO ###")
print("Adivinhe o número que estou pensando, de 1 a",numero_max )
tentativa = 1
while (limite_tentativas >= tentativa):
    print("Tentativa", tentativa)
    chute = int(input("Digite o seu chute:"))
    if (chute == sorteio):
        print("Parabéns, você acertou!")
        break
    elif (chute > sorteio):
        print("Chute um número menor!")
    elif (chute < sorteio):
        print("Chute um número maior!")
    tentativa = tentativa + 1
    # FINAL DO LAÇO WHILE
print("O número sorteado era: ##", sorteio, "##")
print("### FIM DO JOGO ###")
