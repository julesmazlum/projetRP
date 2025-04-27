# Projet - RP

## Description
Ce projet compare deux algorithmes de routage sur graphe :
- **CR** (Routage Cyclique)
- **CNN** (Routage par voisinage)

## Dépendances
- Les librairies nécessaires :
  ```bash
  pip install networkx matplotlib
  ```

## Structure du projet
- `main.py` : script principal
- `graphe.py` : définition et manipulation des graphes
- `cr.py` : algorithme CR
- `cnn.py` : algorithme CNN
- `christofides.py` : algorithme de christophides
- `stats.py` : génération de statistiques
- `tests/exemples_graphes.py` : fichiers de graphes de test

## Exécution
Pour lancer :
```bash
python main.py
```

Ce que le programme fait :
1. charge un graphe d'exemple
2. exécute **CR** puis affiche l'itinéraire
3. exécute **CNN** puis affiche l'itinéraire
4. charge le graphe du sujet
5. refait CR + CNN
6. génére quelques statistiques finales