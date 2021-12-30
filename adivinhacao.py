print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3

for rodada in range(1, total_tentativas+1):
    chute = int(input("Tentativa: {0} de {1}.\nDigite um numero entre 1 e 100: ".format(rodada, total_tentativas)))
    print("Você digitou ", chute)
    if(chute < 1 or chute >100):
        print("Você deve digitar um numero entre 1 e 100!")
        continue
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Parabéns!! Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim do jogo")