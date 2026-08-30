# CCTP — Covering Canadian Traveller Problem : CR vs CNN

Projet M1 ANDROIDE 2025 — UE Résolution de Problèmes (RP), Sorbonne Université. Auteurs : Jules MAZLUM, Aurélien CHAMBOLLE-SOLAZ.

## Description / Sujet

Ce dépôt contient l'implémentation et la comparaison de deux stratégies de résolution pour le **Covering Canadian Traveller Problem (CCTP)**.

Le problème étudié est une généralisation du célèbre problème du voyageur de commerce (TSP), avec une contrainte d'incertitude dynamique (d'où le nom « voyageur canadien », en référence aux routes enneigées imprévisibles) :

- **Le défi** : un voyageur doit visiter tous les sommets d'un graphe routier et revenir à son point de départ le plus rapidement possible.
- **La contrainte d'incertitude** : contrairement à un GPS classique, le voyageur connaît la carte complète (distances, connexions), mais certaines routes peuvent être bloquées. Un blocage n'est découvert qu'en arrivant à un sommet adjacent à la route concernée, et une fois découvert, il reste bloqué définitivement.

L'objectif est de développer des algorithmes « en ligne » capables d'adapter l'itinéraire en temps réel pour minimiser le coût total du trajet.

### Algorithmes implémentés

**1. Algorithme CR (Cyclic Routing)**
Repose sur la tentative répétée de suivre une tournée optimale planifiée :
- Initialisation : calcul d'un tour complet via l'algorithme de **Christofides**.
- Stratégie : le voyageur suit le tour ; si l'arête (vi, vi+1) est bloquée, il tente un raccourci vers vi+2, puis vi+3, etc., jusqu'à trouver un passage.
- L'algorithme procède par itérations (tours) jusqu'à ce que tous les sommets soient visités.

**2. Algorithme CNN (Christofides + Nearest Neighbor)**
Approche hybride en deux phases pour optimiser la fin de parcours :
- Phase d'exploration : comme pour CR, suit un tour de Christofides avec raccourcis en cas de blocage.
- Phase d'optimisation locale : une fois revenu au départ ou bloqué, construit un graphe réduit G′ contenant uniquement les sommets non visités et le départ.
- Phase de terminaison : termine la visite en appliquant l'algorithme du plus proche voisin sur ce graphe réduit, en utilisant les plus courts chemins connus (« safe paths »).

## Structure du dépôt

```text
.
├── src/
│   ├── main.py                    Script principal : lance les simulations, affiche les itinéraires et compare les performances
│   ├── graphe.py                  Gestion du graphe, des poids et simulation de la découverte dynamique des arêtes bloquées
│   ├── christofides.py            Implémentation de l'algorithme de Christofides (base d'approximation pour le TSP)
│   ├── cr.py                      Logique de l'algorithme de Routage Cyclique (CR)
│   ├── cnn.py                     Logique de l'algorithme CNN
│   ├── stats.py                   Statistiques : coût total et rapport de compétitivité
│   └── tests/
│       └── exemples_graphes.py    Jeux de données du sujet et graphes aléatoires
├── projet_RP_2025.pdf             Énoncé du sujet
└── RP-CHAMBOLLE_SOLAZ-MAZLUM.pdf  Rapport du projet
```

## Installation / Prérequis

Projet codé en Python. Installer les dépendances via pip :

```bash
pip install networkx matplotlib
```

## Utilisation

Depuis `src/`, lancer les simulations et comparer les deux algorithmes :

```bash
python main.py
```

## Résultats principaux

- `main.py` exécute CR et CNN sur les instances définies dans `tests/exemples_graphes.py` (jeux de données du sujet et graphes aléatoires).
- `stats.py` calcule le coût total et le rapport de compétitivité de chaque algorithme, permettant de les comparer empiriquement.
- Le détail des résultats est présenté dans le rapport `RP-CHAMBOLLE_SOLAZ-MAZLUM.pdf`.

## Auteurs

- Jules MAZLUM
- Aurélien CHAMBOLLE-SOLAZ
