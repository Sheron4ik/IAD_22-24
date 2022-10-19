#A
n = int(input())
i = 1
while (i*i <= n):
    print(i*i)
    i += 1
    
#B
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i*i
print(ans)

#C
n = int(input())
for i in range(2, n+1):
    if (n % i == 0):
        print(i)
        break
    
#D
n = int(input())
st = 1
while (st <= n):
    print(st, end=' ')
    st *= 2
    
#E
n = int(input())
st = 1
while (st <= n):
    if (st == n):
        print('YES')
        break
    st *= 2
if (st > n):
    print('NO')
    
#F
n = int(input())
st = 1
num_st = 0
while (st < n):
    st *= 2
    num_st += 1
print(num_st)

#G
x = int(input())
y = int(input())
day = 1
cur = x
while (cur < y):
    cur *= 1.1
    day += 1
print(day)

#H
kol = 0
i = int(input())
while (i != 0):
    kol += 1
    i = int(input())
print(kol)

#I
ans = 0
i = int(input())
while (i != 0):
    ans += i
    i = int(input())
print(ans)

#J
ans = 0
kol = 0
i = int(input())
while (i != 0):
    ans += i
    kol += 1
    i = int(input())
print(ans / kol)

#K
kol = 0
i = int(input())
while (i != 0):
    if (i % 2 == 0):
        kol += 1
    i = int(input())
print(kol)

#L
maxi = -1
i = int(input())
while (i != 0):
    if (i >= maxi):
        maxi = i
    i = int(input())
print(maxi)

#M
kol = 0
i = int(input())
pred = i
while (i != 0):
    if (i > pred):
        kol += 1
    pred = i
    i = int(input())
print(kol)

#N
maxi = -1
i = int(input())
pred = -1
while (i != 0):
    if (i >= maxi):
        pred = maxi
        maxi = i
    elif (i > pred):
        pred = i
    i = int(input())
print(pred)

#O
maxi = -1
kol = 0
i = int(input())
while (i != 0):
    if (i > maxi):
        maxi = i
        kol = 1
    elif (i == maxi):
        kol += 1
    i = int(input())
print(kol)

#P
n = int(input())
f_ppast = 0
f_past = 1
f_now = f_ppast + f_past
for i in range(2, n):
    f_ppast = f_past
    f_past = f_now
    f_now = f_ppast + f_past
print(f_now)

#Q
a = int(input())
f_ppast = 0
f_past = 1
f_now = f_ppast + f_past
n = 2
while (a > f_now):
    f_ppast = f_past
    f_past = f_now
    f_now = f_ppast + f_past
    n += 1
if (a == f_now):
    print(n)
else:
    print(-1)
    
#R
a = int(input())
b = int(input())
while (a != b):
    if (a % 2 == 0) and (a - b >= b):
        a //= 2
        print(':2')
    else:
        a -= 1
        print('-1')
        
#S
a = int(input())
while (a // 10 != 0):
    print(a % 10, end='')
    a //= 10
print(a % 10)

#T
k = int(input())
ans = 0
while (k != 0):
    a = k
    pal = 0
    while (a // 10 != 0):
        pal = pal*10 + a%10
        a //= 10
    pal = pal*10 + a%10
    if (k == pal):
        ans += 1
    k -= 1
print(ans)

#U
i = int(input())
pred = 0
cur = 1
maxi = 1
while (i != 0):
    if (i == pred):
        cur += 1
    else:
        cur = 1
    if (cur > maxi):
        maxi = cur
    pred = i
    i = int(input())
print(maxi)

#V
pred = int(input())
up = 1
down = 1
maxi = 1
i = int(input())
while (i != 0):
    if (i > pred):
        up += 1
        down = 1
    elif (i < pred):
        down += 1
        up = 1
    else:
        up = 1
        down = 1;
    if (up > maxi):
        maxi = up
    if (down > maxi):
        maxi = down
    pred = i
    i = int(input())
print(maxi)

#W
pred = int(input())
m = int(input())
i = int(input())
p = 1
p1 = 0
p2 = 0
mini = 10**9
while (i != 0):
    if (pred < m) and (m > i):
        if (p2 == 0):
            p2 = p
        else:
            p2 = p1
        p1 = p
    if ((p1 - p2) < mini) and ((p1 - p2) != 0):
        mini = p1 - p2
    pred = m
    m = i
    p += 1
    i = int(input())
if (mini == 10**9):
    print(0)
else:
    print(mini)
    
#X
i = int(input())
n = 0
x = 0
xK = 0
while (i != 0):
    x += i
    xK += i*i
    n += 1
    i = int(input())
s = x / n
ans = xK + n*s*s - 2*s*x
print((ans / (n - 1)) ** 0.5)
