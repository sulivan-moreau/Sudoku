# Utilisation de la classe Sudoku directement depuis sudoku_backtracking.py
from sudoku_backtracking import Sudoku

def lire_depuis_fichier(nom_fichier):
    grille = []
    with open(nom_fichier, 'r') as fichier:
        for ligne in fichier:
            grille.append([0 if c == '_' else int(c) for c in ligne.strip()])
    return grille

if __name__ == "__main__":
    grille = lire_depuis_fichier('evil_sudoku.txt')  # Assurez-vous que sudoku.txt est présent dans le même répertoire
    sudoku = Sudoku(grille)
    if sudoku.resoudre():
        sudoku.afficher()
    else:
        print("Pas de solution trouvée.")
