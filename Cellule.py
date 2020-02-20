

class Cellule:
    def __init__(self, x, y, valeur, grille):
        self.x = x
        self.y = y
        self.valeur = valeur
        self.grille = grille

    def is_value_valide(self, valeur):
        to_return = self.is_colonne_valide(valeur) and self.is_ligne_valide(valeur) and self.is_block_valide(valeur)
        print(to_return)

        return to_return

    # def is_valeur_valide(valeur):
    def is_colonne_valide(self, valeur):
        for ligne in self.grille.model:
            if ligne[self.x].valeur == int(valeur):
                return False
        return True
        
    def is_ligne_valide(self, valeur):
        ligne = self.grille.model[self.y]
        for cellule in ligne:
            if cellule.valeur == int(valeur):
                return False
        return True

    def get_block_coordinate(self):
        return (self.x // 3 * 3), (self.y // 3 * 3)

    def is_block_valide(self, valeur):
        block_x, block_y = self.get_block_coordinate()
        for i in range(block_y, block_y + 3):
            for j in range(block_x, block_x + 3):
                if self.grille.model[i][j].valeur == int(valeur):
                    return False
        return True