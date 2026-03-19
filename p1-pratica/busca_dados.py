dist = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Dobreta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 232,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374,
    # prova city
    "Prova City": 280
}

vizinhos = {
    "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
    "Bucharest": {"Urziceni": 85, "Fagaras": 211, "Giurgiu": 90, "Pitesti": 101},
    "Craiova": {"Dobreta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    # prova city vizinho dobreta
    "Dobreta" : {"Craiova": 120, "Mehadia": 75, "Prova City":100},
    "Eforie": {"Hirsova": 86},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Giurgiu": {"Bucharest": 90},
    "Hirsova": {"Eforie": 86, "Urziceni": 98},
    "Iasi": {"Neamt": 87, "Vaslui": 92},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    # prova city vizinho mehad
    "Mehadia":{"Lugoj":70, "Dobreta":75, "Prova City":110},
    "Neamt":{"Iasi":87},
    "Oradea":{"Zerind":71, "Sibiu":151},
    "Pitesti": {"Bucharest":101, "Craiova":138, "Rimnicu Vilcea":97},
    "Rimnicu Vilcea":{"Sibiu":80, "Pitesti":97, "Craiova":146},
    "Sibiu":{"Arad":140, "Fagaras":99, "Oradea":151, "Rimnicu Vilcea":80},
    "Timisoara":{"Arad":118, "Lugoj":111},
    "Urziceni":{"Bucharest":85, "Hirsova":98, "Vaslui":142},
    "Vaslui":{"Iasi":92, "Urziceni":142},
    "Zerind":{"Arad":75, "Oradea":71},
    # dobreta + mehadia
    "Prova City": {"Dobreta":100, "Mehadia":110}
}