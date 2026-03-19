from busca_dados import dist, vizinhos
import os

def busca_gulosa(inicio, objetivo, grafo, heuristica):
    atual = inicio
    custo_total = 0
    visitados = set()

    print(f"\n[Busca Gulosa] {inicio} -> {objetivo}\n")

    while atual != objetivo:
        visitados.add(atual)  # cidade visitada
        vizinhos_atuais = grafo.get(atual, {})
        
        # logica dos visitados
        vizinhos_validos = {c: p for c, p in vizinhos_atuais.items() if c not in visitados}
        
        if not vizinhos_validos:
            print("sem caminhos disponiveis")
            return None, custo_total

        melhor = None
        menor_h = float('inf')

        for cidade, peso in vizinhos_validos.items():
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
    origem = "Prova City"
    destino = "Bucharest"     
    print(f'Origem {origem} -> Destino {destino}')
    
    while True:           
        print("\nEscolha o algoritmo de busca:")
        print("1 - Busca Gulosa (COM algoritmo de visitados)")
        print("2 - Busca A* (COM algoritmo de visitados)")
        escolha = input("Digite 1, 2 ou exit: ").strip()
        os.system('cls' if os.name == 'nt' else 'clear') # limpar tela apos escolha

        if escolha == '1': # gulosa
            print("\n[Aviso] Você escolheu a Busca Gulosa.")
            print("-> implementado cidades visitadas.\n")
            busca_gulosa(origem, destino, vizinhos, dist)
            
        elif escolha == '2': # astar
            print("\n[Aviso] Você escolheu a Busca A*.")
            print("-> implementado cidades visitadas.\n")
            print(f"[Busca A*] {origem} para {destino}...")
            
            rota_a, custo_a = busca_aestrela(origem, destino, vizinhos, dist)
            
            if rota_a:
                print(f"Caminho: {' -> '.join(rota_a)}")
                print(f"Custo Total: {custo_a}")
            else:
                print("Não foi possível encontrar um caminho.")
                
        elif escolha.lower() == 'exit':
            break
        
        else:
            print("Opção inválida. Tente novamente.")
            
            
if __name__ == "__main__":
    main()