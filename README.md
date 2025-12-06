# Projet RP : Le Problème du Voyageur Canadien Couvrant (CCTP)

Ce dépôt contient l'implémentation et la comparaison de stratégies de résolution pour le **Covering Canadian Traveller Problem (CCTP)**, réalisé dans le cadre du module de Recherche Opérationnelle (Projet RP 2025).

## Description du Problème

Le problème étudié est une généralisation du célèbre "Voyageur de Commerce" (TSP), mais avec une contrainte d'incertitude dynamique (d'où le nom "Voyageur Canadien", en référence aux routes enneigées imprévisibles).

### Le défi
Un voyageur doit visiter **tous les sommets** d'un graphe routier et revenir à son point de départ le plus rapidement possible.

### La contrainte d'incertitude
Contrairement à un GPS classique :
* Le voyageur connaît la carte complète (distances, connexions), mais **certaines routes peuvent être bloquées**.
* Un blocage n'est **découvert qu'en arrivant** à un sommet adjacent à la route concernée.
* Une fois une route découverte bloquée, elle le reste définitivement.

L'objectif est de développer des algorithmes "en ligne" capables d'adapter l'itinéraire en temps réel pour minimiser le coût total du trajet.

## Algorithmes Implémentés

Ce projet met en compétition deux heuristiques décrites dans la littérature :

### 1. Algorithme CR (Cyclic Routing)
Cette approche repose sur la tentative répétée de suivre une tournée optimale planifiée.
* **Initialisation :** Calcul d'un tour complet via l'algorithme de **Christofides**.
* **Stratégie :** Le voyageur suit le tour. Si l'arête $(v_i, v_{i+1})$ est bloquée, il tente un "raccourci" vers $v_{i+2}$, puis $v_{i+3}$, etc., jusqu'à trouver un passage.
* **Cycles :** L'algorithme procède par itérations (tours) jusqu'à ce que tous les sommets soient visités.

### 2. Algorithme CNN (Christofides + Nearest Neighbor)
Une approche hybride en deux phases pour optimiser la fin de parcours.
* **Phase 1 (Exploration) :** Comme pour CR, l'algorithme commence par suivre un tour de Christofides avec des raccourcis en cas de blocage.
* **Phase 2 (Optimisation locale) :** Une fois revenu au départ ou bloqué, l'algorithme construit un graphe réduit $G'$ contenant uniquement les sommets non visités et le départ.
* **Phase 3 (Terminaison) :** Il termine la visite en appliquant l'algorithme du **Plus Proche Voisin (Nearest Neighbor)** sur ce graphe réduit, en utilisant les plus courts chemins connus ("safe paths").

## Structure du Projet

* `main.py` : Script principal. Lance les simulations, affiche les itinéraires et compare les performances.
* `graphe.py` : Gestion du graphe, des poids et simulation de la découverte dynamique des arêtes bloquées.
* `christofides.py` : Implémentation de l'algorithme de Christofides (base d'approximation pour le TSP).
* `cr.py` : Logique de l'algorithme de Routage Cyclique.
* `cnn.py` : Logique de l'algorithme CNN.
* `stats.py` : Module de statistiques pour évaluer le coût total et le rapport de compétitivité.
* `tests/` : Contient `exemples_graphes.py` avec les jeux de données du sujet et des graphes aléatoires.

## Installation et Prérequis

Le projet est codé en Python. Les dépendances principales sont utilisées pour la manipulation de graphes et la visualisation.

Installez les dépendances via pip :

```bash
pip install networkx matplotlib
```

## Auteurs

* **Jules MAZLUM**
* **Aurélien CHAMBOLLE-SOLAZ**
