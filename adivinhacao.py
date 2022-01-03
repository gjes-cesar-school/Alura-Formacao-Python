import random

def jogar_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    print(numero_secreto)
    total_tentativas = 3
    pontos  = 1000

    nivel = int(input("Digite o nivel dificuldade:\n(1)Fácil (2)Médio (3)Difícil\n"))
    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

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
            print("Parabéns!! Você acertou!\nTotal de pontos {0}".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if (rodada == total_tentativas):
                        print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_tentativas):
                        print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            pontos = pontos - abs(numero_secreto - chute)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar_adivinhacao()