#A
countries = dict()
n = int(input())
for i in range(n):
    line = input().split()
    country, cities = line[0], line[1:]
    for city in cities:
        countries[city] = country
m = int(input())
for i in range(m):
    print(countries[input()])

#B
fin = open("input.txt")
fout = open("output.txt", 'w')
words = {}
for line in fin:
    line = line.split()
    for word in line:
        print(words.get(word, 0), end=' ')
        words[word] = words.get(word, 0) + 1
fin.close()
fout.close()

#C
n = int(input())
synonyms = {}
for i in range(n):
    word1, word2 = input().split()
    synonyms[word1] = word2
    synonyms[word2] = word1
print(synonyms[input()])

#D
fin = open("input.txt")
fout = open("output.txt", 'w')
candidates = dict()
for line in fin:
    line = line.split()
    candidates[line[0]] = candidates.get(line[0], 0) + int(line[1])
for candidate in sorted(candidates):
    fout.write(candidate + ' ' + str(candidates[candidate]) + '\n')
fin.close()
fout.close()

#E
fin = open("input.txt")
fout = open("output.txt", 'w')
words = dict()
for line in fin:
    line = line.split()
    for word in line:
        words[word] = words.get(word, 0) + 1
count = 0
ans_word = ''
for word in sorted(words):
    if (words[word] > count):
        ans_word = word
        count = words[word]
fout.write(ans_word)
fin.close()
fout.close()

#F
fin = open("input.txt")
fout = open("output.txt", 'w')
words = dict()
for line in fin:
    line = line.split()
    for word in line:
        words[word] = words.get(word, 0) + 1
frequency = []
for word in sorted(words):
    frequency.append((word, words[word]))
frequency.sort(key=lambda elem: elem[1], reverse=True)
for i in range(len(frequency)):
    fout.write(frequency[i][0] + '\n')
    print(frequency[i][0])
fin.close()
fout.close()

#G
fin = open("input.txt", "r")
fout = open("output.txt", "w")
candidates = dict()
countVoices = 0
for line in fin:
    candidates[line] = candidates.get(line, 0) + 1
    countVoices += 1
max1 = max2 = ''
k_m1 = k_m2 = 0
for candidate in candidates:
    if (candidates[candidate] > k_m1):
        k_m2 = k_m1
        max2 = max1
        max1 = candidate
        k_m1 = candidates[candidate]
    elif (candidates[candidate] > k_m2):
        max2 = candidate
        k_m2 = candidates[candidate]
if (k_m1 / countVoices) > 0.5:
    fout.write(max1)
else:
    fout.write(max1+max2)
fin.close()
fout.close()

#H
fin = open("input.txt", "r")
fout = open("output.txt", "w")
purchasers = {}
for line in fin:
    name, product, count = line.split()
    if name not in purchasers:
        purchasers[name] = {}
        purchasers[name][product] = int(count)
    else:
        purchasers[name][product] = purchasers[name].get(product, 0) + int(count)
for name in sorted(purchasers):
    print(name, ':', sep='', file=fout)
    for product in sorted(purchasers[name]):
        print(product, purchasers[name][product], file=fout)
fin.close()
fout.close()

#I
fin = open("input.txt", "r")
fout = open("output.txt", "w")
clients = dict()
for line in fin:
    op = line.split()
    if (op[0] == 'DEPOSIT'):
        clients[op[1]] = clients.get(op[1], 0) + int(op[2])
    elif (op[0] == 'WITHDRAW'):
        clients[op[1]] = clients.get(op[1], 0) - int(op[2])
    elif (op[0] == 'BALANCE'):
        if (op[1] in clients):
            print(clients[op[1]], file=fout)
        else:
            print('ERROR', file=fout)
    elif (op[0] == 'TRANSFER'):
        clients[op[1]] = clients.get(op[1], 0) - int(op[3])
        clients[op[2]] = clients.get(op[2], 0) + int(op[3])
    elif (op[0] == 'INCOME'):
        for client in clients:
            if (clients[client] > 0):
                clients[client] = clients[client] * (100 + int(op[1])) // 100
fin.close()
fout.close()

#J
def posLast(string):
    for i in range(len(string) - 2, -1, -1):
        if (string[i] == ' '):
            return i + 1
    return 0

fin = open("input.txt", "r")
fout = open("output.txt", "w")
parties = dict()
voice = 0
for line in fin:
    pos = posLast(line)
    parties[line[:pos-1]] = int(line[pos:len(line)-1])
    voice += int(line[pos:len(line)-1])
fich = voice / 450
v_parties = []
voice = 0
for party in parties:
    v_parties.append((parties[party] % fich, int(parties[party] // fich), party))
    parties[party] = int(parties[party] // fich)
    voice += parties[party]
v_parties.sort(reverse=True)
curAddPos = 0
while (voice != 450):
    parties[v_parties[curAddPos][2]] += 1
    curAddPos += 1
    curAddPos %= len(parties)
    voice += 1
for party in parties:
    print(party, parties[party], file=fout)
fin.close()
fout.close()

#K
def isOneBigChar(word):
    bigChar = 0
    for i in range(len(word)):
        if ('A' <= word[i] <= 'Z'):
            bigChar += 1
    if (bigChar == 1):
        return True
    return False

n = int(input())
words = dict()
for i in range(n):
    word = input()
    if (word.lower() not in words):
        words[word.lower()] = set()
    words[word.lower()].add(word)
petr = input().split()
mistakes = 0
for word in petr:
    if (word.lower() in words):
        if (word not in words[word.lower()]):
            mistakes += 1
    else:
        if not(isOneBigChar(word)):
            mistakes += 1
print(mistakes)

#L
def TripForTree(tree, key, rod, h=1):
    if (key not in tree):
        return
    for child in tree[key]:
        TripForTree(tree, child, rod, h=h+1)
        rod.append((child, h))

n = int(input())
childrens = set()
parents = set()
tree = {}
for i in range(n-1):
    line = input().split()
    childrens.add(line[0])
    parents.add(line[1])
    if (line[1] not in tree):
        tree[line[1]] = set()
    tree[line[1]].add(line[0])
father = list(parents - childrens)
ans_rod = []
ans_rod.append((father[0], 0))
TripForTree(tree, father[0], ans_rod)
ans_rod.sort()
for relative in ans_rod:
    print(relative[0], relative[1])
