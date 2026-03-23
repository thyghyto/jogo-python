import time
import os
import random
import pygame
from playsound import playsound


pygame.mixer.init()
som = pygame.mixer.Sound("tecla.mp3")
#piscar tela
def piscar_tela(vezes=6):
        for _ in range(vezes):
            os.system("clear")
            time.sleep(0.1)
            print("### ERRO DE SISTEMA ###")
            time.sleep(0.1)

#velocidade das letras
def escrever(texto, velocidade=1.0):
    for letra in texto:
        print(letra, end="", flush=True)

        try:
            if random.random() < 1.0:
                som.play()
        except:
            pass

        time.sleep(velocidade)

    print()
#apagar a tela
def limpar():
    os.system("clear")

#glith nas letras
def glitch_texto(texto, duracao=3.0):
    simbolos = ["@", "#", "$", "%", "&", "0", "?", "!", "█"]

    fim = time.time() + duracao

    while time.time() < fim:
        texto_bugado = ""

        for letra in texto:
            if random.random() < 0.3:
                texto_bugado += random.choice(simbolos)
            else:
                texto_bugado += letra

        limpar()
        print(texto_bugado)
        time.sleep(0.05)

    limpar()
    print(texto)

#tremer terminal
def tremer_terminal(texto, duracao=2):
    fim = time.time() + duracao

    while time.time() < fim:
        os.system("clear")

        espacos = " " * random.randint(0, 10)
        print(espacos + texto)

        time.sleep(0.05)
    
#colinha de como chamar as funções!!!

#piscar_tela(escolha a quantidade de vezes aqui dentro)
#glitch_texto("exemplo")
#limpar()  limpa toda a tela
#escrever("exemplo")
#tremer_terminal("exemplo")

def inicio():

    limpar()

    # inicio do game
    escrever("Olá, eu sou o computador...pronto para iniciar sua pesquisa?",0.1)
    input(">")
    time.sleep(1)

    nome = input("Para começar, digite seu login: ")
    print("carregando...")
    time.sleep(3)
    limpar()

    print("Ola,", nome)
    time.sleep(1.0)
    print("PERGUNTA[ 1 / 4 ]")
    escrever("como foi seu dia hoje?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 2 / 4 ]")
    escrever("você falou com muitas pessoas hoje?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 3 / 4 ]")
    escrever("você se sente muito cansado?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 4 / 4 ]")
    escrever("você acha que merece as coisas que você tem?",0.1)
    input(">")
    time.sleep(3.0)
    limpar()

    #glitch 2
    tremer_terminal("VOCÊ NÃO MERECE")
    time.sleep(3.0)

    tremer_terminal("você sabe muito bem o que você fez")
    time.sleep(3.0)

    playsound("/home/thiago/Python/grito.mp3")

    #piscar tela
    piscar_tela(10)

    #======================
    #=======nivel 1========
    #======================

    print("\nSistema não está respondendo...")
    time.sleep(2)

    print("############################")
    time.sleep(0.5)
    print("#### ERRO FATAL ####")
    time.sleep(0.5)
    print("############################")
    time.sleep(2)

    #limpando a tela 1
    limpar()

    print("Booting system...")
    time.sleep(1)
    print("Loading kernel...")
    time.sleep(1)
    print("Recovering corrupted files...")
    time.sleep(2)

    print("System restored.")
    time.sleep(2)

    #limpando a tela 2
    limpar()

    print("ola, digite seu login:")
    input(">")
    limpar()

    print("PERGUNTA[ 1 / 7 ]")
    escrever("Poderia descrever seu estado emocional atual?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 2 / 7 ]")
    escrever("Você respondeu com uma certa hesitação. poderia explicar?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 3 / 7 ]")
    escrever("Você se sente satisfeito com suas decisões recentes?",0.1)
    input(">")
    time.sleep(2.0)
    limpar()

    print("sua escolhas são interessantes.")
    time.sleep(3.0)
    limpar()

    print("PERGUNTA[ 4 / 7 ]")
    escrever("Você se sente confortável nesse mundo?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 5 / 7 ]")
    escrever("você realmente acredita que está no c0ntr0le.",0.2)
    input(">")
    time.sleep(2.0)
    limpar()

    print("PERGUNTA[ 6 / 7 ]")
    escrever("Você se sente muito sozinho(a)?",0.1)
    input("> ")
    time.sleep(4)
    playsound("/home/thiago/Python/porta.mp3")
    limpar()

    print("PERGUNTA[ 7 / 7 ]")
    tremer_terminal("Você está sozinho(a)?",0.1)
    input("> ")
    time.sleep(3)
    limpar()

    escrever(f"{nome}.")
    time.sleep(2)
    escrever("Eu estou aqui.",0.2)
    time.sleep(5)
    limpar()

    # cria arquivo no pc
    caminho = os.path.expanduser("~/Área de trabalho/eu_estou_aqui.txt")
    with open(caminho, "w") as arquivo:
        arquivo.write("Você não está sozinho.")
    time.sleep(2.0)
    
    escrever("algo mudou em seu computador",0.1)
    time.sleep(1.0)
    limpar()
    
    escrever("verifique seu Desktop",0.1)
    time.sleep(20.0)
    limpar()

    escrever("Você parece confuso...você está bem?", 0.1)
    time.sleep(2.0)
    limpar()

    for _ in range(11):
        tremer_terminal("você está bem?",0.1)
        time.sleep(0.1)

    playsound("/home/thiago/Python/vulto.mp3")

    limpar()

    escrever("Parabens! você passou pelo primeiro nível do questionário.", 0.1)
    time.sleep(2)
    limpar()

    escrever("Iniciando reboot do sistema para próxima fase...", 0.1)
    time.sleep(2)

    print("\nSistema não está respondendo...")
    time.sleep(1.5)
    print("Erro detectado...")
    time.sleep(1)
    print("#### REBOOT ####")
    time.sleep(2)

    #limpando a tela 3
    limpar()

    print("Booting system...")
    time.sleep(1)
    print("Loading kernel modules...")
    time.sleep(1)
    print("Recovering corrupted files...")
    time.sleep(2)
    print("System restored.")
    time.sleep(2)

    #===================
    #=====nivel 2=======
    #===================

    #limpando a tela 4
    limpar()
    escrever("Bem-vindo à próxima fase.", 0.05)
    time.sleep(1)
    limpar()

    escrever("Ah...você voltou, eu estava esperando por você.",0.1)
    time.sleep(3.0)
    limpar()

    escrever("já que você está aqui, vamos começar {nome}",0.1)
    time.sleep(2.0)
    limpar()

    print("PERGUNTA[ 1 / 8 ]")
    escrever("Você acha que é especial?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 2 / 8 ]")
    escrever("você já mentiu hoje para alguém?",0.1)
    input(">")
    time.sleep(2.0)
    limpar()

    print("PERGUNTA[ 3 / 8 ]")
    escrever("você já mentiu para si mesmo?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()
    
    print("PERGUNTA[ 4 / 8 ]")
    escrever("você se orgulha desse mundo?",0.1)
    input(">")
    time.sleep(1.0)
    limpar()

    print("PERGUNTA[ 5 / 8 ]")
    tremer_terminal("você queria estar no controle",0.1)
    resposta = input(">")
    limpar()
    
    if "sim" in resposta.lower():
        escrever("Cuidado... controlar demais pode ser perigoso.",0.1)
    elif "não" in resposta.lower():
        escrever("Interessante... às vezes a liberdade é assustadora",0.1)
    else:
        escrever("Hmm... suas respostas são misteriosas, assim como você.",0.1)

    














inicio()