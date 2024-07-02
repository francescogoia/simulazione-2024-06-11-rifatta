from model.model import Model

myModel = Model()
myModel._crea_grafo()
print(myModel.get_dettagli_grafo())
max, min = myModel.get_max_min()
print(max, min)
path, lunghezza = myModel._handle_cammino(3)
print("Lunghezza: ", lunghezza)
for p in path:
    print(p)
