import random as r
import os

HITS = 3
TAMANHO = 10

locHeroi = []
locVilao = []
locPoderes = []

def gerar_tabuleiro():
    return [[0 for _ in range(TAMANHO)] for _ in range(TAMANHO)]

def set_caracter(matriz, letra):
    while True:
        x = r.randrange(TAMANHO)
        y = r.randrange(TAMANHO)
        if matriz[x][y] == 0:
            matriz[x][y] = letra
            return [x, y]

def gerar_heroi(matriz):
    global locHeroi
    locHeroi = set_caracter(matriz, "H")

def gerar_vilao(matriz):
    global locVilao

    if locVilao and matriz[locVilao[0]][locVilao[1]] == "V":
        matriz[locVilao[0]][locVilao[1]] = 0
    locVilao = set_caracter(matriz, "V")

def gerar_poderes(matriz):
    global locPoderes
    locPoderes = []

    for _ in range(5):
        pos = set_caracter(matriz, "P")
        locPoderes.append(pos)

def imprimir_tabuleiro(matriz):
    print("\n--- TABULEIRO DO JOGO ---")
    for linha in matriz:
        linha_formatada = " ".join(str(celula) if celula != 0 else "." for celula in linha)
        print(linha_formatada)
    print("-------------------------\n")

def limpar_posicao(matriz, pos):
    if pos in locPoderes:
        matriz[pos[0]][pos[1]] = "P"
    else:
        matriz[pos[0]][pos[1]] = 0

def decisao_heroi(matriz):
    global locHeroi, locVilao, HITS
    lista_prioridades = []

    # regra 1 - prioridade 100
    if locVilao and locHeroi == locVilao:
        lista_prioridades.append({"acao": "CATCH", "peso": 100})

    # regra 2 - prioridade 60
    if locVilao and locHeroi[0] > locVilao[0] and locHeroi[0] >= 2:
        lista_prioridades.append({"acao": "HEROI_CIMA_2", "peso": 60})
        
    # regra 2.1 - prioridade 59 (variação pra borda)
    if locVilao and locHeroi[0] > locVilao[0] and locHeroi[0] < 2:
        lista_prioridades.append({"acao": "HEROI_CIMA_1", "peso": 59})

    # regra 3 - prioridade 55 
    if locVilao and locHeroi[0] < locVilao[0] and locHeroi[0] <= TAMANHO - 3:
        lista_prioridades.append({"acao": "HEROI_BAIXO_2", "peso": 55})

    # regra 3.1 - prioridade 54 (variação pra borda)
    if locVilao and locHeroi[0] < locVilao[0] and locHeroi[0] > TAMANHO - 3:
        lista_prioridades.append({"acao": "HEROI_BAIXO_1", "peso": 54})

    # regra 4 - prioridade 50 
    if locVilao and locHeroi[1] > locVilao[1] and locHeroi[1] >= 2:
        lista_prioridades.append({"acao": "HEROI_ESQUERDA_2", "peso": 50})
        
    # regra 4.1 - prioridade 49 (variação pra borda)
    if locVilao and locHeroi[1] > locVilao[1] and locHeroi[1] < 2:
        lista_prioridades.append({"acao": "HEROI_ESQUERDA_1", "peso": 49})

    # regra 5 - prioridade 45
    if locVilao and locHeroi[1] < locVilao[1] and locHeroi[1] <= TAMANHO - 3:
        lista_prioridades.append({"acao": "HEROI_DIREITA_2", "peso": 45})
        
    # regra 5.1 - prioridade 44 (variação pra borda)
    if locVilao and locHeroi[1] < locVilao[1] and locHeroi[1] > TAMANHO - 3:
        lista_prioridades.append({"acao": "HEROI_DIREITA_1", "peso": 44})

    if lista_prioridades:
        melhor_acao = max(lista_prioridades, key=lambda item: item['peso'])
        acao = melhor_acao['acao']
        print(f"[Herói] Ação: {acao} (Prioridade: {melhor_acao['peso']})")
        
        # decisão do herói
        if acao == "CATCH":
            HITS -= 1
            print(">>> HIT! <<<")
            limpar_posicao(matriz, locHeroi)
            if HITS > 0:
                gerar_vilao(matriz)
                matriz[locHeroi[0]][locHeroi[1]] = "H"
            return True

        limpar_posicao(matriz, locHeroi)
        
        # executa a melhor ação
        if acao == "HEROI_CIMA_2": 
            locHeroi[0] -= 2
        if acao == "HEROI_CIMA_1": 
            locHeroi[0] -= 1
        if acao == "HEROI_BAIXO_2": 
            locHeroi[0] += 2
        if acao == "HEROI_BAIXO_1": 
            locHeroi[0] += 1
        if acao == "HEROI_ESQUERDA_2": 
            locHeroi[1] -= 2
        if acao == "HEROI_ESQUERDA_1": 
            locHeroi[1] -= 1
        if acao == "HEROI_DIREITA_2": 
            locHeroi[1] += 2
        if acao == "HEROI_DIREITA_1": 
            locHeroi[1] += 1


        if locVilao and locHeroi == locVilao:
            matriz[locHeroi[0]][locHeroi[1]] = "X"
        else:
            matriz[locHeroi[0]][locHeroi[1]] = "H"
            
    return False


