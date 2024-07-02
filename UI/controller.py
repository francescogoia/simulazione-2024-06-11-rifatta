import time

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model





    def handleGrafo(self, e):
        self._model._crea_grafo()
        nNodi, nArchi = self._model.get_dettagli_grafo()
        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text(f"Grafo correttamente creato. Il grafo ha {nNodi} nodi e {nArchi} archi."))
        self._pesoMax, self._pesoMin = self._model.get_max_min()
        self._view.txt_result1.controls.append(ft.Text(f"Informazioni sui pesi degli archi: valore minimo = {self._pesoMin}, valore massimo = {self._pesoMax}"))
        self._view._txtInSoglia.disabled = False
        self._view._btn_conta_archi.disabled = False
        self._view._btn_cammino.disabled = False
        self._view.update_page()

    def handleContaArchi(self, e):
        soglia = self._view._txtInSoglia.value
        try:
            floatSoglia = float(soglia)
        except ValueError:
            self._view.txt_result2.controls.clear()
            self._view.txt_result2.controls.append(ft.Text(f"Errore, inserire un valore numerico in 'Soglia'."))
            self._view.update_page()
            return
        if self._pesoMin <= floatSoglia <= self._pesoMax:
            self._soglia = floatSoglia
            nArchiMaggiore, nArchiMinore = self._model._conta_archi(floatSoglia)
            self._view.txt_result2.controls.clear()
            self._view.txt_result2.controls.append(ft.Text(f"Numero di archi con peso maggiore della soglia {nArchiMaggiore}\n"
                                                           f"Numero di archi con peso minore della soglia {nArchiMinore}"))
            self._view.update_page()
        else:
            self._view.txt_result2.controls.clear()
            self._view.txt_result2.controls.append(ft.Text(f"Errore, inserire un valore di 'Soglia' compreso tra il valore minimo ed il valore massimo."))
            self._view.update_page()
            return

    def handleCammino(self, e):
        percorso, lunghezza = self._model._handle_cammino(self._soglia)
        self._view.txt_result3.controls.clear()
        self._view.txt_result3.controls.append(ft.Text(f"Trovato cammino di lunghezza {lunghezza}:"))
        for p in percorso:
            self._view.txt_result3.controls.append(ft.Text(f"{p[0]} --> {p[1]}: {p[2]}"))
        self._view.update_page()

