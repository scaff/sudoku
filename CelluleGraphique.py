from tkinter import *
import tkinter.font as tkFont
from Cellule import *

class CelluleGraphique(Cellule):
    def __init__(self, x, y, valeur, grille):
        super().__init__(x, y, valeur, grille)

        canvas = self.grille.canvas
        if (valeur != 0): state = 'disabled'
        else : state = 'normal'
        value = StringVar()
        entry = Entry(
            canvas,
            width=1,
            relief='flat',
            justify='center',
            state=state,
            textvariable=value,
            disabledbackground='white',
            font=tkFont.Font(size=20))
        if (valeur != 0): value.set(str(valeur))
        canvas.create_window(self.x * 50 + 15, self.y * 50 + 8, anchor='nw', window=entry)

        entry.bind('<KeyPress>', self.is_value_valide)

    def is_value_valide(self, event):
        # try:
        if super().is_value_valide(event.char):
            self.grille.model[self.y][self.x] = int(event.char)
        # except:
        #     pass
