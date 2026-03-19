# from dados import dist, vizinhos
# from busca import busca_gulosa, busca_aestrela

# def main():
#     cidades = sorted(list(dist.keys()))
#     print(f"Cidades: {', '.join(cidades)}")
    
#     while True:
#         entrada = input("\ncidade de partida (ou 'exit' para sair): ").strip()
        
#         if entrada.lower() == 'exit':
#             break
            
#         origem = entrada.title()
#         if origem not in dist:
#             print(f"Erro: '{origem}' não está no mapa.")
#             continue

#         destino = "Bucharest"

#         print(f"\n[Busca Gulosa] {origem} para {destino}...")
#         rota_g, custo_g = busca_gulosa(origem, destino, vizinhos, dist)
        
#         if rota_g:
#             partes = []
#             for i in range(len(rota_g) - 1):
#                 c_at, prox = rota_g[i], rota_g[i+1]
#                 partes.append(f"{c_at} ({vizinhos[c_at][prox]})")
#             partes.append(rota_g[-1])
#             print(f"Caminho: {' -> '.join(partes)}")
#             print(f"Custo Total: {custo_g}")

#         print(f"\n[Busca A*] {origem} para {destino}...")
#         rota_a, custo_a = busca_aestrela(origem, destino, vizinhos, dist)
        
#         if rota_a:
#             print(f"Caminho: {' -> '.join(rota_a)}")

# if __name__ == "__main__":
#     main()

from dados import dist, vizinhos

def busca_gulosa(inicio, objetivo, grafo, heuristica):
    atual = inicio
    custo_total = 0

    print(f"\n[Busca Gulosa] {inicio} -> {objetivo}\n")

    while atual != objetivo:
        vizinhos_atuais = grafo.get(atual, {})
        if not vizinhos_atuais:
            print("Sem vizinhos. Falha.")
            return None, custo_total

        melhor = None
        menor_h = float('inf')

        for cidade, peso in vizinhos_atuais.items():
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

def main():
    cidades = sorted(list(dist.keys()))
    print(f"Cidades: {', '.join(cidades)}")
    
    while True:
        entrada = input("\ncidade de partida (ou 'exit' para sair): ").strip()
        
        if entrada.lower() == 'exit':
            break
            
        origem = entrada.title()
        if origem not in dist:
            print(f"Erro: '{origem}' não está no mapa.")
            continue

        destino = "Bucharest"

        # Menu de escolha do algoritmo
        print("\nEscolha o algoritmo de busca:")
        print("1 - Busca Gulosa (SEM algoritmo de visitados)")
        print("2 - Busca A* (COM algoritmo de visitados)")
        escolha = input("Digite 1 ou 2: ").strip()

        if escolha == '1':
            print("\n[Aviso] Você escolheu a Busca Gulosa.")
            print("-> Esta implementação NÃO salva os nós visitados (pode entrar em loop infinito dependendo do mapa).\n")
            busca_gulosa(origem, destino, vizinhos, dist)
            
        elif escolha == '2':
            print("\n[Aviso] Você escolheu a Busca A*.")
            print("-> Esta implementação UTILIZA um dicionário de nós visitados para otimização e segurança.\n")
            print(f"[Busca A*] {origem} para {destino}...")
            
            rota_a, custo_a = busca_aestrela(origem, destino, vizinhos, dist)
            
            if rota_a:
                print(f"Caminho: {' -> '.join(rota_a)}")
                print(f"Custo Total: {custo_a}")
            else:
                print("Não foi possível encontrar um caminho.")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()