import random as r
import os

TAMANHO = 10
TURN = 'c1'

locObjetivo = []
locC1 = []
locC2 = []
locPoderes1 = []
locPoderes2 = []

def gerar_tabuleiro():
    return [[0 for _ in range(TAMANHO)] for _ in range(TAMANHO)]

def set_caracter(matriz, letra):
    # setado pra gerar os carros e o objetivo
    if letra == 'C1':
        x = 9
        y = 0
        if matriz[x][y] == 0:
            matriz[x][y] = letra
            return [x, y]
    
    if letra == 'C2':
        x = 9
        y = 9
        if matriz[x][y] == 0:
            matriz[x][y] = letra
            return [x, y]
        
    if letra == 'OO':
        x = 0
        y = r.randrange(TAMANHO)
        if matriz[x][y] == 0:
            matriz[x][y] = letra
            return [x, y]
    
    #gerar poderes sem conflitar com nada
    while True:
        x = r.randrange(TAMANHO)
        y = r.randrange(TAMANHO)
        if matriz[x][y] == 0:
            matriz[x][y] = letra
            return [x, y]

def gerar_c1(matriz):
    global locC1
    locC1 = set_caracter(matriz, "C1")
    
def gerar_c2(matriz):
    global locC2
    locC2 = set_caracter(matriz, "C2")    
    
def gerar_objetivo(matriz):
    global locObjetivo
    locObjetivo = set_caracter(matriz, "OO")    

def gerar_poderes(matriz):
    global locPoderes1, locPoderes2
    locPoderes1 = []
    locPoderes2 = []

    for _ in range(3):
        pos = set_caracter(matriz, "P1")
        locPoderes1.append(pos)
    for _ in range(3):
        pos = set_caracter(matriz, "P2")
        locPoderes2.append(pos)

def imprimir_tabuleiro(matriz):
    print("\n----- TABULEIRO DO JOGO -----")
    for linha in matriz:
        linha_formatada = " ".join(str(celula) if celula != 0 else ".." for celula in linha)
        print(linha_formatada)
    print("------------------------------\n")

def limpar_posicao(matriz, pos):
    if pos in locPoderes1:
        matriz[pos[0]][pos[1]] = "P1"
    else:
        matriz[pos[0]][pos[1]] = 0
        
    if pos in locPoderes2:
        matriz[pos[0]][pos[1]] = "P2"
    else:
        matriz[pos[0]][pos[1]] = 0
        
def verificar_poderes(carro, pos, matriz):
    global locObjetivo, locPoderes1, locPoderes2
    if pos in locPoderes1:
        print(f'[{carro}] ativou o Poder 1. Objetivo vai para esquerda')
        matriz[locObjetivo[0]][locObjetivo[1]] = 0
        if locObjetivo[1] > 0:
            locObjetivo[1] -= 1
        matriz[locObjetivo[0]][locObjetivo[1]] = "OO"
        locPoderes1.remove(pos)
        return True # retorna true pra adicionar na lista de prioridades
        
    elif pos in locPoderes2:
        print(f'[{carro}] ativou o Poder 2. Objetivo vai para direita')
        matriz[locObjetivo[0]][locObjetivo[1]] = 0
        if locObjetivo[1] > 0:
            locObjetivo[1] += 1
        matriz[locObjetivo[0]][locObjetivo[1]] = "OO"
        locPoderes2.remove(pos)
        return True # retorna true pra adicionar na lista de prioridades
    
    return False

