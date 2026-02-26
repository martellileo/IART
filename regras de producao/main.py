import random as r

HITS = 3
TAMANHO = 10

LOCHEROI = []
LOCVILAO = []
LOCBUFF = []

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
    if locHeroi[0][1] == locVilao[0][1]:
        print("hit")
        if HITS > 0: HITS -= 1
        matriz[locVilao[0]][locVilao[1]] = 0
        set_caracter(matriz, "V")

    # x > 2 1
    if locHeroi[0] > locVilao[0]:
        matriz[locHeroi[0]][locHeroi[1]] = 0
        locHeroi[0] -= 1
        matriz[locHeroi[0]][locHeroi[1]] = "H"

if __name__ == "__main__":
    tabuleiro = gerar_tabuleiro()
    
    gerar_heroi(tabuleiro)
    gerar_vilao(tabuleiro)
    gerar_buff(tabuleiro)

    while HITS > 0:
        imprimir_tabuleiro(tabuleiro)
        
        print(f"Vida (Hits) restante: {HITS}")
        print(f"Loc Heroi (H): {locHeroi}")
        print(f"Loc Vilao (V): {locVilao}")
        print(f"Loc Buff (B): {locBuff}")
        
        print("\nPressione Enter para atualizar o turno (ou Ctrl+C para sair)...")
        input()
        decisao(tabuleiro)
