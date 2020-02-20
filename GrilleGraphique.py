from Grille import *
from tkinter import *
from CelluleGraphique import *

class GrilleGraphique(Grille):
    def __init__(self, base_model):
        self.model = []
        self.generate_canvas()

        self.generate_grid(base_model)

        self.fenetre.mainloop()

    def generate_canvas(self):
        self.fenetre = Tk()
        self.fenetre.geometry('450x450')
        self.canvas = Canvas(self.fenetre, width=450, height=450, bg='white')
        self.canvas.pack()
    
    def generate_grid(self, base_model):
        
        
        for i, ligne in enumerate(base_model):
            self.model.append([])
            width = 1
            
            if i % 3 == 0:
                width = 3

            self.canvas.create_line((i * 50, 450), (i * 50, 0), width=width)
            for j, cellule in enumerate(ligne):
                self.model[i].append(CelluleGraphique(j, i, cellule, self))
                width = 1
            
                if j%3 == 0:
                    width = 3

                self.canvas.create_line((0, j * 50), (450, j * 50), width=width)
