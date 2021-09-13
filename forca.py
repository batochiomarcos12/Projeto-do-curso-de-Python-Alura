import random  #rando gera números aleatórios (biblioteca)


def jogar():    # definindo minha função master

    mensagem_de_inicialização_jogo()
    palavra_secreta = carregando_a_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0



    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):  #se chute esta dentro da palavra.
         marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros +=1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor(palavra_secreta)

    else:
        imprime_mensagem_perdedor(palavra_secreta)


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor(palavra_secreta):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def pede_chute():
    chute = input('Qual é a letra ? ')
    chute = chute.strip().upper()  # strip elimina os espaços entre as letras upper letra maiscula
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):  # independente se o usário didtar maíscula ou miniscula, será maiscula.
            letras_acertadas[index] = letra
        index += 1

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]


def mensagem_de_inicialização_jogo():
    print('*' * 33)
    print('***Bem vindo! Ao jogo da forca***')  # tela de exibiçaõ
    print('*' * 33)

def carregando_a_palavra_secreta():
    arquivo = open("frutas.txt", "r")  # importando arquivo esterno (abrindo)
    frutas = []

    for linha in arquivo:  # para linha dentro de arquivo (Buscar a palavra aleatoria )
        linha = linha.strip()
        frutas.append(linha)

    arquivo.close()  # fechando arquivo esterno

    numero = random.randrange(0, len(frutas))  # seleciona palavras aleatórias dentro da lista.
    palavra_secreta = frutas[numero].upper()
    return palavra_secreta



if(__name__ =="__main__"):
    jogar()