import adivinhacao
import forca

print("*********************************")
print("*******Escolha o seu jogo*******!")
print("*********************************")

jogo = int(input("(1) Adivinhação (2) Forca\n Qual o jogo?")) 

if(jogo == 1):
    print("Jagando Adivinhação")
    adivinhacao.jogar_adivinhacao()
elif(jogo == 2):
    print("Jogando Forca")
    forca.jogar_forca()