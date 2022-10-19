#A
a = int(input())
b = int(input())
print(((a // b * a) + (b // a * b)) // ((a // b) + (b // a)))

#B
a = int(input())
b = int(input())
if (a > b):
    print(1)
elif (a < b):
    print(2)
else:
    print(0)
    
#C
x = int(input())
if (x > 0):
    print(1)
elif (x < 0):
    print(-1)
else:
    print(0)

#D
a = int(input())
b = int(input())
c = int(input())
if (a >= b):
    if (a >= c):
        print(a)
    else:
        print(c)
else:
    if (b >= c):
        print(b)
    else:
        print(c)

#E
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 > 0) and (x2 > 0):
    if (y1 > 0) and (y2 > 0):
        print('YES')
    elif (y1 < 0) and (y2 < 0):
        print('YES')
    else:
        print('NO')
elif (x1 < 0) and (x2 < 0):
    if (y1 > 0) and (y2 > 0):
        print('YES')
    elif (y1 < 0) and (y2 < 0):
        print('YES')
    else:
        print('NO')
else:
    print('NO')

#F
a = int(input())
if (a % 4 == 0) and (a % 100 != 0):
    print('YES')
elif (a % 400 == 0):
    print('YES')
else:
    print('NO')

#G
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (-1 <= (x1 - x2) <= 1):
    if (-1 <= (y1 - y2) <= 1):
        print('YES')
    else:
        print('NO')
else:
    print('NO')

#H
a = int(input())
b = int(input())
c = int(input())
if (a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0):
    if (a % 2 != 0) or (b % 2 != 0) or (c % 2 != 0):
        print('YES')
    else:
        print('NO')
else:
    print('NO')

#I
a = int(input())
b = int(input())
if ((a - 1) % (b-a+1) == 0) and (b % (b-a+1) == 0):
    print('YES')
else:
    print('NO')

#J
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (((x1 + y1) % 2) == ((x2 + y2) % 2)):
    print('YES')
else:
    print('NO')
    
#K
n = int(input())
m = int(input())
k = int(input())
if (n * m >= k):
    if (k % m == 0) or (k % n == 0):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
    
#L
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
t = abs(x2 - x1)
if (y2 - y1 > 0) and ((y2 - y1) >= t):
    if ((y2 - y1) % 2) == (t % 2):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
    
#M
a = int(input())
b = int(input())
c = int(input())
if (a <= b):
    if (c <= a):
        a, b, c = c, a, b
    elif (c <= b):
        b, c = c, b
else:
    if (c <= b):
        a, c = c, a
    elif (c <= a):
        a, b, c = b, c, a
    else:
        a, b = b, a
print(a, b, c)

#N
a = int(input())
b = int(input())
c = int(input())
if (a == b == c):
    print(3)
elif (a == b) or (a == c) or (b == c):
    print(2)
else:
    print(0)
    
#O
a = int(input())
b = int(input())
c = int(input())
if (a > 0) and (b > 0) and (c > 0):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
            print('rectangular')
        elif (a*a + b*b < c*c) or (a*a + c*c < b*b) or (b*b + c*c < a*a):
            print('obtuse')
        else:
            print('acute')
    else:
        print('impossible')
else:
    print('impossible')

#P
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if ((a <= d) and (b <= e)) or ((b <= d) and (a <= e)):
    print('YES')
elif ((a <= d) and (c <= e)) or ((c <= d) and (a <= e)):
    print('YES')
elif ((b <= d) and (c <= e)) or ((c <= d) and (b <= e)):
    print('YES')
else:
    print('NO')
    
#Q
a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
    ###
if (a1 <= b1):
    if (c1 <= a1):
        a1, b1, c1 = c1, a1, b1
    elif (c1 <= b1):
        b1, c1 = c1, b1
else:
    if (c1 <= b1):
        a1, c1 = c1, a1
    elif (c1 <= a1):
        a1, b1, c1 = b1, c1, a1
    else:
        a1, b1 = b1, a1
    ###
if (a2 <= b2):
    if (c2 <= a2):
        a2, b2, c2 = c2, a2, b2
    elif (c2 <= b2):
        b2, c2 = c2, b2
else:
    if (c2 <= b2):
        a2, c2 = c2, a2
    elif (c2 <= a2):
        a2, b2, c2 = b2, c2, a2
    else:
        a2, b2 = b2, a2
    ###
if (a1 == a2) and (b1 == b2) and (c1 == c2):
    print('Boxes are equal')
elif (a1 >= a2) and (b1 >= b2) and (c1 >= c2):
    print('The first box is larger than the second one')
elif (a1 <= a2) and (b1 <= b2) and (c1 <= c2):
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
    
#R
a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
    ###
ans1 = (a1//a2) * (b1//b2) * (c1//c2)
ans2 = (a1//a2) * (b1//c2) * (c1//b2)
ans3 = (a1//b2) * (b1//a2) * (c1//c2)
ans4 = (a1//b2) * (b1//c2) * (c1//a2)
ans5 = (a1//c2) * (b1//a2) * (c1//b2)
ans6 = (a1//c2) * (b1//b2) * (c1//a2)
if (ans2 <= ans1):
    ans2 = ans1
if (ans4 <= ans3):
    ans4 = ans3
if (ans6 <= ans5):
    ans6 = ans5

if (ans2 <= ans4):
    ans2 = ans4
if (ans2 <= ans6):
    print(ans6)
else:
    print(ans2)
    
#S
n = int(input())
if (5 <= n <= 20) or (n%10 == 0) or (5 <= (n%10) <= 9):
    print(n, 'korov')
elif (n%10 == 1):
    print(n, 'korova')
elif (2 <= (n%10) <= 4):
    print(n, 'korovy')

#T
n = int(input())
if ((n % 5 == 0) and (n > 0)) or ((n % 3 == 0) and (n > 0)):
    print('YES')
elif (((n - 3) % 5 == 0) and ((n-3) > 0)) or (((n - 5) % 3 == 0) and ((n-5) > 0)):
    print('YES')
elif (((n - 2*3) % 5 == 0) and ((n-2*3) > 0)) or (((n - 2*5) % 3 == 0) and ((n-2*5) > 0)):
    print('YES')
elif ((n - 3*3) % 5 == 0) and ((n-3*3) > 0):
    print('YES')
elif ((n - 4*3) % 5 == 0) and ((n-4*3) > 0):
    print('YES')
else:
    print('NO')
    
#U
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a == b == 0):
    print('INF')
else:
    b = -b
    d = -d
    if (c != 0) and (a != 0):
        if ((b // a) != (d // c)) and (b % a == 0):
            print(b // a)
        else:
            print('NO')
    else:
        if (a == 0) or (b % a != 0):
            print('NO')
        else:
            print(b // a)

#V
k = int(input())
m = int(input())
n = int(input())
if (k >= n):
    print(2 * m)
else:
    print(((2*n + k - 1) // k) * m)

#W
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())
    ###
l1 = b1 - a1
l2 = b2 - a2
l3 = b3 - a3
    ###
if (a1 <= a2):
    r12 = a2 - b1
else:
    r12 = a1 - b2

if (a2 <= a3):
    r23 = a3 - b2
else:
    r23 = a2 - b3

if (a1 <= a3):
    r13 = a3 - b1
else:
    r13 = a1 - b3
    ###
if ((r23 <= 0) and ((r13 <= 0) or (r12 <= 0))) or ((r13 <= 0) and ((r23 <= 0) or (r12 <= 0))) or ((r12 <= 0) and ((r13 <= 0) or (r23 <= 0))):
    print('0')
elif (r23 <= 0) or (l1 >= r23):
    print('1')
elif (r13 <= 0) or (l2 >= r13):
    print('2')
elif (r12 <= 0) or (l3 >= r12):
    print('3')
else:
    print('-1')
    
#X
l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
lc = int(input())
wc = int(input())
hc = int(input())
    ###
l1l2 = l1 + l2
l1w2 = l1 + w2
w1l2 = w1 + l2
w1w2 = w1 + w2
    ###
if (h1 <= hc) and (h2 <= hc):
    if (l1l2 <= lc) and (w1 <= wc) and (w2 <= wc):
        print('YES')
    elif (l1w2 <= lc) and (w1 <= wc) and (l2 <= wc):
        print('YES')
    elif (w1l2 <= lc) and (l1 <= wc) and (w2 <= wc):
        print('YES')
    elif (w1w2 <= lc) and (l1 <= wc) and (l2 <= wc):
        print('YES')
    elif (l1 <= lc) and (l2 <= lc) and (w1w2 <= wc):
        print('YES')
    elif (l1 <= lc) and (w2 <= lc) and (w1l2 <= wc):
        print('YES')
    elif (w1 <= lc) and (l2 <= lc) and (l1w2 <= wc):
        print('YES')
    elif (w1 <= lc) and (w2 <= lc) and (l1l2 <= wc):
        print('YES')
    elif (h1 + h2 <= hc):
        if (l1 <= lc) and (w1 <= wc) and (l2 <= lc) and (w2 <= wc):
            print('YES')
        elif (l1 <= lc) and (w1 <= wc) and (w2 <= lc) and (l2 <= wc):
            print('YES')
        elif (w1 <= lc) and (l1 <= wc) and (l2 <= lc) and (w2 <= wc):
            print('YES')
        elif (w1 <= lc) and (l1 <= wc) and (w2 <= lc) and (l2 <= wc):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
