from graphe import Graphe

# n = 16
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
        graphe.block_arrete(u, v)

    return graphe, "v1"

def exemple_graphe_1bis():
    sommets = [f"v{i}" for i in range(1, 17)]
    arretes = {}
    for i in range(len(sommets)):
        for j in range(i + 1, len(sommets)):
            cout = abs(i - j) + 1
            arretes[(sommets[i], sommets[j])] = cout
            arretes[(sommets[j], sommets[i])] = cout

    bloquees = {
        ("v3", "v4"), ("v9", "v10"), ("v12", "v13"),
        ("v8", "v10"), ("v13", "v14")
    }

    graphe = Graphe(sommets, arretes)
    for u, v in bloquees:
        graphe.block_arrete(u, v)

    return graphe, "v1"

# n = 30
def exemple_graphe_2():
    sommets = [f"v{i}" for i in range(1, 31)]
    arretes = {}
    for i in range(len(sommets)):
        for j in range(i + 1, len(sommets)):
            cout = abs(i - j) + 1
            arretes[(sommets[i], sommets[j])] = cout
            arretes[(sommets[j], sommets[i])] = cout

    bloquees = {
        ("v2", "v3"), ("v3", "v4"), ("v5", "v6"), ("v7", "v8"),
        ("v10", "v11"), ("v12", "v13"), ("v14", "v15"), ("v17", "v18"),
        ("v19", "v20"), ("v20", "v21"), ("v22", "v23"), ("v25", "v26"),
        ("v27", "v28")
    }

    graphe = Graphe(sommets, arretes)
    for u, v in bloquees:
        graphe.block_arrete(u, v)

    return graphe, "v1"


def exemple_graphe_2bis():
    sommets = [f"v{i}" for i in range(1, 31)]
    arretes = {}
    for i in range(len(sommets)):
        for j in range(i + 1, len(sommets)):
            cout = abs(i - j) + 1
            arretes[(sommets[i], sommets[j])] = cout
            arretes[(sommets[j], sommets[i])] = cout

    bloquees = {
        ("v3", "v4"), ("v10", "v11"), ("v20", "v21")
    }

    graphe = Graphe(sommets, arretes)
    for u, v in bloquees:
        graphe.block_arrete(u, v)

    return graphe, "v1"

# n = 40
def exemple_graphe_3():
    sommets = [f"v{i}" for i in range(1, 41)]
    arretes = {}
    for i in range(len(sommets)):
        for j in range(i + 1, len(sommets)):
            cout = abs(i - j) + 1
            arretes[(sommets[i], sommets[j])] = cout
            arretes[(sommets[j], sommets[i])] = cout

    bloquees = {
        ("v2", "v3"), ("v4", "v5"), ("v6", "v7"), ("v8", "v9"),
        ("v11", "v12"), ("v13", "v14"), ("v17", "v18"), ("v19", "v20"),
        ("v22", "v23"), ("v24", "v25"), ("v27", "v28"), ("v30", "v31"),
        ("v32", "v33"), ("v36", "v37")
    }

    graphe = Graphe(sommets, arretes)
    for u, v in bloquees:
        graphe.block_arrete(u, v)

    return graphe, "v1"

def exemple_graphe_3bis():
    sommets = [f"v{i}" for i in range(1, 41)]
    arretes = {}
    for i in range(len(sommets)):
        for j in range(i + 1, len(sommets)):
            cout = abs(i - j) + 1
            arretes[(sommets[i], sommets[j])] = cout
            arretes[(sommets[j], sommets[i])] = cout

    # Blocages stratégiques pour pénaliser CR
    bloquees = {
        ("v2", "v3"), ("v3", "v4"),
        ("v5", "v6"), ("v6", "v7"),
        ("v8", "v9"), ("v9", "v10"),
        ("v11", "v12"), ("v12", "v13"),
        ("v14", "v15"), ("v15", "v16"),
        ("v17", "v18"), ("v18", "v19"),
        ("v20", "v21"), ("v21", "v22"),
        ("v23", "v24"), ("v24", "v25"),
        ("v26", "v27"), ("v27", "v28"),
        ("v29", "v30"), ("v30", "v31"),
        ("v32", "v33"), ("v33", "v34"),
        ("v35", "v36"), ("v36", "v37"),
        ("v38", "v39"), ("v39", "v40")
    }

    graphe = Graphe(sommets, arretes)
    for u, v in bloquees:
        graphe.block_arrete(u, v)

    return graphe, "v1"




def exemple_graphe_0():
    sommets = ["S", "v1", "v2", "v3", "v4", "t"]
    arretes = {
        ("S", "v1"): 2, ("v1", "S"): 2,
        ("S", "v3"): 2, ("v3", "S"): 2,
        ("v1", "v3"): 2, ("v3", "v1"): 2,
        ("v1", "v2"): 2, ("v2", "v1"): 2,
        ("v3", "v2"): 3, ("v2", "v3"): 3,
        ("v3", "v4"): 2, ("v4", "v3"): 2,
        ("v2", "v4"): 3, ("v4", "v2"): 3,
        ("v2", "t"): 3, ("t", "v2"): 3,
        ("v4", "t"): 2, ("t", "v4"): 2
    }

    bloquees = {("v3", "v4"), ("v4", "v3")}  # Attention, bloqué dans les deux sens

    graphe = Graphe(sommets, arretes)
    for u, v in bloquees:
        graphe.block_arrete(u, v)

    return graphe, "S"
