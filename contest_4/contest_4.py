#A
n = float(input())
print(n - int(n))

#B
n = float(input())
dp = n - int(n)
if (dp >= 0.5):
    print(int(n + 1))
else:
    print(int(n))

#C
a = float(input())
b = float(input())
c = float(input())
p = (a + b + c)/2
print((p * (p - a) * (p - b) * (p - c)) ** (0.5))

#D
p = float(input())
x = float(input())
y = float(input())
sum_kop = 100*x + y
sum_kop += sum_kop * p / 100
print(int(sum_kop / 100), int(sum_kop % 100))

#E
p = float(input())
x = float(input())
y = float(input())
k = float(input())
sum_kop = 100*x + y
while (k != 0):
    sum_kop += int(sum_kop * p / 100)
    k -= 1
print(int(sum_kop / 100), int(sum_kop % 100))

#F
s = input()
p = s.split('.')
print(p[0], int(p[1]))

#G
n = int(input())
ans = 1
for i in range(2, n+1):
    ans += 1/(i*i)
print(ans)

#H
n = int(input())
x = float(input())
a = float(input())
ans = a
for i in range(n):
    a = float(input())
    ans = ans*x + a
print(ans)

#I
a = float(input())
b = float(input())
c = float(input())

d = b*b - 4*a*c
if (d == 0):
    print(-b / (2*a))
elif (d > 0):
    d = d**0.5
    x1 = (-b - d) / (2*a)
    x2 = (-b + d) / (2*a)
    if (x1 > x2):
        print(x2, x1)
    else:
        print(x1, x2)
        
#J
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

y = (a*f - c*e) / (a*d - b*c)
x = (e*d - f*b) / (a*d - b*c)

print(x, y)

#K
s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[-1::-2])
print(len(s))

#L
w = input().split()
print(len(w))

#M
w = input().split()
print(w[1], w[0])

#N
s = input()
l, r = s.find('f'), s.rfind('f')
if (l != -1):
    if (l == r):
        print(l)
    else:
        print(l, r)
        
#O
s = input()
l, r = s.find('h'), s.rfind('h')
ans = s[:l] + s[r + 1:]
print(ans)

#P
s = input()
l = s.find('f')
if (l != -1):
    sr = s[l + 1:]
    lr = sr.find('f')
    if (lr != -1):
        print(lr + l + 1)
    else:
        print(-1)
else:
    print(-2)
    
#Q
s = input()
l, r = s.find('h'), s.rfind('h')
ans = s[:l+1] + 2*s[l+1:r] + s[r:]
print(ans)

#R
s = input()
print(s.replace('1', 'one'))

#S
s = input()
print(s.replace('@', ''))

#T
s = input()
l, r = s.find('h'), s.rfind('h')
if (l == -1) or (l == r):
    print(s)
else:
    ts = s[l+1:r]
    print(s[:l+1] + ts.replace('h', 'H') + s[r:])
    
#U
a = float(input())
b = float(input())
c = float(input())

if (a != 0):
    d = b*b - 4*a*c
    if (d == 0):
        print(1, -b / (2*a))
    elif (d > 0):
        d = d**0.5
        x1 = (-b - d) / (2*a)
        x2 = (-b + d) / (2*a)
        if (x1 > x2):
            print(2, x2, x1)
        else:
            print(2, x1, x2)
    else:
        print(0)
else:
    if (b != 0):
        print(1, -c/b)
    else:
        if (c == 0):
            print(3)
        else:
            print(0)
            
#V
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

det = a*d - b*c
dx = e*d - f*b
dy = a*f - c*e
if (det != 0):
    x = dx / det
    y = dy / det
    print(2, x, y)
else:
    if (dx == 0) and (dy == 0):
        if (a == b == c == d == 0):
            if (e == f == 0):
                print(5)
            else:
                print(0)
        else:
            if (a == c == 0):
                if (b == 0):
                    print(4, f / d)
                else:
                    print(4, e / b)
            else:
                if (b == d == 0):
                    if (a == 0):
                        print(3, f / c)
                    else:
                        print(3, e / a)
                else:
                    if (b == 0):
                        print(1, -c / d, f / d)
                    else:
                        print(1, -a / b, e / b)
    else:
        print(0)
        
#W
s = input()
for i in range(len(s)-1):
    print(s[i], end='*')
print(s[len(s)-1])

#X
s = input()
ans = ''
for i in range(len(s)):
    if (i % 3 != 0):
        ans += s[i]
print(ans)