def decisao_vilao(matriz):
    global locVilao, locHeroi
    lista_prioridades = []
    
    # vilao espera pra tomar hit
    if not locVilao or locHeroi == locVilao:
        return

    # regra 6 - prioridade 100
    if locVilao in locPoderes:
        lista_prioridades.append({"acao": "VILAO_TELEPORT", "peso": 100})

    # regra 7 - prioridade 60
    if locHeroi[0] > locVilao[0] and locVilao[0] > 0:
        lista_prioridades.append({"acao": "VILAO_CIMA", "peso": 60})
        
    # regra 8 - prioridade 55
    if locHeroi[0] < locVilao[0] and locVilao[0] < TAMANHO - 1:
        lista_prioridades.append({"acao": "VILAO_BAIXO", "peso": 55})

    # regra 9 - prioridade 50
    if locHeroi[1] > locVilao[1] and locVilao[1] > 0:
        lista_prioridades.append({"acao": "VILAO_ESQUERDA", "peso": 50})

    # regra 10 - prioridade 45
    if locHeroi[1] < locVilao[1] and locVilao[1] < TAMANHO - 1:
        lista_prioridades.append({"acao": "VILAO_DIREITA", "peso": 45})

    if lista_prioridades:
        melhor_acao = max(lista_prioridades, key=lambda item: item['peso'])
        acao = melhor_acao['acao']
        print(f"[Vilão] Ação: {acao} (Prioridade: {melhor_acao['peso']})")
        
        # decisão do vilão
        if acao == "VILAO_TELEPORT":
            print(">>> vilão pegou o poder! <<<")
            limpar_posicao(matriz, locVilao)
            locVilao = set_caracter(matriz, "V")
            return

        limpar_posicao(matriz, locVilao)

        if acao == "VILAO_CIMA":
            locVilao[0] -= 1
        if acao == "VILAO_BAIXO":
            locVilao[0] += 1
        if acao == "VILAO_ESQUERDA":
            locVilao[1] -= 1
        if acao == "VILAO_DIREITA":
            locVilao[1] += 1


        if locVilao == locHeroi:
            matriz[locVilao[0]][locVilao[1]] = "X"
        else:
            matriz[locVilao[0]][locVilao[1]] = "V"

if __name__ == "__main__":
    tabuleiro_principal = gerar_tabuleiro()
    
    gerar_poderes(tabuleiro_principal)
    gerar_heroi(tabuleiro_principal)
    gerar_vilao(tabuleiro_principal)

    while HITS > 0:
        imprimir_tabuleiro(tabuleiro_principal)
        print(f"vida: {HITS}.")
        
        capturou_neste_turno = decisao_heroi(tabuleiro_principal)
        if not capturou_neste_turno:
            decisao_vilao(tabuleiro_principal)

        input("pressione [ENTER] para próxima rodada...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    print("\n--- FIM DE JOGO ---")
    print("vilão derrotado!")