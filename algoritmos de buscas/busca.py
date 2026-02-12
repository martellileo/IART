# def busca_gulosa(inicio, objetivo, grafo, heuristica):
#     # [(valor_h, custo_g, atual, caminho)]
#     fila = [(heuristica[inicio], 0, inicio, [inicio])]
#     visitados = set()

#     while fila:
#         # encontra menor h
#         indice_melhor = 0
#         for i in range(1, len(fila)):
#             if fila[i][0] < fila[indice_melhor][0]:
#                 indice_melhor = i
        
#         # popa o melhor elemento
#         (_, custo_acumulado, atual, caminho) = fila.pop(indice_melhor)

#         if atual == objetivo:
#             return caminho, custo_acumulado

#         if atual not in visitados:
#             visitados.add(atual)
#             for proximo, peso in grafo.get(atual, {}).items():
#                 if proximo not in visitados:
#                     fila.append((heuristica[proximo], custo_acumulado + peso, proximo, caminho + [proximo]))
        
    
#     return None, 0

def busca_gulosa(inicio, objetivo, grafo, heuristica):
    atual = inicio
    custo_total = 0

    print(f"\n[Busca Gulosa] {inicio} -> {objetivo}\n")

    while atual != objetivo:
        vizinhos = grafo.get(atual, {})
        if not vizinhos:
            print("Sem vizinhos. Falha.")
            return None, custo_total

        melhor = None
        menor_h = float('inf')

        for cidade, peso in vizinhos.items():
            if heuristica[cidade] < menor_h:
                menor_h = heuristica[cidade]
                melhor = (cidade, peso)

        proximo, peso = melhor
        print(f"{atual} -> {proximo} | {peso}\n")

        custo_total += peso
        atual = proximo

    print(f"Destino alcançado: {objetivo}")
    print(f"Custo Total: {custo_total}")
    return objetivo, custo_total


def busca_aestrela(inicio, objetivo, grafo, heuristica):
    # [(valor_f, custo_g, atual, caminho)]
    fila = [(heuristica[inicio], 0, inicio, [inicio])]
    visitados = {}

    while fila:
        indice_melhor = 0
        for i in range(1, len(fila)):
            if fila[i][0] < fila[indice_melhor][0]:
                indice_melhor = i
        
        (f_score, g_score, atual, caminho) = fila.pop(indice_melhor)

        if atual == objetivo:
            return caminho, g_score

        if atual in visitados and visitados[atual] <= g_score:
            continue
        
        visitados[atual] = g_score

        for proximo, peso in grafo.get(atual, {}).items():
            novo_g = g_score + peso
            novo_f = novo_g + heuristica[proximo]
            fila.append((novo_f, novo_g, proximo, caminho + [proximo]))
            
    return None, 0