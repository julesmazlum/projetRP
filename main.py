from graphe import Graphe
from cr import CR
from cnn import CNN
from tests.exemples_graphes import exemple_graphe_1, exemple_graphe_2, exemple_graphe_3

if __name__ == "__main__":
    print("[TEST] Chargement du graphe exemple...")
    graphe, depart = exemple_graphe_3()
    #graphe.afficher_graphe()

    print("\n[CR] Exécution de l'algorithme CR...")
    resultat_cr = CR(graphe, depart, verbose=False)
    print("Itinéraire CR:", resultat_cr)
    graphe.draw_graph(parcours=resultat_cr, titre="Parcours CR")

    print("\n[CNN] Exécution de l'algorithme CNN...")
    resultat_cnn = CNN(graphe, depart, graphe.bloquees.copy()) 
    print("Itinéraire CNN:", resultat_cnn)
    graphe.draw_graph(parcours=resultat_cnn, titre="Parcours CNN")
    
    """for u, v in zip(resultat_cnn[:-1], resultat_cnn[1:]):
        if graphe.is_blocked(u, v):
            print(f"ERREUR : Arête bloquée {u}-{v} dans le parcours")
        elif (u, v) not in graphe.arretes:
            print(f"ERREUR : Arête inexistante {u}-{v}")"""

