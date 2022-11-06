#A
inp_list = input().split()
for i in range(0, len(inp_list), 2):
    print(inp_list[i])

#B
inp_list = input().split()
for i in range(len(inp_list)):
    if (int(inp_list[i]) % 2 == 0):
        print(inp_list[i], end=' ')

#C
inp_list = list(map(int, input().split()))
ans = 0
for i in range(len(inp_list)):
    if (inp_list[i] > 0):
        ans += 1
print(ans)

#D
inp_list = list(map(int, input().split()))
for i in range(1, len(inp_list)):
    if (inp_list[i-1] < inp_list[i]):
        print(inp_list[i], end=' ')

#E
inp_list = list(map(int, input().split()))
for i in range(1, len(inp_list)):
    if (inp_list[i-1] >= 0) and (inp_list[i] >= 0):
        print(inp_list[i-1], inp_list[i])
        break
    elif (inp_list[i-1] < 0) and (inp_list[i] < 0):
        print(inp_list[i-1], inp_list[i])
        break

#F
inp_list = list(map(int, input().split()))
ans = 0
for i in range(1, len(inp_list)-1):
    if (inp_list[i-1] < inp_list[i]) and (inp_list[i] > inp_list[i+1]):
        ans += 1
        i += 1
print(ans)

#G
inp_list = list(map(int, input().split()))
pos = 0
cur_max = inp_list[0]
for i in range(1, len(inp_list)):
    if (inp_list[i] > cur_max):
        cur_max = inp_list[i]
        pos = i
print(cur_max, pos)

#H
inp_list = list(map(int, input().split()))
mini = 1001
for i in range(len(inp_list)):
    if (inp_list[i] > 0) and (inp_list[i] < mini):
        mini = inp_list[i]
print(mini)

#I
inp_list = list(map(int, input().split()))
mini = 10**10
for i in range(len(inp_list)):
    if (inp_list[i] % 2 != 0) and (inp_list[i] < mini):
        mini = inp_list[i]
print(mini)

#J
inp_list = list(map(int, input().split()))
x = int(input())
i = 0
while (i < len(inp_list)) and (x <= inp_list[i]):
    i += 1
print(i+1)

#K
inp_list = list(map(int, input().split()))
ans = 1
for i in range(1, len(inp_list)):
    if (inp_list[i] != inp_list[i-1]):
        ans += 1
print(ans)

#L
inp_list = list(map(int, input().split()))
print(*inp_list[::-1])

#M
inp_list = list(map(int, input().split()))
n = len(inp_list)
for i in range(n // 2):
    inp_list[i], inp_list[n - i - 1] = inp_list[n - i - 1], inp_list[i]
print(*inp_list)

#N
inp_list = list(map(int, input().split()))
for i in range(1, len(inp_list), 2):
    inp_list[i], inp_list[i - 1] = inp_list[i - 1], inp_list[i]
print(*inp_list)

#O
inp_list = list(map(int, input().split()))
last = inp_list[len(inp_list) - 1]
for i in range(len(inp_list)-1, 0, -1):
    inp_list[i] = inp_list[i-1]
inp_list[0] = last
print(*inp_list)

#P
inp_list = list(map(int, input().split()))
pos_min = 0
pos_max = 0
for i in range(1, len(inp_list)):
    if (inp_list[i] < inp_list[pos_min]):
        pos_min = i
    if (inp_list[pos_max] < inp_list[i]):
        pos_max = i
inp_list[pos_min], inp_list[pos_max] = inp_list[pos_max], inp_list[pos_min]
print(*inp_list)

#Q
inp_list = list(map(int, input().split()))
k = int(input())
for i in range(k, len(inp_list)-1):
    inp_list[i] = inp_list[i+1]
inp_list.pop()
print(*inp_list)

#R
inp_list = list(map(int, input().split()))
inp_list.append(0)
k, c = list(map(int, input().split()))
for i in range(len(inp_list)-1, k, -1):
    inp_list[i] = inp_list[i-1]
inp_list[k] = c
print(*inp_list)

#S
inp_list = list(map(int, input().split()))
ans = 0
for i in range(len(inp_list)):
    for j in range(i+1, len(inp_list)):
        if (inp_list[i] == inp_list[j]):
            ans += 1
print(ans)

#T
inp_list = list(map(int, input().split()))
for num in inp_list:
    if (inp_list.count(num) == 1):
        print(num, end=' ')

#U
def ReplaceInList(start, end, some_list, symbol):
    for idx in range(start, end):
        some_list[idx] = symbol

n, k = list(map(int, input().split()))
ans = list('I'*n)
for i in range(k):
    l, r = list(map(int, input().split()))
    ReplaceInList(l-1, r, ans, '.')
print(''.join(ans))

#V
x = []
y = []
flag = False
for i in range(8):
    x_i, y_i = list(map(int, input().split()))
    x.append(x_i)
    y.append(y_i)
for i in range(8):
    for j in range(i+1, 8):
        if (x[i] == x[j]) or (y[i] == y[j]):
            flag = True
            break
        elif (abs(x[i] - x[j]) == abs(y[i] - y[j])):
            flag = True
            break
    if flag:
        print('YES')
        break
if not flag:
    print('NO')

#W
inp_list = list(map(int, input().split()))
i = 0
while (i < len(inp_list)) and (inp_list[i] != 0):
    i += 1
pos = i
for idx in range(i+1, len(inp_list)):
    if (inp_list[idx] != 0):
        inp_list[pos], inp_list[idx] = inp_list[idx], inp_list[pos]
        pos += 1
print(*inp_list)

#X
inp_list = list(map(int, input().split()))
num_max = inp_list[0]
cur_max = inp_list.count(num_max)
for i in range(1, len(inp_list)):
    if (inp_list.count(inp_list[i]) > cur_max):
        num_max = inp_list[i]
        cur_max = inp_list.count(num_max)
print(num_max)
