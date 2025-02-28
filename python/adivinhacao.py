import random
sorteio = random.randint(1,10)
print(sorteio)
print("### JOGO DA ADIVINHAÇÃO ###")
print("Adivinhe o número que estou pensando, de 1 a 10")
limite_tentativas = 3
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