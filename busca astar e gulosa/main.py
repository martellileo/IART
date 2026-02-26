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
from busca import busca_gulosa

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

        busca_gulosa(origem, destino, vizinhos, dist)

if __name__ == "__main__":
    main()
