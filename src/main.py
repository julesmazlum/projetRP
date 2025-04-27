from graphe import Graphe
from cr import CR
from cnn import CNN
from stats import stats
from tests.exemples_graphes import *

if __name__ == "__main__":
    print("[TEST] Chargement du graphe exemple...")
    graphe, depart = exemple_graphe_0()

    print("\n[CR] Exécution de l'algorithme CR...")
    resultat_cr = CR(graphe, depart, graphe.bloquees.copy(), verbose=False)
    print("Itinéraire CR:", resultat_cr)
    graphe.draw_graph(parcours=resultat_cr, titre="Parcours CR")

    print("\n[CNN] Exécution de l'algorithme CNN...")
    resultat_cnn = CNN(graphe, depart, graphe.bloquees.copy()) 
    print("Itinéraire CNN:", resultat_cnn)
    graphe.draw_graph(parcours=resultat_cnn, titre="Parcours CNN")

    print("\n\nPour le problème du sujet")
    graphe, depart = exemple_graphe_1()

    print("\n[CR] Exécution de l'algorithme CR...")
    resultat_cr = CR(graphe, depart, graphe.bloquees.copy(), verbose=False)
    print("Itinéraire CR:", resultat_cr)

    print("\n[CNN] Exécution de l'algorithme CNN...")
    resultat_cnn = CNN(graphe, depart, graphe.bloquees.copy()) 
    print("Itinéraire CNN:", resultat_cnn)

    print("\n\nQuelques statistiques")
    stats()

