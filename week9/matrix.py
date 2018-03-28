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
exec(stdin.read())
