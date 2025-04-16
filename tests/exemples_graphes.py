from graphe import Graphe

def exemple_graphe_1():
    sommets = [f"v{i}" for i in range(1, 17)]
    arretes = {}
    for i in range(len(sommets)):
        for j in range(i + 1, len(sommets)):
            cout = abs(i - j) + 1
            arretes[(sommets[i], sommets[j])] = cout
            arretes[(sommets[j], sommets[i])] = cout

    bloquees = {
        ("v3", "v4"), ("v3", "v5"), ("v7", "v8"),
        ("v9", "v10"), ("v12", "v13"), ("v12", "v14"),
        ("v16", "v4"), ("v4", "v5"), ("v8", "v10"), ("v13", "v14"),
        ("v14", "v1"), ("v13", "v10"), ("v10", "v5"), ("v5", "v14")
    }

    graphe = Graphe(sommets, arretes)
    for u, v in bloquees:
        graphe.bloquer_arrete(u, v)

    return graphe, "v1"
