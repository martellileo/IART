import random as r

HITS = 3
TAMANHO = 10
valor_dano = 1
buff_ativo = True

locHeroi = []
locVilao = []
locBuff = []
lista_prioridades = []

def gerar_tabuleiro():
    tabuleiro = []
    for i in range(TAMANHO):
        linha = []
        for j in range(TAMANHO):
            linha.append(0)
        tabuleiro.append(linha)
    return tabuleiro

def set_caracter(matriz, letra):
    x = r.randrange(TAMANHO)
    y = r.randrange(TAMANHO)
    
    if matriz[x][y] == 0:
        matriz[x][y] = letra
        return [x, y]
    else:
        return set_caracter(matriz, letra)

def gerar_heroi(matriz):
    global locHeroi
    locHeroi = set_caracter(matriz, "H")

def gerar_vilao(matriz):
    global locVilao
    locVilao = set_caracter(matriz, "V")

def gerar_buff(matriz):
    global locBuff
    locBuff = set_caracter(matriz, "B")

def imprimir_tabuleiro(matriz):
    print("\n--- TABULEIRO DO JOGO ---")
    for linha in matriz:
        linha_formatada = " ".join(str(celula) if celula != 0 else "." for celula in linha)
        print(linha_formatada)
    print("-------------------------\n")

def decisao(matriz):
    global lista_prioridades, locHeroi, locVilao, locBuff, buff_ativo
    lista_prioridades = []

    if not locVilao:
        lista_prioridades.append({"acao": "SPAWN_VILAO", "peso": 110})

    if locVilao and locHeroi == locVilao:
        lista_prioridades.append({"acao": "HIT", "peso": 100})
    
    if buff_ativo and locHeroi == locBuff:
        lista_prioridades.append({"acao": "COLETAR_BUFF", "peso": 95})

    if locVilao:
        if locHeroi[0] > locVilao[0]:
            lista_prioridades.append({"acao": "MOVER_CIMA", "peso": 60})
        
        if locHeroi[0] < locVilao[0]:
            lista_prioridades.append({"acao": "MOVER_BAIXO", "peso": 55})

        if locHeroi[1] > locVilao[1]:
            lista_prioridades.append({"acao": "MOVER_ESQUERDA", "peso": 50})
        
        if locHeroi[1] < locVilao[1]:
            lista_prioridades.append({"acao": "MOVER_DIREITA", "peso": 45})

    realizar(matriz)

def realizar(matriz):
    global HITS, locHeroi, locVilao, locBuff, lista_prioridades, valor_dano, buff_ativo

    if not lista_prioridades:
        return

    melhor_acao = max(lista_prioridades, key=lambda item: item['peso'])
    acao = melhor_acao['acao']
    
    print(f"lista de turn {lista_prioridades}")
    print(f"best turn: {acao} (Peso: {melhor_acao['peso']})")

    if acao == "SPAWN_VILAO":
        locVilao = set_caracter(matriz, "V")
        return

    if acao == "HIT":
        HITS -= valor_dano
        matriz[locHeroi[0]][locHeroi[1]] = "H"
        locVilao = [] 
        return

    if acao == "COLETAR_BUFF":
        valor_dano = 2
        buff_ativo = False
        return

    matriz[locHeroi[0]][locHeroi[1]] = 0

    if acao == "MOVER_CIMA":
        locHeroi[0] -= 1
    elif acao == "MOVER_BAIXO":
        locHeroi[0] += 1
    elif acao == "MOVER_ESQUERDA":
        locHeroi[1] -= 1
    elif acao == "MOVER_DIREITA":
        locHeroi[1] += 1

    if locVilao and locHeroi == locVilao:
        matriz[locHeroi[0]][locHeroi[1]] = "⚔️"
    else:
        matriz[locHeroi[0]][locHeroi[1]] = "H"

if __name__ == "__main__":
    tabuleiro_principal = gerar_tabuleiro()
    
    gerar_heroi(tabuleiro_principal)
    gerar_vilao(tabuleiro_principal)
    gerar_buff(tabuleiro_principal)

    while HITS > 0:
        imprimir_tabuleiro(tabuleiro_principal)
        
        print(f"hits {HITS} | Dano atual: {valor_dano}")
        if buff_ativo:
            print(f"locBuff: {locBuff}")
            
        print(f"locHeroi: {locHeroi} | locVilao: {locVilao}")
        
        input()
        decisao(tabuleiro_principal)
    
    print("\n--- end game ---")