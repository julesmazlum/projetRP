from graphe import nearest_neighbor, construire_G_prime, dijkstra_connues
from christofides import christofides
import networkx as nx

def CNN(graphe, depart, bloquees):
    """
    Implémentation de l'algorithme CNN pour le problème CCTP
    """
    # Christofides 
    tour = christofides(graphe, depart)
    
    if tour[-1] == tour[0]:
        tour = tour[:-1]  #on retire le retour au départ

    n = len(tour)
    non_visites = set(tour)
    non_visites.remove(depart)
    parcours_complet = [depart]
    current = depart
    i = tour.index(current)
    visited_in_phase1 = {depart}

    while non_visites:
        next_index = (i + 1) % n
        next_sommet = tour[next_index]

        if next_sommet not in non_visites:
            i = next_index
            continue

        if graphe.is_blocked(current, next_sommet) or (current, next_sommet) in bloquees:
            # accessible non visité 
            found = False
            for skip in range(2, n):
                candidate_index = (i + skip) % n
                candidate = tour[candidate_index]
                if (candidate in non_visites and 
                    not graphe.is_blocked(current, candidate) and 
                    (current, candidate) not in bloquees):
                    next_sommet = candidate
                    next_index = candidate_index
                    found = True
                    break
            
            if not found:
                # chemin via Dijkstra
                try:
                    path, _ = dijkstra_connues(graphe, current, next_sommet, bloquees, visited_in_phase1)
                    for node in path[1:]:
                        if node in non_visites:
                            non_visites.remove(node)
                        parcours_complet.append(node)
                        visited_in_phase1.add(node)
                    current = path[-1]
                    i = tour.index(current)
                    continue
                except:
                    # sommet suivant
                    i = next_index
                    continue

        if next_sommet in non_visites:
            parcours_complet.append(next_sommet)
            non_visites.remove(next_sommet)
            visited_in_phase1.add(next_sommet)
        
        current = next_sommet
        i = tour.index(current)

    # sommets non visités
    U = non_visites
    if U:
        Us = U.union({depart})
        G_prime, developpements = construire_G_prime(graphe, Us, bloquees, visited_in_phase1)
        
        # G_prime valide
        for u in G_prime.sommets:
            for v in G_prime.sommets:
                if u != v and not G_prime.is_blocked(u, v) and (u, v) not in G_prime.arretes:
                    raise ValueError(f"Arête manquante {u}-{v} dans G_prime")

        chemin_nn = nearest_neighbor(G_prime, depart)
        
        # Développer 
        chemin_developpe = []
        for i in range(len(chemin_nn)-1):
            u, v = chemin_nn[i], chemin_nn[i+1]
            if (u, v) in developpements:
                # Vérifier que le chemin développé est valide
                path = developpements[(u, v)]
                for node_from, node_to in zip(path[:-1], path[1:]):
                    if graphe.is_blocked(node_from, node_to):
                        raise ValueError(f"Arête bloquée {node_from}-{node_to} dans le chemin développé")
                chemin_developpe += path[1:]  # Ne pas répéter le premier nœud
            else:
                if graphe.is_blocked(u, v):
                    raise ValueError(f"Arête bloquée {u}-{v} dans le chemin NN")
                chemin_developpe.append(v)
        
        parcours_complet += chemin_developpe

    # Retour au départ 
    if parcours_complet[-1] != depart:
        if not graphe.is_blocked(parcours_complet[-1], depart):
            parcours_complet.append(depart)
        else:
            # chemin valide
            try:
                return_path, _ = dijkstra_connues(graphe, parcours_complet[-1], depart, bloquees, visited_in_phase1)
                parcours_complet += return_path[1:]
            except:
                raise ValueError("Aucun chemin de retour vers le départ trouvé")

    return parcours_complet

