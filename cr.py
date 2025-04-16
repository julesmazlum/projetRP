from christofides import *

def CR(graphe, depart, verbose=False):
    """
    Implémentation de l'algorithme CR (Routage Cyclique)
    """

    # Fonction d'affichage avec verbose
    def log(msg):
        if verbose:
            print(f"[CR] {msg}")
    #

    # Récupération du tour de christofide
    tour = christofides(graphe, depart)
    log(f"Tour initial généré par Christofides: {tour}")

    # Supression du dernier élément qui est le départ
    if tour[-1] == tour[0]:
        tour = tour[:-1]
        log(f"Retrait du retour au point de départ: {tour}")


    # Données
    n = len(tour)

    # Ensemble des sommets non visités
    non_visites = set(tour)
    non_visites.remove(depart)

    # Ensemble des arêtes bloquées
    bloquees_totales = set()

    # Le parcours retourné
    parcours_complet = [depart]

    # Booleans utiles
    retour_ajoute = True
    inverser_sens = False

    # Paramètres de départ
    # Sommet courant
    current = depart
    sens = 1

    log(f"Début du routage cyclique depuis {depart}")
    log(f"Sommets à visiter: {non_visites}")

    # Tant qu'il reste des sommets à visiter
    while non_visites:
        # Parcours pour cette iteration
        iteration_path = [current]
        # Sommets visités pour cette iteration
        visited_this_round = set()
        # arête bloquées pour cette itération
        blocages_cette_iter = set()

        # L'index du sommet courant
        i = tour.index(current)

        # Le sommet de départ pour l'iteration, pour pouvoir détecter une boucle complète
        init = current

        log("")
        log(f"Nouvelle itération à partir de {current} dans le sens {'horaire' if sens == 1 else 'anti-horaire'}")

        while True:
            # Sommet suivant
            next_index = (i + sens) % n
            next_sommet = tour[next_index]

            # Si le sommet suivant == le sommet de départ, alors on a fait une boucle complète -> itération finie
            if next_sommet == init:
                log("Itération terminée. Fin de boucle.")
                break

            # Si le sommet suivant a déjà été visité, alors on passe au suivant
            if next_sommet not in non_visites:
                log(f"{next_sommet} déjà visité. On continue.")
                i = next_index
                continue
            # Sinon on essaye de s'y déplacer
            else:
                log(f"Tentative de passage en {next_sommet}")

            # Si l'arête entre le sommet courant et le sommet suivant est bloqué, alors on essaye de trouver un shortcut
            if graphe.est_bloquee(current, next_sommet):
                log(f"Blocage détecté entre {current} et {next_sommet}")
                # Blocage ajouté
                blocages_cette_iter.add((current, next_sommet))
                trouve = False

                # Index du sommet courant
                start = tour.index(current)
                # Index du sommet suivant
                end = tour.index(next_sommet)
                tentative = None

                # S'il existe des sommets internes entre le sommet courant et le sommet suivant
                # Alors on cherche un shortcut parmis ceux la
                if abs(start - end) > 1:
                    tentative = chercher_alternative(
                        tour, current, sens, graphe, non_visites, start_index=start,
                        end_index=end, next_sommet_original=next_sommet, 
                        bloquees_totales=bloquees_totales, verbose=verbose
                    )
                # S'il n'existe pas de sommets entre les deux
                # OU si aucun shortcut n'a été trouvé
                # Alors on essaye d'en trouver un entre le sommet suivant et la fin de la boucle
                if not tentative:
                    tentative = chercher_alternative(
                        tour, current, sens, graphe, non_visites, start_index=i,
                        end_index=tour.index(init), skip_visited=True,
                        next_sommet_original=next_sommet,
                        bloquees_totales=bloquees_totales, verbose=verbose
                    )

                # Si un shortcut a été trouvé, le sommet suivant est le shortcut
                if tentative:
                    next_sommet = tentative
                    trouve = True
                # Sinon on n'a pas pu terminer notre boucle donc, sens opposé
                else:
                    log("Aucune alternative trouvée. Inversion du sens à la prochaine itération.")
                    inverser_sens = True
                    break

            # On se déplace au sommet suivant (MAJ des données)
            log(f"Déplacement vers {next_sommet}")
            iteration_path.append(next_sommet)
            non_visites.discard(next_sommet)
            visited_this_round.add(next_sommet)
            current = next_sommet
            i = tour.index(current)

            # Si tous les sommets ont étés visités.
            # Alors on ajoute un dernier sommet qui est le départ (le boolean passe permet de le faire une unique fois)
            if len(non_visites) == 0 and retour_ajoute:
                log("")
                log(f"Tous les sommets ont été visités. Réajout du départ ({depart}) pour retour.")
                non_visites.add(depart)
                retour_ajoute = False

        # Si aucune solution trouvée
        if not visited_this_round:
            log("Aucun sommet visité dans cette itération. Fin.")
            break

        # MAJ des données globales
        parcours_complet += iteration_path[1:]
        bloquees_totales.update(blocages_cette_iter)

        log("Fin de parcours de l'itération !")
        log(f"Chemin parcouru jusque-là : {parcours_complet}")
        log(f"Arêtes bloquées cumulées : {bloquees_totales}")
        log(f"Sommets restants : {non_visites}")

        # Si on a pas réussi à atteindre tous les sommets du tour (donc inverser_sens == True), alors on inverse le sens
        if non_visites:
            sens = -1 if inverser_sens else 1
            #sens *= -1 if inverser_sens else 1
            log(f"Sens: {'anti-horaire' if sens == -1 else 'horaire'}")
            log("—" * 50)
            inverser_sens = False

    # Parcours complet
    log(f"Parcours complet: {parcours_complet}")
    return parcours_complet


