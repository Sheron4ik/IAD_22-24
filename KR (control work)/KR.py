#A
a = int(input())
b = int(input())
c = int(input())
d = int(input())
res = (c*100 + d) - (a*100 + b)
print(res // 100, res % 100)

#B
inp_str = input()
left_pos, right_pos = inp_str.find('h'), inp_str.rfind('h')
res_str = inp_str[:left_pos + 1] + inp_str[left_pos + 1:right_pos][::-1] + inp_str[right_pos:]
print(res_str)

#C
n = int(input())
otr = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if (otr[i] + otr[j] > otr[k]) and (otr[i] + otr[k] > otr[j]) and (otr[k] + otr[j] > otr[i]):
                ans += 1
print(ans)

#D
fin = open("input.txt", "r", encoding="utf-8")
fout = open("output.txt", "w", encoding="utf-8")
members = []
for line in fin:
    line = line.split()
    members.append((int(line[2]), int(line[3])))
members.sort(reverse = True)
cur_class, cur_pos = 0, 1
b11 = members[0][1]
while (members[cur_pos][0] == members[cur_class][0]):
    cur_pos += 1
b10 = members[cur_pos][1]
cur_class = cur_pos
while (members[cur_pos][0] == members[cur_class][0]):
    cur_pos += 1
b9 = members[cur_pos][1]
print(b9, b10, b11, file=fout)
fin.close()
fout.close()

#E
# не успел ;с

#F
n, k = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for j in range(n):
    column = []
    for i in range(n):
        column.append(matrix[i][j])
    column.sort()
    column.sort(key=lambda el: abs(k - el))
    for i in range(n):
        matrix[i][j] = column[i]

for i in range(n):
    print(*matrix[i])
