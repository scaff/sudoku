from Cellule import *
from tkinter import *
import tkinter.font as tkFont

class CelluleGraphique(Cellule):
    def __init__(self, x, y, valeur, grille):
        super().__init__(x, y, valeur, grille)

        value = StringVar()
        if (valeur != 0): value.set(valeur)
        else: value.set('')
        self.element_graphique = Entry(
            self.grille.canvas,
            width=1,
            font=tkFont.Font(size=20),
            relief='flat',
            justify='center',
            state=self.get_entry_state(valeur),
            disabledbackground='white',
            textvariable=value
        )
        self.grille.canvas.create_window(self.x * 50 + 15, self.y * 50 + 8, anchor='nw', window=self.element_graphique)

        self.element_graphique.bind('<KeyRelease>', self.is_valeur_valide)

    def is_valeur_valide(self, event):
        try:
            int_value = int(event.char)
            is_valid = super().is_valeur_valide(int_value)
            if is_valid:
                self.valeur = int_value
        except:
            pass

    def get_entry_state(self, valeur):
        if (valeur != 0):
            return 'disabled'
        return 'normal'