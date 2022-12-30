#A
from sys import stdin

class Matrix:
    def __init__(self, values):
        self.v = [0] * len(values)
        for i in range(len(values)):
            self.v[i] = [0] * len(values[i])
            for j in range(len(values[i])):
                self.v[i][j] = values[i][j]

    def __str__(self):
        out = ""
        for i in range(len(self.v)):
            out += '\n'
            out += str(self.v[i][0])
            for j in range(1, len(self.v[i])):
                out += '\t' + str(self.v[i][j])
        return out[1:]

    def size(self):
        return (len(self.v), len(self.v[0]))

exec(stdin.read())

#B
from sys import stdin

class Matrix:
    def __init__(self, values):
        self.v = [0] * len(values)
        for i in range(len(values)):
            self.v[i] = [0] * len(values[i])
            for j in range(len(values[i])):
                self.v[i][j] = values[i][j]

    def __str__(self):
        out = ""
        for i in range(len(self.v)):
            out += '\n'
            out += str(self.v[i][0])
            for j in range(1, len(self.v[i])):
                out += '\t' + str(self.v[i][j])
        return out[1:]

    def size(self):
        return (len(self.v), len(self.v[0]))

    def __add__(self, other):
        result = [0] * len(self.v)
        for i in range(len(self.v)):
            result[i] = [0] * len(self.v[i])
            for j in range(len(self.v[i])):
                result[i][j] = self.v[i][j] + other.v[i][j]
        return Matrix(result)

    def __mul__(self, other):
        result = [0] * len(self.v)
        for i in range(len(self.v)):
            result[i] = [0] * len(self.v[i])
            for j in range(len(self.v[i])):
                result[i][j] = self.v[i][j] * other
        return Matrix(result)

    __rmul__ = __mul__

exec(stdin.read())

#C
from sys import stdin

class MatrixError(BaseException):
    def __init__(self, first, second):
        self.matrix1 = first
        self.matrix2 = second

class Matrix:
    def __init__(self, values):
        self.v = [0] * len(values)
        for i in range(len(values)):
            self.v[i] = [0] * len(values[i])
            for j in range(len(values[i])):
                self.v[i][j] = values[i][j]

    def __str__(self):
        out = ""
        for i in range(len(self.v)):
            out += '\n'
            out += str(self.v[i][0])
            for j in range(1, len(self.v[i])):
                out += '\t' + str(self.v[i][j])
        return out[1:]

    def size(self):
        return (len(self.v), len(self.v[0]))

    def __add__(self, other):
        if (self.size() == other.size()):
            result = [0] * len(self.v)
            for i in range(len(self.v)):
                result[i] = [0] * len(self.v[i])
                for j in range(len(self.v[i])):
                    result[i][j] = self.v[i][j] + other.v[i][j]
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        result = [0] * len(self.v)
        for i in range(len(self.v)):
            result[i] = [0] * len(self.v[i])
            for j in range(len(self.v[i])):
                result[i][j] = self.v[i][j] * other
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        result = [0] * len(self.v[0])
        for i in range(len(self.v[0])):
            result[i] = [0] * len(self.v)
            for j in range(len(self.v)):
                result[i][j] = self.v[j][i]
        self.v = [0] * len(result)
        for i in range(len(result)):
            self.v[i] = [0] * len(result[i])
            for j in range(len(result[i])):
                self.v[i][j] = result[i][j]
        return self

    def transposed(mat):
        result = [0] * len(mat.v[0])
        for i in range(len(mat.v[0])):
            result[i] = [0] * len(mat.v)
            for j in range(len(mat.v)):
                result[i][j] = mat.v[j][i]
        return Matrix(result)

exec(stdin.read())

#D
from sys import stdin

class MatrixError(BaseException):
    def __init__(self, first, second):
        self.matrix1 = first
        self.matrix2 = second