def decisao_c1(matriz):
    global locC1, locObjetivo
    lista_prioridades = []
    
    if locObjetivo and locC1 == locObjetivo:
        lista_prioridades.append({"acao": "C1_VITORIA", "peso": 100})
        
    if verificar_poderes("C1", locC1, matriz):
        lista_prioridades.append({"acao": "C1_CONSUMIR", "peso": 90})
        
    if locObjetivo and locC1[0] > locObjetivo[0]:
        lista_prioridades.append({"acao": "C1_CIMA", "peso": 60})
        
    if locObjetivo and locC1[1] > locObjetivo[1]:
        lista_prioridades.append({"acao": "C1_ESQUERDA", "peso": 50})
        
    if locObjetivo and locC1[1] < locObjetivo[1]:
        lista_prioridades.append({"acao": "C1_DIREITA", "peso": 40})
        
    if lista_prioridades:
        melhor_acao = max(lista_prioridades, key=lambda item: item['peso'])
        acao = melhor_acao['acao']
        print(f"[C1] Ação: {acao} (Prioridade: {melhor_acao['peso']})")
        
        if acao == "C1_VITORIA":
            print(">>> C1 chegou ao Objetivo <<<")
            limpar_posicao(matriz, locC1)
            matriz[locC1[0]][locC1[1]] = "C1"
            return True # condição de vitoria, win retorna true e break na main 
        
        if acao == "C1_CONSUMIR":
            print(">>> C1 consome poder <<<")
            limpar_posicao(matriz, locC1)
            matriz[locC1[0]][locC1[1]] = "C1"
        
    limpar_posicao(matriz, locC1)
    
    if acao == "C1_CIMA":
        locC1[0] -= 1
    if acao == "C1_ESQUERDA":
        locC1[1] -= 1
    if acao == "C1_DIREITA":
        locC1[1] += 1
        
    if locObjetivo and locC1 == locObjetivo:
        matriz[locC1[0]][locC1[1]] = "VV"
    else:
        matriz[locC1[0]][locC1[1]] = "C1"
        
    return False # retorna que nao pegou o objetivo
        
def decisao_c2(matriz):
    global locC2, locObjetivo
    lista_prioridades = []
    
    if locObjetivo and locC2 == locObjetivo:
        lista_prioridades.append({"acao": "C2_VITORIA", "peso": 100})
        
    if verificar_poderes("C2", locC2, matriz):
        lista_prioridades.append({"acao": "C2_CONSUMIR", "peso": 90})
        
    if locObjetivo and locC2[0] > locObjetivo[0]:
        lista_prioridades.append({"acao": "C2_CIMA", "peso": 60})
        
    if locObjetivo and locC2[1] > locObjetivo[1]:
        lista_prioridades.append({"acao": "C2_ESQUERDA", "peso": 50})
        
    if locObjetivo and locC2[1] < locObjetivo[1]:
        lista_prioridades.append({"acao": "C2_DIREITA", "peso": 40})
        
    if lista_prioridades:
        melhor_acao = max(lista_prioridades, key=lambda item: item['peso'])
        acao = melhor_acao['acao']
        print(f"[C2] Ação: {acao} (Prioridade: {melhor_acao['peso']})")
        
        if acao == "C2_VITORIA":
            print(">>> C2 chegou ao Objetivo <<<")
            limpar_posicao(matriz, locC2)
            matriz[locC2[0]][locC2[1]] = "C2"
            return True # mesma coisa do c1
        
        if acao == "C2_CONSUMIR":
            print(">>> C2 consome poder <<<")
            limpar_posicao(matriz, locC1)
            matriz[locC2[0]][locC2[1]] = "C2"
        
        limpar_posicao(matriz, locC2)
        
        if acao == "C2_CIMA":
            locC2[0] -= 1
        if acao == "C2_ESQUERDA":
            locC2[1] -= 1
        if acao == "C2_DIREITA":
            locC2[1] += 1
            
        if locObjetivo and locC2 == locObjetivo:
            matriz[locC2[0]][locC2[1]] = "VV"
        else:
            matriz[locC2[0]][locC2[1]] = "C2"
        
    return False # retorna que nao pegou o objetivo

if __name__ == "__main__":
    tabuleiro_principal = gerar_tabuleiro()
    vitoria_turno = False
    
    gerar_c1(tabuleiro_principal)
    gerar_c2(tabuleiro_principal)
    gerar_objetivo(tabuleiro_principal)
    gerar_poderes(tabuleiro_principal)

    while not vitoria_turno:
        imprimir_tabuleiro(tabuleiro_principal)
        print(f"[TURN]: {TURN}.")
        
        # alterna os turnos
        if TURN == "c1":
            vitoria_turno = decisao_c1(tabuleiro_principal)
            if vitoria_turno:
                ganhador = "C1"
                break
            TURN = "c2"
            
        elif TURN == "c2":
            vitoria_turno = decisao_c2(tabuleiro_principal)
            if vitoria_turno:
                ganhador = "C2"
                break
            TURN = "c1"

        # espera e clena a tela pra proxima rodada
        input("pressione [ENTER] para próxima rodada...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    # achou a win e saiu da main exec
    print("\n--- FIM DE JOGO ---")
    print(f'>>> {ganhador} venceu! <<<')
    