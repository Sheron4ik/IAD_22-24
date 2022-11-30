#A
print(len(set(map(int, input().split()))))

#B
print(len(set(map(int, input().split())) & set(map(int, input().split()))))

#C
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
fout.write(' '.join(map(str, sorted(set(map(int, fin.readline().split())) & set(map(int, fin.readline().split()))))))
fin.close()
fout.close()

#D
inp = list(map(int, input().split()))
ansSet = set()
for num in inp:
    if (num in ansSet):
        print('YES')
    else:
        print('NO')
        ansSet.add(num)

#E
anya, borya = map(int, input().split())
SetAnya = set()
SetBorya = set()
SetIntersection = set()
for i in range(anya):
    SetAnya.add(int(input()))
for i in range(borya):
    num = int(input())
    if num in SetAnya:
        SetIntersection.add(num)
    else:
        SetBorya.add(num)
print(len(SetIntersection))
print(*sorted(SetIntersection))
print(len(SetAnya - SetIntersection))
print(*sorted(SetAnya - SetIntersection))
print(len(SetBorya))
print(*sorted(SetBorya))

#F
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
ans = set()
for line in fin:
    lists = line.split()
    for word in lists:
        ans.add(word)
fout.write(str(len(ans)))
fin.close()
fout.close()

#G
n = int(input())
ansSet = set(range(1, n + 1))
inp = input()
while(inp != 'HELP'):
    luck = set(map(int, inp.split()))
    ans = input()
    if (ans == 'YES'):
        ansSet &= luck
    else:
        ansSet -= luck
    inp = input()
print(*sorted(ansSet))

#H
n = int(input())
ansSet = set(range(1, n + 1))
inp = input()
while(inp != 'HELP'):
    luck = set(map(int, inp.split()))
    prob = luck & ansSet
    if (len(prob) <= len(ansSet) // 2):
        print('NO')
        ansSet -= luck
    else:
        print('YES')
        ansSet = prob
    inp = input()
print(*sorted(ansSet))

#I
all_lang = set()
Eq_lang = set()
n = int(input())
for i in range(n):
    count_lang = int(input())
    tmp = set()
    for j in range(count_lang):
        lang = input()
        all_lang.add(lang)
        tmp.add(lang)
    if i == 0:
        Eq_lang = tmp
    else:
        Eq_lang &= tmp

print(len(Eq_lang))
for cur_lang in Eq_lang:
    print(cur_lang)
print(len(all_lang))
for cur_lang in all_lang:
    print(cur_lang)

#J
bus1_s, bus1_e, bus2_s, bus2_e = map(int, input().split())
print(len(set(range(min(bus1_s, bus1_e), max(bus1_s, bus1_e) + 1)) & set(range(min(bus2_s, bus2_e), max(bus2_s, bus2_e) + 1))))

#K
n, k = map(int, input().split())
days = set()
for i in range(k):
    a, b = map(int, input().split())
    days |= set([day for day in range(a, n+1, b) if day % 7 not in (0, 6)])
print(len(days))

#L
def CorrectFormat(number):
    number = number.replace('(', '')
    number = number.replace(')', '')
    number = number.replace('-', '')
    number = number.replace('+', '')
    if (len(number) != 7):
        return number[1:]
    return '495' + number

added = CorrectFormat(input())
for i in range(3):
    tel = CorrectFormat(input())
    if (tel == added):
        print('YES')
    else:
        print('NO')
