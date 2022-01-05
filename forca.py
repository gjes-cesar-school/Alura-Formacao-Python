import random
import unidecode

def imprimir_titulo():
    print("*********************************")
    print("***Bem vindo ao jogo de forca***!")
    print("*********************************")

def escolha_palavra_secreta():
    arquivo = open("frutas.txt","r")
    frutas = []
    for linha in arquivo:
        frutas.append(linha.strip())
    arquivo.close()
    palavra_secreta =  unidecode.unidecode(frutas[random.randrange(0,len(frutas))].upper()) 
    print(palavra_secreta) 
    return palavra_secreta

def mostrar_quantidade_letras(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def solicitar_chute():
    return input("Qual a letra? ").strip().upper()

def mostrar_letras_acertadas(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1
    return letras_acertadas

def ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________ ")
    print("      '._==_==_=_.' ")
    print("      .-\\:       /-. ")
    print("     | (|:.       |) | ")
    print("      '-|:.       |-' ")
    print("        \\::.    / ")
    print("         '::.  .' ")
    print("           ) ( ")
    print("         _.' '._ ")
    print("        '-------' ")

def perdeu(palavra_secreta):
    print("Você perdeu, a palavra secreta era {0}, tente novamente.".format(palavra_secreta))
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________ ")
    print("   /               \ ")
    print("  /                 \ ")
    print("//                   \/\ ")
    print("\|   XXXX      XXXX  | / ")
    print(" |   XXXX       XXXX |/ ")
    print(" |   XXX         XXX | ")
    print(" |                   | ")
    print(" \__      XXX      __/ ")
    print("   |\     XXX     /| ")
    print("   | |           | | ")
    print("   | I I I I I I I |")
    print("   |  I I I I I I  | ")
    print("   \_             _/ ")
    print("     \_         _/ ")
    print("       \_______/ ")

def desenha_forca(erros):
    print("Ops, você errou! Faltam {} tentativas".format(7-erros))
    print(" _______   ")
    print(" |/ |      ")
    if(erros == 1):
        print(" | (_) ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
    if(erros == 2):
        print(" | (_) ")
        print(" | \   ")
        print(" |     ")
        print(" |     ")
    if(erros == 3):
        print(" | (_) ")
        print(" | \|  ")
        print(" |     ")
        print(" |     ")
    if(erros == 4):
        print(" | (_) ")
        print(" | \|/ ")
        print(" |     ")
        print(" |     ")
    if(erros == 5):
        print(" | (_) ")
        print(" | \|/ ")
        print(" |  |  ")
        print(" |     ")
    if(erros == 6):
        print(" | (_) ")
        print(" | \|/ ")
        print(" |  |  ")
        print(" | /   ")
    if (erros == 7):
        print(" | (_) ")
        print(" | \|/ ")
        print(" |  |  ")
        print(" | / \ ")
        print(" |     ")
        print("_|___  ")
        print()

def jogar_forca():
    imprimir_titulo()
    palavra_secreta = escolha_palavra_secreta()
    letras_acertadas = mostrar_quantidade_letras(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = solicitar_chute()
        if(chute in palavra_secreta):
            letras_acertadas =  mostrar_letras_acertadas(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
            
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        ganhou()
    else:
        perdeu(palavra_secreta)
        
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar_forca()