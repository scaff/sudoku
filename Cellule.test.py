import unittest
from Cellule import *
from Grille import *

class TestCellule(unittest.TestCase):
    def test_is_ligne_valide (self):
        base_model = [
            [ 8, 1, 3,  9, 0, 5,  7, 0, 6 ],
            [ 0, 5, 0,  0, 0, 0,  0, 0, 0 ],
            [ 4, 7, 2,  3, 6, 1,  8, 0, 5 ],
            
            [ 6, 0, 4,  0, 1, 0,  5, 0, 0 ],
            [ 0, 9, 5,  0, 3, 8,  0, 2, 1 ],
            [ 0, 0, 0,  0, 0, 2,  0, 0, 0 ],

            [ 0, 3, 0,  0, 7, 4,  0, 0, 9 ],
            [ 5, 4, 0,  0, 8, 0,  1, 0, 3 ],
            [ 0, 6, 7,  5, 9, 0,  0, 0, 4 ],
        ]
        grille = Grille(base_model)

        cellule = Cellule(0, 1, 0, grille)
        self.assertTrue(cellule.is_ligne_valide(1))
        self.assertFalse(cellule.is_ligne_valide(5))

        cellule2 = Cellule(3, 4, 0, grille)
        self.assertTrue(cellule2.is_ligne_valide(6))
        self.assertFalse(cellule2.is_ligne_valide(8))
    
    def test_is_colonne_valide (self):
        base_model = [
            [ 8, 1, 3,  9, 0, 5,  7, 0, 6 ],
            [ 0, 5, 0,  0, 0, 0,  0, 0, 0 ],
            [ 4, 7, 2,  3, 6, 1,  8, 0, 5 ],
            
            [ 6, 0, 4,  0, 1, 0,  5, 0, 0 ],
            [ 0, 9, 5,  0, 3, 8,  0, 2, 1 ],
            [ 0, 0, 0,  0, 0, 2,  0, 0, 0 ],

            [ 0, 3, 0,  0, 7, 4,  0, 0, 9 ],
            [ 5, 4, 0,  0, 8, 0,  1, 0, 3 ],
            [ 0, 6, 7,  5, 9, 0,  0, 0, 4 ],
        ]
        grille = Grille(base_model)

        cellule = Cellule(0, 1, 0, grille)
        self.assertTrue(cellule.is_colonne_valide(1))
        self.assertFalse(cellule.is_colonne_valide(5))

        cellule2 = Cellule(3, 4, 0, grille)
        self.assertTrue(cellule2.is_colonne_valide(6))
        self.assertFalse(cellule2.is_colonne_valide(9))

    def test_is_block_valide (self):
        base_model = [
            [ 8, 1, 3,  9, 0, 5,  7, 0, 6 ],
            [ 0, 5, 0,  0, 0, 0,  0, 0, 0 ],
            [ 4, 7, 2,  3, 6, 1,  8, 0, 5 ],
            
            [ 6, 0, 4,  0, 1, 0,  5, 0, 0 ],
            [ 0, 9, 5,  0, 3, 8,  0, 2, 1 ],
            [ 0, 0, 0,  0, 0, 2,  0, 0, 0 ],

            [ 0, 3, 0,  0, 7, 4,  0, 0, 9 ],
            [ 5, 4, 0,  0, 8, 0,  1, 0, 3 ],
            [ 0, 6, 7,  5, 9, 0,  0, 0, 4 ],
        ]
        grille = Grille(base_model)

        cellule = Cellule(0, 1, 0, grille)
        self.assertTrue(cellule.is_block_valide(6))
        self.assertFalse(cellule.is_block_valide(5))

        cellule2 = Cellule(3, 4, 0, grille)
        self.assertTrue(cellule2.is_block_valide(6))
        self.assertFalse(cellule2.is_block_valide(8))

if __name__ == '__main__':
    unittest.main()