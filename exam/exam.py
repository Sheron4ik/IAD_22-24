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
