from graphe import Graphe
from cr import CR
from cnn import CNN
from tests.exemples_graphes import exemple_graphe_1

if __name__ == "__main__":
    print("[TEST] Chargement du graphe exemple...")
    graphe, depart = exemple_graphe_1()
    #graphe.afficher_graphe()

    print("\n[CR] Exécution de l'algorithme CR...")
    resultat_cr = CR(graphe, depart)
    print("Itinéraire CR:", resultat_cr)

    print("\n[CNN] Exécution de l'algorithme CNN...")
    resultat_cnn = CNN(graphe, depart)
    print("Itinéraire CNN:", resultat_cnn)