class Matrix:
    def __init__(self, values):
        self.v = [0] * len(values)
        for i in range(len(values)):
            self.v[i] = [0] * len(values[i])
            for j in range(len(values[i])):
                self.v[i][j] = values[i][j]

    def __str__(self):
        out = ""
        for i in range(len(self.v)):
            out += '\n'
            out += str(self.v[i][0])
            for j in range(1, len(self.v[i])):
                out += '\t' + str(self.v[i][j])
        return out[1:]

    def size(self):
        return (len(self.v), len(self.v[0]))

    def __add__(self, other):
        if (self.size() == other.size()):
            result = [0] * len(self.v)
            for i in range(len(self.v)):
                result[i] = [0] * len(self.v[i])
                for j in range(len(self.v[i])):
                    result[i][j] = self.v[i][j] + other.v[i][j]
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [0] * len(self.v)
            for i in range(len(self.v)):
                result[i] = [0] * len(self.v[i])
                for j in range(len(self.v[i])):
                    result[i][j] = self.v[i][j] * other
        elif isinstance(other, Matrix) and (len(self.v[0]) == len(other.v)):
            result = [0] * len(self.v)
            for i in range(len(self.v)):
                result[i] = [0] * len(other.v[0])
                for j in range(len(other.v[0])):
                    for k in range(len(other.v)):
                        result[i][j] += (self.v[i][k] * other.v[k][j])
        else:
            raise MatrixError(self, other)
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        result = [0] * len(self.v[0])
        for i in range(len(self.v[0])):
            result[i] = [0] * len(self.v)
            for j in range(len(self.v)):
                result[i][j] = self.v[j][i]
        self.v = [0] * len(result)
        for i in range(len(result)):
            self.v[i] = [0] * len(result[i])
            for j in range(len(result[i])):
                self.v[i][j] = result[i][j]
        return self

    def transposed(mat):
        result = [0] * len(mat.v[0])
        for i in range(len(mat.v[0])):
            result[i] = [0] * len(mat.v)
            for j in range(len(mat.v)):
                result[i][j] = mat.v[j][i]
        return Matrix(result)

exec(stdin.read())

#E
from sys import stdin, float_info
eps = float_info.epsilon

class MatrixError(BaseException):
    def __init__(self, first, second):
        self.matrix1 = first
        self.matrix2 = second

class Matrix:
    def __init__(self, values):
        self.v = [0] * len(values)
        for i in range(len(values)):
            self.v[i] = [0] * len(values[i])
            for j in range(len(values[i])):
                self.v[i][j] = values[i][j]

    def __str__(self):
        out = ""
        for i in range(len(self.v)):
            out += '\n'
            out += str(self.v[i][0])
            for j in range(1, len(self.v[i])):
                out += '\t' + str(self.v[i][j])
        return out[1:]

    def size(self):
        return (len(self.v), len(self.v[0]))

    def __add__(self, other):
        if (self.size() == other.size()):
            result = [0] * len(self.v)
            for i in range(len(self.v)):
                result[i] = [0] * len(self.v[i])
                for j in range(len(self.v[i])):
                    result[i][j] = self.v[i][j] + other.v[i][j]
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [0] * len(self.v)
            for i in range(len(self.v)):
                result[i] = [0] * len(self.v[i])
                for j in range(len(self.v[i])):
                    result[i][j] = self.v[i][j] * other
        elif isinstance(other, Matrix) and (len(self.v[0]) == len(other.v)):
            result = [0] * len(self.v)
            for i in range(len(self.v)):
                result[i] = [0] * len(other.v[0])
                for j in range(len(other.v[0])):
                    for k in range(len(other.v)):
                        result[i][j] += (self.v[i][k] * other.v[k][j])
        else:
            raise MatrixError(self, other)
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        result = [0] * len(self.v[0])
        for i in range(len(self.v[0])):
            result[i] = [0] * len(self.v)
            for j in range(len(self.v)):
                result[i][j] = self.v[j][i]
        self.v = [0] * len(result)
        for i in range(len(result)):
            self.v[i] = [0] * len(result[i])
            for j in range(len(result[i])):
                self.v[i][j] = result[i][j]
        return self

    def transposed(mat):
        result = [0] * len(mat.v[0])
        for i in range(len(mat.v[0])):
            result[i] = [0] * len(mat.v)
            for j in range(len(mat.v)):
                result[i][j] = mat.v[j][i]
        return Matrix(result)

    def solve(self, x):
        if (len(self.v) != len(self.v[0])) or (len(self.v[0]) != len(x)):
            raise Exception
        copy, n = Matrix(self.v), len(self.v)
        vec = []
        for i in range(n):
            vec.append(x[i])
        for k in range(n):
            maxi, index = abs(copy.v[k][k]), k
            for i in range(k + 1, n):
                if (abs(copy.v[i][k]) > maxi):
                    maxi, index = abs(copy.v[i][k]), i
            if (maxi < eps):
                raise Exception
            if (index != k):
                for j in range(k, n):
                    copy.v[k][j], copy.v[index][j] = copy.v[index][j], copy.v[k][j]
                vec[k], vec[index] = vec[index], vec[k]
            k1 = copy.v[k][k]
            for i in range(k + 1, n):
                if (copy.v[i][k] > eps):
                    k2 = copy.v[i][k]
                    copy.v[i][k] = 0
                    for j in range(k + 1, n):
                        copy.v[i][j] = k1*copy.v[i][j] - k2*copy.v[k][j]
                    vec[i] = k1*vec[i] - k2*vec[k]
        for k in range(n - 1, -1, -1):
            for j in range(k + 1, n):
                vec[k] -= vec[j]*copy.v[k][j]
            vec[k] /= copy.v[k][k]
        return vec

