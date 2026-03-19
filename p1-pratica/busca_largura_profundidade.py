from collections import deque

def criar_grafo():
    grafo = {}
    
    conexoes = [
        ('1', '14'),  ('1','15'),   ('15', '2'),  ('2', '17'),
        ('17', '3'),  ('3', '18'),  ('3', '4'),   ('4','5'),
        ('5', '6'),   ('6', '7'),   ('7', '19'),  ('5', '9'),
        ('9', '10'),  ('10', '13'), ('13', '14'),
        ('14', '12'), ('14', '16')
    ]
    
    for u, v in conexoes:
        if u not in grafo: grafo[u] = []
        if v not in grafo: grafo[v] = []
        
        grafo[u].append(v)
        grafo[v].append(u)
        
    return grafo

def imprimir_adjacentes(grafo):
    # sorted ta dando erro pq ta tratando como string, entao sempre pega
    # o numero 1 como primeiro 1 - 10 - 11 - 12 - etc
    print("\n--- Lista de Adjacentes ---")
    for no in sorted(grafo.keys()):
        vizinhos = ", ".join(sorted(grafo[no]))
        print(f"Nó {no}: [{vizinhos}]")

def realizar_largura(grafo, inicio, objetivo):
    if inicio not in grafo or objetivo not in grafo:
        return None

    fila = deque([[inicio]])
    visitados = {inicio}

    while fila:
        caminho_atual = fila.popleft()
        no_atual = caminho_atual[-1]

        if no_atual == objetivo:
            return caminho_atual

        for vizinho in sorted(grafo[no_atual]):
            if vizinho not in visitados:
                visitados.add(vizinho)
                novo_caminho = list(caminho_atual)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
                
    return None

def realizar_profundidade(grafo, inicio, objetivo):
    if inicio not in grafo or objetivo not in grafo:
        return None

    pilha = [[inicio]]
    visitados = {inicio}

    while pilha:
        caminho_atual = pilha.pop()
        no_atual = caminho_atual[-1]

        if no_atual == objetivo:
            return caminho_atual

        for vizinho in sorted(grafo[no_atual], reverse=True):
            if vizinho not in visitados:
                visitados.add(vizinho)
                novo_caminho = list(caminho_atual)
                novo_caminho.append(vizinho)
                pilha.append(novo_caminho)
                
    return None

def main():
    grafo = criar_grafo()
    
    imprimir_adjacentes(grafo)
    
    print("\n--- Configuração da Busca ---")
    raiz = '3'
    alvo = '13'

    print("\nBusca em Largura")
    resultadoBFS = realizar_largura(grafo, raiz, alvo)
    print(f"Trajeto: {' -> '.join(resultadoBFS)}")
    print(f"Número de nós no caminho: {len(resultadoBFS)}")
    print(f"Distância (saltos): {len(resultadoBFS) - 1}")

    print("\nBusca em Profundidade")
    resultadoDFS = realizar_profundidade(grafo, raiz, alvo)
    print(f"Trajeto: {' -> '.join(resultadoDFS)}")
    print(f"Número de nós no caminho: {len(resultadoDFS)}")
    print(f"Distância (saltos): {len(resultadoDFS) - 1}")

if __name__ == "__main__":
    main()