def chercher_alternative(tour, current, sens, graphe, non_visites, start_index, end_index=None, 
                         skip_visited=False, next_sommet_original=None, bloquees_totales=None,
                         verbose=False):
    """
    Recherche de sommet alternatif en cas de blocage
    Parmi sommets internes/ externes
    """

    # Fonction d'affichage avec verbose
    def log(msg):
        if verbose:
            print(f"[CA] {msg}")
    #

    # Données
    n = len(tour)
    log(f"Recherche {f"interne d'alternative depuis {current} vers {next_sommet_original}" if not skip_visited else f"externe d'alternative depuis {current}"}")


    for j in range(2, n):
        # Index sommet tentatif
        # Recherche externe j in range(2,n), car on déjà testé le +1
        if skip_visited:
            tentative_index = (start_index + j * sens) % n
        # Recherche interne j in range(1,n), on veut tester +1
        else:
            tentative_index = (start_index + (j-1) * sens) % n 

        # Si aucun sommet n'est trouvé
        # - en interne : sommet tentatif == sommet suivant
        # - en externe : sommet tentatif == sommet de fin de boucle
        if tentative_index == end_index:
            log("Fin de la recherche atteinte.")
            break

        # Sommet tentatif
        sommet_tentatif = tour[tentative_index]
        log(f"Tentative de passage en {sommet_tentatif}")

        # Pendant une recherche externe, pas le droit d'utiliser des sommets déjà vistés
        if skip_visited and sommet_tentatif not in non_visites:
            log(f"{sommet_tentatif} déjà visité (recherche externe).")
            continue

        # Lors d'une recherche interne, si l'arête entre le sommet tentatif et le sommet suivant est bloqué
        # Inutile d'y aller
        if bloquees_totales and (sommet_tentatif, next_sommet_original) in bloquees_totales:
            log(f"{sommet_tentatif} -> {next_sommet_original} déjà testé sans succès.")
            continue

        # Sommet tentatif possible
        if not graphe.est_bloquee(current, sommet_tentatif):
            log(f"Alternative valide trouvée: {sommet_tentatif}")
            return sommet_tentatif
        # Sinon pas trouvé
        else:
            log(f"Chemin bloqué entre {current} et {sommet_tentatif}")
            if bloquees_totales is not None:
                bloquees_totales.add((current, sommet_tentatif))

    log("Aucune alternative trouvée.")
    return None
