from Grille import *
from tkinter import *

class GrilleGraphique(Grille):
    def __init__(self, base_model):
        self.fenetre = Tk()
        super().__init__(base_model)

        self.fenetre.mainloop()