'''
n = input()
s2_old = n[::2]
suma = 0
for let in s2_old:
    t = int(let)*2
    if (t > 9):
        t -= 9
    suma += t
for i in range(1, 6, 2):
    suma += int(n[i])
if (suma % 10 == 0):
    print('YES')
else:
    print('NO')
'''

'''
m1, m2 = map(int, input().split())
n1, n2 = map(int, input().split())

for i in range(m1, m2+1):
    for j in range(n1, n2+1):
        print(i, 'x', j, '=', i*j)
    print()
'''


'''
def travel(tree, key, rod):
    if (key not in tree):
        rod[key] = 0
        return
    kolvo = 0
    for child in tree[key]:
        kolvo += 1
        travel(tree, child, rod)
        kolvo += rod[child]
    rod[key] = kolvo

n = int(input())
childs = set()
parents = set()
tree = {}
for i in range(n-1):
    line = input().split()
    childs.add(line[0])
    parents.add(line[1])
    if (line[1] not in tree):
        tree[line[1]] = set()
    tree[line[1]].add(line[0])
fat = list(parents - childs)
ans = {}
travel(tree, fat[0], ans)
for chel in sorted(ans):
    print(chel, ans[chel])
'''

'''
fin = open("input.txt", 'r')
fout = open("output.txt", 'w')
line = fin.readline()
s = ""
for symb in line:
    if symb in ".,!?":
        s += ' '
    else:
        s += symb
words = s.split()
print(len(words) - words.count('-'), file=fout)
fin.close()
fout.close()
'''
'''
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
'''


'''
Generate 5 random tasks from one-name book
'''

import random

taskLim = {1:17, #tasks in each paragraph
           2:38,
           3:51,
           4:145,
           5:94,
           6:83,
           7:171,
           8:19,
           9:54,
           10:28,
           11:261,
           12:199,
           13:61,
           14:40}

def ChapTaskGen():
    chap = random.randint(1,14)
    task = '.' + str(random.randint(1,taskLim[chap]-1))
    return str(chap) + task
    
def TasksToDo(toDo):
    '''Print tasks to do'''
    pythonFile = ''
    print(toDo)
    for i in toDo:
        pythonFile += i
        if i==toDo[len(toDo)-1]:
            pythonFile += '.py'
        else:
            pythonFile += ' '
    with open('solved/' + pythonFile, 'w'):
        print(pythonFile)


def TaskAccomp():
    
    file = open('Container.txt', 'r+')
    finished = file.read()
    finished = finished.split(' ')
    #print(finished)
    
    toDo = []
    for i in range(5):
        task = ChapTaskGen()
        while True:
            if task not in finished and task not in toDo:
                break
            else:
                task = ChapTaskGen()
        toDo.append(task)
        WRITETOFILE = toDo[i] + ' '
        file.write(WRITETOFILE)
        
    TasksToDo(toDo)

TaskAccomp()












