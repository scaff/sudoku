from Cellule import *

class Grille:
    def __init__(self, base_model):
        self.model = []
        for i, ligne in enumerate(base_model):
            self.model.append([])
            for j, cellule in enumerate(ligne):
                self.model[i].append(Cellule(j, i, cellule, self))
