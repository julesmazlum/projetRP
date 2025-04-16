from christofides import *

def CR(graphe, depart):
    """
    Implémentation de l'algorithme CR (Routage Cyclique)
    """
    tour = christofides(graphe, depart)

    if tour[-1] == tour[0]:
        tour = tour[:-1]

    n = len(tour)
    passe = True
    b = False
    non_visites = set(tour)
    non_visites.remove(depart)
    parcours_complet = [depart]
    bloquees_totales = set()
    current = depart
    sens = 1
    

    while non_visites:
        iteration_path = [current]
        visited_this_round = set()
        blocages_cette_iter = set()

        i = tour.index(current)
        init = current

        while True:
            next_index = (i + sens) % n
            next_sommet = tour[next_index]

            if next_sommet == init:
                break

            if next_sommet not in non_visites:
                i = next_index
                continue

            if graphe.est_bloquee(current, next_sommet):
                blocages_cette_iter.add((current, next_sommet))
                trouve = False

                start = tour.index(current)
                end = tour.index(next_sommet)
                tentative = None
                if abs(start - end) > 1:
                    tentative = chercher_alternative(
                        tour, current, sens, graphe, non_visites, start_index=start,
                        end_index=tour.index(next_sommet),
                        next_sommet_original=next_sommet, bloquees_totales=bloquees_totales
                    )
                if not tentative:
                    tentative = chercher_alternative(
                        tour, current, sens, graphe, non_visites, start_index=i,
                        end_index=tour.index(init), skip_visited=True,
                        next_sommet_original=next_sommet, bloquees_totales=bloquees_totales
                    )
                if tentative:
                    next_sommet = tentative
                    trouve = True
                else:
                    b = True
                    break
            
            iteration_path.append(next_sommet)
            non_visites.discard(next_sommet)
            visited_this_round.add(next_sommet)
            current = next_sommet
            i = tour.index(current)

            if len(non_visites) == 0 and passe:
                non_visites.add(depart)
                passe = False

        if not visited_this_round:
            break

        parcours_complet += iteration_path[1:]
        bloquees_totales.update(blocages_cette_iter)

        if non_visites:
            if not b:
                sens = 1
            else:
                sens = -1
            b = False

    return parcours_complet


def chercher_alternative(tour, current, sens, graphe, non_visites, start_index, end_index=None, 
                         skip_visited=False, next_sommet_original=None, bloquees_totales=None):
    n = len(tour)
    for j in range(1, n):
        tentative_index = (start_index + j * sens) % n
        if tentative_index == end_index:
            break
        sommet_tentatif = tour[tentative_index]

        if skip_visited and sommet_tentatif not in non_visites:
            continue

        if bloquees_totales and (sommet_tentatif, next_sommet_original) in bloquees_totales:
            continue

        if not graphe.est_bloquee(current, sommet_tentatif):
            return sommet_tentatif

        else:
            if bloquees_totales is not None:
                bloquees_totales.add((current, sommet_tentatif))
    
    return None


