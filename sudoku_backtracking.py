class Sudoku:
    def __init__(self, grille):
        self.grille = grille
        self.original = [[bool(val) for val in row] for row in grille]

    def resoudre(self):
        for i in range(9):
            for j in range(9):
                if self.grille[i][j] == 0:
                    for c in range(1, 10):
                        if self.valide(i, j, c):
                            self.grille[i][j] = c
                            if self.resoudre():
                                return True
                            self.grille[i][j] = 0
                    return False
        return True

    def valide(self, i, j, c):
        bloc_i, bloc_j = 3 * (i // 3), 3 * (j // 3)
        for k in range(9):
            if self.grille[i][k] == c or self.grille[k][j] == c or self.grille[bloc_i + k // 3][bloc_j + k % 3] == c:
                return False
        return True

    def afficher(self):
        for i in range(9):
            for j in range(9):
                sep = '*' if self.original[i][j] else ' '
                print(f"{self.grille[i][j]}{sep}", end=' ')
            print()
