from Grille import *
from CelluleGraphique import *
from tkinter import *

class GrilleGraphique(Grille):
    def __init__(self, base_model):
        self.fenetre = Tk()
        self.fenetre.geometry('450x450')
        self.canvas = Canvas(self.fenetre, width=450, height=450, bg='white')
        self.canvas.pack()

        self.generate_grid(base_model)

        self.fenetre.mainloop()

    def generate_grid(self, base_model):
        self.model = []
        for i, ligne in enumerate(base_model):
            self.model.append([])
            self.canvas.create_line(0, i * 50, 450, i * 50, width=self.get_line_width(i))
            for j, cellule in enumerate(ligne):
                self.model[i].append(CelluleGraphique(j, i, cellule, self))
                self.canvas.create_line(j * 50, 0, j * 50, 450, width=self.get_line_width(j))

    def get_line_width(self, i):
        if i % 3 == 0:
            return 3
        return 1