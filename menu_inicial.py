import adivinhação
import forca

print("escolha o jogo desejado:")
print("1 - adivinhação")
print("2 - forca")

opcao = int(input("digite o número do jogo desejado:"))

if opcao == 1:
    print("Executando adivinhção...")
    adivinhação.jogar()
elif opcao == 2:
    print("Executando forca...") 
else:
    print("Executando adivinhação") 
    adivinhação.jogar()

    