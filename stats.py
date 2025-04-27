from cr import CR
from cnn import CNN
import time
from tests.exemples_graphes import *

def mesurer(fonction, graphe, depart):
    temps = []
    for _ in range(30):
        debut = time.perf_counter()
        fonction(graphe, depart, graphe.bloquees.copy())
        fin = time.perf_counter()
        temps.append(fin - debut)
    return sum(temps) / len(temps)

def cout(fonction, graphe, depart, known):
    parcours = fonction(graphe, depart, graphe.bloquees.copy(), known=known)
    cout_total = 0

    for i in range(len(parcours) - 1):
        u = parcours[i]
        v = parcours[i + 1]
        cout_total += graphe.arretes[(u, v)]

    return cout_total

def stats():

    graphes = [
        exemple_graphe_1(),
        exemple_graphe_1bis(),
        exemple_graphe_2(),
        exemple_graphe_2bis(),
        exemple_graphe_3(),
        exemple_graphe_3bis()
    ]

    # Temps

    print("\nTemps...")
    for i, (graphe, depart) in enumerate(graphes, 1):
        moyenne_CR = mesurer(CR, graphe, depart)
        moyenne_CNN = mesurer(CNN, graphe, depart)
        print(f"graphe {i}  ({len(graphe.sommets)} noeuds) : CR = {moyenne_CR:.6f}s, CNN = {moyenne_CNN:.6f}s")

    print("\nCout...")
    # Cout
    for i, (graphe, depart) in enumerate(graphes, 1):
        print(f"graphe {i} ({len(graphe.sommets)} noeuds)")

        coutParcoursCR = cout(CR, graphe, depart, known=False)
        print("[CR] Coût total du chemin sans connâitre les arêtes bloquées:", coutParcoursCR)
        
        coutParcoursCRKnown = cout(CR, graphe, depart, known=True)
        print("[CR] Coût total du chemin en connaissant les arêtes bloquées:", coutParcoursCRKnown)
        print(f"Ratio CR : {coutParcoursCR/coutParcoursCRKnown:.6f}\n")

        coutParcoursCNN = cout(CNN, graphe, depart, known=False)
        print("[CNN] Coût total du chemin sans connâitre les arêtes bloquées:", coutParcoursCNN)

        coutParcoursCNNKnown = cout(CNN, graphe, depart, known=True)
        print("[CNN] Coût total du chemin en connaissant les arêtes bloquées:", coutParcoursCNNKnown)
        print(f"Ratio CNN : {coutParcoursCNN/coutParcoursCNNKnown:.6f}\n")

    











