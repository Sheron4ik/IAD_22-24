#A
def min4(a, b, c, d):
    return min(min(a, b), min(c, d))

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))

#B
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))

#C
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def perimeter(x1, y1, x2, y2, x3, y3):
    return distance(x1, y1, x2, y2) + distance(x1, y1, x3, y3) + distance(x2, y2, x3, y3)

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
print(perimeter(x1, y1, x2, y2, x3, y3))

#D
def xor(x, y):
    return (x + y) % 2

x = int(input())
y = int(input())
print(xor(x, y))

#E
def IsPointInSquare(x, y):
    return (-1 <= x <= 1) and (-1 <= y <= 1)

x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')

#F
def IsPointInSquare(x, y):
    return (-1 <= (abs(x)+abs(y)) <= 1)

x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')

#G
def IsPointInCircle(x, y, xc, yc, r):
    return (((x - xc)**2 + (y - yc)**2)**0.5) <= r

x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')

#H
def IsPointInArea(x, y):
    return (((y >= -x) and (y >= 2*x + 2) and ((x+1)*(x+1) + (y-1)*(y-1) <= 4)) or ((y <= -x) and (y <= 2*x + 2) and (((x+1)*(x+1) + (y-1)*(y-1) >= 4))))

x = float(input())
y = float(input())
if IsPointInArea(x, y):
    print('YES')
else:
    print('NO')

#I
def MinDivisor(n):
    for i in range(2, int(n**0.5) + 1):
        if (n % i == 0):
            return i
    return n

n = int(input())
print(MinDivisor(n))

#J
def IsPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if (n % i == 0):
            return False
    return True

n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')

#K
def power(a, n):
    if (n == 0):
        return 1
    return a * power(a, n - 1)

a = float(input())
n = int(input())
print(power(a, n))

#L
def power(a, n):
    ans = 1
    for i in range(1, abs(n)+1):
        ans *= a
    if (n < 0):
        return 1/ans
    return ans

a = float(input())
n = int(input())
print(power(a, n))

#M
def summ(a, b):
    if (b == 0):
        return a
    return 1 + summ(a, b - 1)

a = int(input())
b = int(input())
print(summ(a, b))

#N
def power(a, n):
    if (n == 0):
        return 1
    if (n % 2 == 1):
        return a * power(a, n - 1)
    return power(a*a, n // 2)

a = float(input())
n = int(input())
if (n < 0):
    print(1/power(a, abs(n)))
else:
    print(power(a, abs(n)))

#O
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

a = int(input())
b = int(input())
print(gcd(a, b))

#P
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

def ReduceFraction(n, m):
    com = gcd(n, m)
    return n // com, m // com

n = int(input())
m = int(input())
p, q = ReduceFraction(n, m)
print(p, q)

#Q
def phib(n):
    if (n == 0) or (n == 1):
        return n
    return phib(n-2) + phib(n-1)

n = int(input())
print(phib(n))

#R
def C(n, k):
    if (n == k) or (k == 0):
        return 1
    return C(n-1, k-1) + C(n-1, k)

n = int(input())
k = int(input())
print(C(n, k))

#S
def summ(a):
    if (a == 0):
        return a
    return a + summ(int(input()))

a = int(input())
print(summ(a))

#T
def reverse(a):
    if (a == 0):
        print(a)
        return
    reverse(int(input()))
    print(a) 

a = int(input())
reverse(a)

#U
def move(n, x, y):
    if (n == 1):
        print(n, x, y)
        return
    move(n-1, x, 6-x-y)
    print(n, x, y)
    move(n-1, 6-x-y, y)

n = int(input())
move(n, 1, 3)

#V
ans = []
def sum2_block(n, block):
    if (n != 0):
        num = int(n**0.5)
        if (num >= block) and (block > 1):
            num = block - 1
        ans.append(num)
        sum2_block(n - num**2, block)

n = int(input())
sqr2 = int(n**0.5)
for block in range(sqr2, 0, -1):
    sum2_block(n, block)
    if (len(ans) <= 4):
        print(*ans)
        break
    else:
        ans.clear()

#W
ans = []
def sum3_block(n, block):
    if (n != 0):
        num = int(n**(1/3))
        if (num >= block) and (block > 1):
            num = block - 1
        ans.append(num**3)
        sum3_block(n - num**3, block)

n = int(input())
sqr3 = int(n**(1/3))
flag = False
for block in range(sqr3, 0, -1):
    sum3_block(n, block)
    if (0 <= len(ans) <= 7):
        flag = True
        if (len(ans) == 0):
            print(0)
        else:
            print(*ans)
        break
    else:
        ans.clear()
if not(flag):
    print(0)

#X
flag = True
def only2(a):
    if (a != 0):
        only2(int(input()))
        if (((int(a**0.5))**2) == a):
            print(a, end=' ')
            global flag
            flag = False

a = int(input())
only2(a)
if (flag):
    print('0')
