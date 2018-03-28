from copy import deepcopy
from sys import stdin


class Matrix(list):
    def __init__(self, l):
        self.matr = deepcopy(l)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, elem)) for elem in self.matr)

    def size(self):
        sp = (len(self.matr), len(self.matr[0]))
        return sp

    def __add__(self, other):
        for i in range(len(self.matr)):
            for j in range(len(self.matr[0])):
                self.matr[i][j] = self.matr[i][j] + other.matr[i][j]
        return '\n'.join('\t'.join(map(str, elem)) for elem in self.matr)

    def __mul__(self, other):
        self.newMatr = deepcopy(self.matr)
        for i in range(len(self.matr)):
            for j in range(len(self.matr[0])):
                self.newMatr[i][j] = self.matr[i][j] * other
        return '\n'.join('\t'.join(map(str, elem)) for elem in self.newMatr)

    def __rmul__(other, self):
        other.newMatr = deepcopy(other.matr)
        for i in range(len(other.matr)):
            for j in range(len(other.matr[0])):
                other.newMatr[i][j] = self * other.matr[i][j]
        return '\n'.join('\t'.join(map(str, elem)) for elem in other.newMatr)
exec(stdin.read())
