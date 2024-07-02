import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMap = {}
        self._grafo = nx.DiGraph()

    def _crea_grafo(self):
        self._nodes = DAO.getAllNodes()
        self._grafo.add_nodes_from(self._nodes)
        archi = DAO.getAllEdges()
        for a in archi:
            self._grafo.add_edge(a[0], a[1], weight=float(a[2]))

    def get_dettagli_grafo(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def get_max_min(self):
        a_min = 0
        a_max = 0
        for a in self._grafo.edges(data=True):
            peso_arco = a[2]["weight"]
            if peso_arco < a_min:
                a_min = peso_arco
            if peso_arco > a_max:
                a_max = peso_arco
        return a_max, a_min

    def _conta_archi(self, soglia):
        n_min = 0
        n_mag = 0
        for a in self._grafo.edges(data=True):
            peso_arco = a[2]["weight"]
            if peso_arco < soglia:
                n_min += 1
            if peso_arco > soglia:
                n_mag += 1
        return n_mag, n_min

    def _handle_cammino(self, soglia):
        self._bestPath = []
        self._bestLunghezza = 0
        for n in self._nodes:
            self._ricorsione(n, [], soglia)
        return self._bestPath, self._bestLunghezza

    def _ricorsione(self, nodo, parziale, soglia):
        peso_parziale = self._get_peso_parziale(parziale)
        if peso_parziale > self._bestLunghezza:
            self._bestLunghezza = peso_parziale
            self._bestPath = copy.deepcopy(parziale)
        successori = self._grafo.successors(nodo)
        for s in successori:
            peso_arco = self._grafo[nodo][s]["weight"]
            if peso_arco > soglia and self._filtro_arco(nodo, s, parziale):
                parziale.append((nodo, s, peso_arco))
                self._ricorsione(s, parziale, soglia)
                parziale.pop()

    def _get_peso_parziale(self, parziale):
        totP = 0
        for a in parziale:
            totP += a[2]
        return totP

    def _filtro_arco(self, nodo, s, parziale):
        for a in parziale:
            if a[:2] == (nodo, s):  # or a[:2] == (s, nodo): non serve perché il grafo è orientato
                return False
        return True