exec(stdin.read())

#F
from sys import stdin, float_info
eps = float_info.epsilon

class MatrixError(BaseException):
    def __init__(self, first, second):
        self.matrix1 = first
        self.matrix2 = second

class Matrix:
    def __init__(self, values):
        self.v = [0] * len(values)
        for i in range(len(values)):
            self.v[i] = [0] * len(values[i])
            for j in range(len(values[i])):
                self.v[i][j] = values[i][j]

    def __str__(self):
        out = ""
        for i in range(len(self.v)):
            out += '\n'
            out += str(self.v[i][0])
            for j in range(1, len(self.v[i])):
                out += '\t' + str(self.v[i][j])
        return out[1:]

    def size(self):
        return (len(self.v), len(self.v[0]))

    def __add__(self, other):
        if (self.size() == other.size()):
            result = [0] * len(self.v)
            for i in range(len(self.v)):
                result[i] = [0] * len(self.v[i])
                for j in range(len(self.v[i])):
                    result[i][j] = self.v[i][j] + other.v[i][j]
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [0] * len(self.v)
            for i in range(len(self.v)):
                result[i] = [0] * len(self.v[i])
                for j in range(len(self.v[i])):
                    result[i][j] = self.v[i][j] * other
        elif isinstance(other, Matrix) and (len(self.v[0]) == len(other.v)):
            result = [0] * len(self.v)
            for i in range(len(self.v)):
                result[i] = [0] * len(other.v[0])
                for j in range(len(other.v[0])):
                    for k in range(len(other.v)):
                        result[i][j] += (self.v[i][k] * other.v[k][j])
        else:
            raise MatrixError(self, other)
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        result = [0] * len(self.v[0])
        for i in range(len(self.v[0])):
            result[i] = [0] * len(self.v)
            for j in range(len(self.v)):
                result[i][j] = self.v[j][i]
        self.v = [0] * len(result)
        for i in range(len(result)):
            self.v[i] = [0] * len(result[i])
            for j in range(len(result[i])):
                self.v[i][j] = result[i][j]
        return self

    def transposed(mat):
        result = [0] * len(mat.v[0])
        for i in range(len(mat.v[0])):
            result[i] = [0] * len(mat.v)
            for j in range(len(mat.v)):
                result[i][j] = mat.v[j][i]
        return Matrix(result)

    def solve(self, x):
        if (len(self.v) != len(self.v[0])) or (len(self.v[0]) != len(x)):
            raise Exception
        copy, n = Matrix(self.v), len(self.v)
        vec = []
        for i in range(n):
            vec.append(x[i])
        for k in range(n):
            maxi, index = abs(copy.v[k][k]), k
            for i in range(k + 1, n):
                if (abs(copy.v[i][k]) > maxi):
                    maxi, index = abs(copy.v[i][k]), i
            if (maxi < eps):
                raise Exception
            if (index != k):
                for j in range(k, n):
                    copy.v[k][j], copy.v[index][j] = copy.v[index][j], copy.v[k][j]
                vec[k], vec[index] = vec[index], vec[k]
            k1 = copy.v[k][k]
            for i in range(k + 1, n):
                if (copy.v[i][k] > eps):
                    k2 = copy.v[i][k]
                    copy.v[i][k] = 0
                    for j in range(k + 1, n):
                        copy.v[i][j] = k1*copy.v[i][j] - k2*copy.v[k][j]
                    vec[i] = k1*vec[i] - k2*vec[k]
        for k in range(n - 1, -1, -1):
            for j in range(k + 1, n):
                vec[k] -= vec[j]*copy.v[k][j]
            vec[k] /= copy.v[k][k]
        return vec

class SquareMatrix(Matrix):
    def __pow__(self, p):
        if p == 0:
            return SquareMatrix([[1 if i==j else 0 for j in range(len(self.v))] for i in range(len(self.v))])
        if p == 1:
            return self
        if p % 2 == 0:
            tmp = self.__pow__(p // 2)
            return tmp * tmp
        return self * self.__pow__(p - 1)

exec(stdin.read())
