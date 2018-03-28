from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, l):
        self.matr = deepcopy(l)

    def __str__(self):
        strRep = ""
        amount = 0
        for matr in self.matr:
            if amount != 0:
                strRep += "\n"
            new_str = "\t".join(str(elem) for elem in matr)
            strRep += new_str
            amount += 1
        return strRep

    def size(self):
        return len(self.matr), len(self.matr[0])

    def __add__(self, other):
        if len(self.matr) == len(other.matr):
            lenght = len(self.matr[0])
            for elem in self.matr:
                if len(elem) != lenght:
                    raise MatrixError(self, other)
            for elem2 in other.matr:
                if len(elem2) != lenght:
                    raise MatrixError(self, other)
            result = []
            numbers = []
            for i in range(len(self.matr)):
                for j in range(len(self.matr[0])):
                    summa = other.matr[i][j] + self.matr[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.matr[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.newMatr = deepcopy(self.matr)
            for i in range(len(self.matr)):
                for j in range(len(self.matr[0])):
                    self.newMatr[i][j] = self.matr[i][j] * other
            return '\n'.join('\t'.join(map(str, e)) for e in self.newMatr)

    def transpose(self):
        t_matrix = list(zip(*self.matr))
        self.matr = t_matrix
        return Matrix(t_matrix)

    def transposed(self):
        t_matrix = list(zip(*self.matr))
        return Matrix(t_matrix)

    __rmul__ = __mul__

exec(stdin.read())
