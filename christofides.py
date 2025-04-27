import networkx as nx
import matplotlib.pyplot as plt

def christofides(graphe, depart):
    G = nx.Graph()
    for (u, v), cout in graphe.arretes.items():
        G.add_edge(u, v, weight=cout)

    # 1. Arbre couvrant de poids minimal
    T = nx.minimum_spanning_tree(G)

    # 2. Sommets de degré impair
    odd_nodes = [v for v in T.nodes if T.degree(v) % 2 == 1]
    G_odd = nx.Graph()
    for i in range(len(odd_nodes)):
        for j in range(i+1, len(odd_nodes)):
            u, v = odd_nodes[i], odd_nodes[j]
            if G.has_edge(u, v):
                G_odd.add_edge(u, v, weight=G[u][v]['weight'])

    # 3. Couplage parfait de poids minimum
    matching = nx.algorithms.matching.min_weight_matching(G_odd)

    # 4. Multigraphe avec les arêtes de T + matching
    multigraph = nx.MultiGraph()
    multigraph.add_edges_from(T.edges(data=True))
    for u, v in matching:
        multigraph.add_edge(u, v, weight=G[u][v]['weight'])

    # 5. Tour eulérien
    euler_circuit = list(nx.eulerian_circuit(multigraph, source=depart))

    # 6. Transformer en tour hamiltonien (supprimer les répétitions de sommets)
    visited = set()
    hamiltonian_path = []
    for u, v in euler_circuit:
        if u not in visited:
            visited.add(u)
            hamiltonian_path.append(u)
    hamiltonian_path.append(hamiltonian_path[0])  # on boucle pour faire un tour

    return list(reversed(hamiltonian_path))