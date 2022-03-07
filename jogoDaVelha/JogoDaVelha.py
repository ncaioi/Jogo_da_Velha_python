import os
import random

jogarNovamente="s"
jogadas=0
quemJoga=2
maxJogadas=9
vit="n"
velha=[
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + str(jogadas))

def jogadorJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga==2 and jogadas<maxJogadas:
        l=int(input("Linha: "))
        c=int(input("Coluna: "))
        try:
            while velha[l][c]!= " ":
                l=int(input("Linha: "))
                c=int(input("Coluna: "))
            velha[l][c]="X"
            quemJoga=1
            jogadas+=1
        except:
            print("Linha e/ou coluna invalida: ")

def cpuJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga==1 and jogadas<maxJogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha[l][c]!=" ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        velha[l][c]="O"
        jogadas+=1
        quemJoga=2

def verificarVitoria():
    global velha
    vitoria="n"
    simbolos=["X","O"]
    for s in simbolos:
        vitoria="n"
        #verificar linhas
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(velha[il][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):
                vitoria=s
                break
            il+=1
        if(vitoria!="n"):
            break
        #Verificar colunas
        il=ic=0
        while ic<3:
            soma=0
            il=0
            while il<3:
                if(velha[il][ic]==s):
                    soma+=1
                il+=1
            if(soma==3):
                vitoria=s
                break
            ic+=1
        if(vitoria!="n"):
            break
        #Verifica diagonal 1
        soma=0
        digl=0
        digc=0
        while digl<3:
            if(velha[digl][digc]==s):
                soma+=1
            digl+=1
            digc+=1
            if(soma==3):
                vitoria=s
                break
        if(vitoria!="n"):
            break
        #Verifica diagonal 2
        soma=0
        digl=0
        digc=2
        while digc>=0:
            if(velha[digl][digc]==s):
                soma+=1
            digl+=1
            digc-=1
            if(soma==3):
                vitoria=s
                break
        if(vitoria!="n"):
            break
    
    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas=0
    quemJoga=2
    maxJogadas=9
    vit="n"
    velha=[
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


while(jogarNovamente=="s"):
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit=verificarVitoria()
        if(vit!="n") or (jogadas>=maxJogadas):
            break

    print("FIM DE JOGO")
    if(vit=="X" or vit=="O"):
        print("Resultado: Jogador " + vit + " venceu")
    else:
        print("Resultado: Empate")
    
    jogarNovamente=input("Deseja jogar novamente[s/n]: ")
    redefinir()
