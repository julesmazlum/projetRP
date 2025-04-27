import networkx as nx
import matplotlib.pyplot as plt

class Graphe:
    def __init__(self, sommets, arretes):
        self.sommets = sommets
        self.arretes = arretes
        self.bloquees = set()

    def block_arrete(self, u, v):
        self.bloquees.add((u, v))
        self.bloquees.add((v, u))

    def is_blocked(self, u, v):
        return (u, v) in self.bloquees

    def voisins(self, sommet):
        return [v for v in self.sommets if v != sommet and not self.is_blocked(sommet, v)]

    def cout(self, u, v):
        return self.arretes.get((u, v), float('inf'))
    
    def draw_graph(self, parcours=None, titre="Graphe"):
        G = nx.Graph()
    
        # Add all edges
        for (u, v), weight in self.arretes.items():
            G.add_edge(u, v, weight=weight)
    
        # Positions
        if hasattr(self, 'pos') and self.pos:
            pos = self.pos
        else:
            pos = nx.spring_layout(G)
    
        edge_labels = nx.get_edge_attributes(G, 'weight')
    
        plt.figure(figsize=(8, 6))
    
        # 1. Draw normal (non-blocked) edges first
        normal_edges = [(u, v) for (u, v) in G.edges() if not self.is_blocked(u, v)]
        nx.draw_networkx_edges(G, pos, edgelist=normal_edges, edge_color='black', width=1)
    
        # 2. Draw blocked edges on top
        blocked_edges = [(u, v) for (u, v) in G.edges() if self.is_blocked(u, v)]
        if blocked_edges:
            nx.draw_networkx_edges(
                G, pos, edgelist=blocked_edges,
                edge_color='grey', style='dashed', width=2.5
            )
    
        # 3. Draw nodes and labels
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
        nx.draw_networkx_labels(G, pos, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
        # 4. Draw parcours if given
        if parcours:
            path_edges = list(zip(parcours[:-1], parcours[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
    
        plt.title(titre)
        plt.axis('off')
        plt.show()


        
def nearest_neighbor(graphe, start):
    visités = {start}
    chemin = [start]
    courant = start

    while len(visités) < len(graphe.sommets):
        voisins_non_visités = [v for v in graphe.voisins(courant) if v not in visités]
        if not voisins_non_visités:
            break  # plus de voisins accessibles

        prochain = min(voisins_non_visités, key=lambda v: graphe.cout(courant, v))
        chemin.append(prochain)
        visités.add(prochain)
        courant = prochain
    return chemin

def dijkstra_connues(graphe, start, end, bloquees, visites):
    """ Version de Dijkstra pour les arêtes connues """
    G_nx = nx.Graph()
    for u in graphe.sommets:
        for v in graphe.sommets:
            if u != v and not graphe.is_blocked(u, v) and ((u in visites) or (v in visites)):
                poids = graphe.cout(u, v)
                G_nx.add_edge(u, v, weight=poids)
    
    if not nx.has_path(G_nx, start, end):
        raise ValueError(f"Aucun chemin de {start} à {end} avec les arêtes connues")
    
    return nx.dijkstra_path(G_nx, start, end, weight='weight'), nx.dijkstra_path_length(G_nx, start, end, weight='weight')

def construire_G_prime(graphe, Us, Eb, visites):
    developpements = {}
    arretes_G_prime = {}
    
    for u in Us:
        for v in Us:
            if u != v:
                chemin, cout = dijkstra_connues(graphe, u, v, Eb, visites)
                if chemin:
                    arretes_G_prime[(u, v)] = cout
                    arretes_G_prime[(v, u)] = cout  # Graphe non orienté
                    developpements[(u, v)] = chemin
                    developpements[(v, u)] = list(reversed(chemin))
    
    G_prime = Graphe(list(Us), arretes_G_prime)
    
    # Bloquer 
    for u in Us:
        for v in Us:
            if u != v and (u, v) not in arretes_G_prime:
                G_prime.block_arrete(u, v)
    
    return G_prime, developpements


