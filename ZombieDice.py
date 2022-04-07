# Leonardo Martins Ribeiro
# Análise e Desenvolvimento de Sistemas

import time
import random
#import numpy as np ### ambos imports para trocar o random
#import secrets

#######################################################
# REGRAS                                              #
# O jogador deve comer 13 cérebros para ganhar o jogo #
#                                                     #
# DADOS                                               #
# 13 DADOS DE 6 FACES                                 #
# 6 VERDES, 4 AMARELOS E 3 VERMELHOS                  #
# 2 TIROS, 2 CÉREBROS E 2 PASSOS                      #
#######################################################
                                                     
###############################################################################################

# DECLARAÇÃO DAS PRINCIPAIS VARIÁVEIS:

#dadoVerde = "CPCTPC" # Constante contendo Faces do dado verde
dadoVerde = ('C', 'P', 'C', 'T', 'P', 'C')
#dadoAmarelo = "TPTCPT" # Constante contendo Faces do dado amarelo
dadoAmarelo = ('T', 'P', 'T', 'C', 'P', 'T')
#dadoVermelho = "TPTCPT" # Constante contendo Faces do dado vermelho
dadoVermelho = ('T', 'P', 'T', 'C', 'P', 'T')
jogadorAtual = 0
nrojogadores = 0
dadosSorteados = []
jogadores = []
tiros = 0
passos = 0
cerebros = 0

def copoDados():
    global listaDados, listaDados_original
    listaDados = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoAmarelo, 
                    dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoVermelho, dadoVermelho, dadoVermelho]
    listaDados_original = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoAmarelo, 
                            dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoVermelho, dadoVermelho, dadoVermelho]
copoDados()
###############################################################################################

print ("\n")
print("Para se jogar Zombie Dice é necessário a presença de 2 jogadores!")
print ("\n")
time.sleep(0.5)

# REPETIÇÃO PARA ENQUANTO A QUANTIDADE FOR MENOR QUE 2, AVISAR JOGADOR E PEDIR INPUT NOVAMENTE.

while nrojogadores < 2:
    nrojogadores = int(input("Insira o número de jogadores: "))
    if nrojogadores < 2:
        print("É necessário 2 jogadores")
# Para cada jogador baseado na quantia inserida no input anterior
# Input para atribuir um identificador para cada jogador
for i in range(nrojogadores):
    jogador = input("Insira o nome do Jogador " + str(i + 1) + ": ");
    jogadores.append({"Nome": jogador, "Cérebros": cerebros}) # Adiciona os jogadores do input na lista

time.sleep(0.5)
print('\n')

print("#################### INICIANDO O JOGO! ####################")
print('\n')
time.sleep(0.35)
print("Dados no Copo: ")
print("\n")
time.sleep(0.35)
print(listaDados)
time.sleep(0.35)
print("\n")
print(jogadores) # Para teste, mostra lista de jogadores

