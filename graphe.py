class Graphe:
    def __init__(self, sommets, arretes):
        self.sommets = sommets
        self.arretes = arretes
        self.bloquees = set()

    def bloquer_arrete(self, u, v):
        self.bloquees.add((u, v))
        self.bloquees.add((v, u))

    def est_bloquee(self, u, v):
        return (u, v) in self.bloquees

    def voisins(self, sommet):
        return [v for v in self.sommets if v != sommet and not self.est_bloquee(sommet, v)]

    def cout(self, u, v):
        return self.arretes.get((u, v), float('inf'))

    def afficher_graphe(self):
        print("Sommets du graphe :")
        for sommet in self.sommets:
            print(f" - {sommet}")
        
        print("\nArêtes du graphe :")
        deja_vu = set()
        for (u, v), cout in self.arretes.items():
            if (v, u) not in deja_vu:
                statut = "bloquée" if self.est_bloquee(u, v) else "libre"
                print(f" {u} -- {v} (coût: {cout}, {statut})")
                deja_vu.add((u, v))

