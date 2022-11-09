#A
inp_list = list(map(int, input().split()))
flag = False
for i in range(1, len(inp_list)):
    if (inp_list[i-1] >= inp_list[i]):
        flag = True
        break
if (flag):
    print('NO')
else:
    print('YES')

#B
inp_list = list(map(int, input().split()))
cur_idx = 0
for i in range(1, len(inp_list)):
    if (inp_list[cur_idx] <= inp_list[i]):
        cur_idx = i
print(inp_list[cur_idx], cur_idx)

#C
len_list = int(input())
inp_list = list(map(int, input().split()))
x = int(input())
cur_ans = inp_list[0]
for i in range(1, len_list):
    if (abs(cur_ans - x) > abs(inp_list[i] - x)):
        cur_ans = inp_list[i]
print(cur_ans)

#D
inp_list = list(map(int, input().split()))
max1, max2 = max(inp_list[0], inp_list[1]), min(inp_list[0], inp_list[1])
min1, min2 = max2, max1
for i in range(2, len(inp_list)):
    if (inp_list[i] >= max1):
        max2, max1 = max1, inp_list[i]
    elif (inp_list[i] > max2):
        max2 = inp_list[i]

    if (inp_list[i] <= min1):
        min2, min1 = min1, inp_list[i]
    elif (inp_list[i] < min2):
        min2 = inp_list[i]
if (max1*max2 > min1*min2):
    print(max2, max1)
else:
    print(min1, min2)

#E
inp_list = list(map(int, input().split()))
max1, max3 = max(inp_list[0], inp_list[1], inp_list[2]), min(inp_list[0], inp_list[1], inp_list[2])
max2 = inp_list[0] + inp_list[1] + inp_list[2] - max1 - max3
min1, min2 = max3, max2
for i in range(3, len(inp_list)):
    if (inp_list[i] >= max1):
        max3, max2, max1 = max2, max1, inp_list[i]
    elif (inp_list[i] >= max2):
        max3, max2 = max2, inp_list[i]
    elif (inp_list[i] > max3):
        max3 = inp_list[i]

    if (inp_list[i] <= min1):
        min2, min1 = min1, inp_list[i]
    elif (inp_list[i] < min2):
        min2 = inp_list[i]

if (max1*max2*max3 > min1*min2*max1):
    print(max3, max2, max1)
else:
    print(min1, min2, max1)

#F
def CountSort(a):
    count_list = [0] * 101
    for num in a:
        count_list[num] += 1
    ptr = 0
    for i in range(101):
        while (count_list[i] != 0):
            a[ptr] = i
            ptr += 1
            count_list[i] -=1

a = list(map(int, input().split()))
CountSort(a)
print(*a)

#G
n = int(input())
klav = list(map(int, input().split()))
k = int(input())
tap = list(map(int, input().split()))
for i in range(k):
    klav[tap[i]-1] -= 1
for cur_klav in klav:
    if cur_klav < 0:
        print('YES')
    else:
        print('NO')

#H
n = int(input())
inp_list = list(map(int, input().split()))
inp_list.sort()
print(*inp_list)

#I
v, u = map(int, input().split())
v_u = []
for i in range(u):
    cur = int(input())
    v_u.append(cur)
v_u.sort()
ans = 0
for i in range(u):
    v -= v_u[i]
    if (v < 0):
        break
    ans += 1
print(ans)

#J
cur_size = int(input())
sizes = list(map(int, input().split()))
sizes.sort()
ans = 0
pred = -3
for i in range(len(sizes)):
    if (sizes[i] < cur_size):
        continue
    if (sizes[i] - pred > 2):
        ans += 1
        pred = sizes[i]
print(ans)

#K
n = int(input())
students = []
for i in range(n):
    name, score = input().split()
    students.append((name, int(score)))
students.sort(key=lambda student: student[1], reverse=True)
for i in range(n):
    print(students[i][0])

#L
s = list(map(int, input().split()))
t = list(map(int, input().split()))
s.sort()
t.sort(reverse=True)
suma = 0
for i in range(len(s)):
    suma += (s[i]*t[i])
print(suma)

#M
def merge(a, b):
    ptr1 = 0
    ptr2 = 0
    ans_list = []
    while (ptr1 < len(a)) and (ptr2 < len(b)):
        if (a[ptr1] < b[ptr2]):
            ans_list.append(a[ptr1])
            ptr1 += 1
        else:
            ans_list.append(b[ptr2])
            ptr2 += 1
    while (ptr1 < len(a)):
        ans_list.append(a[ptr1])
        ptr1 += 1
    while (ptr2 < len(b)):
        ans_list.append(b[ptr2])
        ptr2 += 1
    return ans_list

a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = merge(a, b)
print(*ans)

#N
def Intersection(a, b):
    ptr1 = 0
    ptr2 = 0
    ans_list = []
    while (ptr1 < len(a)) and (ptr2 < len(b)):
        while (ptr1 < len(a)) and (a[ptr1] < b[ptr2]):
            ptr1 += 1
        if (ptr1 == len(a)):
            break
        while (ptr2 < len(b)) and (a[ptr1] > b[ptr2]):
            ptr2 += 1
        if (ptr2 == len(b)):
            break
        if (a[ptr1] == b[ptr2]):
            ans_list.append(a[ptr1])
            ptr1 += 1
            ptr2 += 1
    return ans_list

a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = Intersection(a, b)
print(*ans)

#O
def binary_search(some_sortedList, start, end, target):
    left = start
    right = end
    while (left < right):
        middle = (left + right) // 2
        if (some_sortedList[middle][0] == target):
            return middle
        if (some_sortedList[middle][0] < target):
            left = middle + 1
        else:
            right = middle
    return right

count_city = int(input())
cities = list(map(int, input().split()))
count_school = int(input())
tmp = input().split()
schools = []
for i in range(count_school):
    schools.append((int(tmp[i]), i))
schools.sort()
for i in range(count_city):
    pos = binary_search(schools, 0, count_school-1, cities[i])
    if (abs(schools[pos][0] - cities[i]) > abs(schools[pos-1][0] - cities[i])):
        print(schools[pos-1][1] + 1)
    else:
        print(schools[pos][1] + 1)