time.sleep(0.5)
# ESTRUTURA DE REPETIÇÃO CONTENDO O JOGO
while True:

    time.sleep(1)
        
    # DENTRO DA REPETIÇÃO:

    # para cada vez, o jogador da vez pega 3 dados dos 13 disponíveis
    # FUNÇÃO PARA RANDOMIZAR E "JOGAR" 3 TIPOS DE DADOS
    # FUNÇÃO PARA RANDOMIZAR A "FACE" DOS 3 DADOS
    # se a face randomizada for cerebro, o jogador come um cerebro
    # se a face randomizada for tiro, o jogador recebe um tiro
    # se a face randomizada for passo, a vítima escapa
    # se o jogador escolher continuar a jogar

    print("\n")

    print("Turno atual é do jogador: ", jogadores[jogadorAtual])

    time.sleep(0.5)
    
    print("\n")
    
    for i in range(0, 3):
        def sorteioDados():
            valorSorteado = random.randint(0, len(listaDados) - 1) # Int Random
            dadoSorteado = listaDados[valorSorteado] # Utiliza o valor do Int Random para buscar um valor na lista de dados
            
            print(dadoSorteado)
            
            time.sleep(0.7)

            # CONDICIONAIS PARA ATRIBUIR VALOR DE FACES PARA OS DADOS SELECIONADOS ANTERIORMENTE
            def sorteioCorDados():
                if (dadoSorteado == dadoVerde):
                    corDado = "VERDE"
                elif (dadoSorteado == dadoAmarelo):
                    corDado = "AMARELO"
                else:
                    corDado = "VERMELHO"
                print("Dado Sorteado é: " + corDado)
                return corDado
            sorteioCorDados()
            
            ####################################################################################

            time.sleep(0.5)

            print("\n")

            def DadosLista():
                dadosSorteados.append(dadoSorteado)
                listaDados.remove(dadoSorteado)
                time.sleep(0.6)
                print("Dados no Copo: ")
                print("\n")
                time.sleep(0.6)
                print(listaDados)
            DadosLista()

            print("\n")

            time.sleep(0.7)
            return valorSorteado, dadoSorteado
        sorteioDados()
    
    # REPETIÇÃO PARA CONDICIONAIS/
    # PARA CADA DADO, ATRIBUI UM VALOR RANDOMICO PARA SELECIONAR UMA FACE
    # E ATRIBUI O VALOR DA FACE PARA O SIMPLES CONTADOR

    def sorteioFaceDados():
        global cerebros, tiros, passos
        for dadoSorteado in dadosSorteados:
            nroFaces = random.randint(0, 5) # Atribui um int para escolher a face
            # Condicional para pegar a face correta utilizando o int randomizado
            if dadoSorteado[nroFaces] == "C": # Se o valor randomizado cair na face "C"
                cerebros = cerebros + 1 # Atualiza o Contador
                print("Você comeu cérebro!".format(cerebros))
                time.sleep(0.8)    
            elif dadoSorteado[nroFaces] == "T": # Se o valor randomizado cair na face "T"
                tiros = tiros + 1 # Atualiza o Contador
                print("Você levou tiro!".format(tiros))
                time.sleep(0.8)
            else: # Caso não seja nenhum dos últimos casos então caiu "P"
                passos = passos + 1 # Atualiza o Contador
                print("Vítima escapou!")
        return nroFaces
    sorteioFaceDados()

    #######################################################################

    def score():
        time.sleep(0.5)
        print("\n")
        print("########## PONTUAÇÂO ATUAL ##########")
        print("\n")

        time.sleep(0.5)
        print("CÉREBROS: {}".format(cerebros)) # UTILIZA VALOR DO CONTADOR ATUALIZADO ANTERIORMENTE PARA O PLACAR
        time.sleep(0.5)
        print("TIROS: {}".format(tiros)) # UTILIZA VALOR DO CONTADOR ATUALIZADO ANTERIORMENTE PARA O PLACAR

        time.sleep(0.5)

        print("\n")
    score()

    # Escolha do jogador, rolar dados novamente ou passar para o próximo.
    continuarTurno = input("Você deseja rolar os dados novamente? Não para passar os dados para o próximo jogador (s = sim | n = não): ")

    print("\n")

    time.sleep(0.5)

    # Condicional para caso a escolha do input seja não,
    # Ele reseta o valor do contador de placar e roda para o próximo jogador.
    def fimTurno():
        global jogadorAtual, nrojogadores, dadosSorteados, listaDados, listaDados_original, tiros, cerebros, passos
        global jogadorAtual
        if continuarTurno == 'n':
            jogadorAtual = jogadorAtual + 1
            dadosSorteados = []
            listaDados = listaDados_original
            tiros = 0
            cerebros = 0
            passos = 0
            # Se o jogador atual for o mesmo que a quantia de jogador
            # Para o funcionamento do código, pois é o último jogador
            if jogadorAtual == nrojogadores:
                print("FIM DE JOGO!")
                print("SCORE FINAL: {}".format(jogadores))
                quit
        # Condicional Else para caso a resposta seja sim
        # Rodar o jogo novamente para o mesmo jogador.
        else:
            print("Rolando os dados novamente...")
            dadosSorteados = [] # Limpa a lista contendo dados sorteados
        return dadosSorteados, listaDados, tiros, cerebros, passos
    fimTurno()        