#A
a = int(input())
b = int(input())
print(*tuple(range(a, b+1)))

#B
a = int(input())
b = int(input())
if (a < b):
    print(*tuple(range(a, b+1)))
else:
    print(*tuple(range(a, b-1, -1)))

#C
n = int(input())
print(*tuple(range(10**n - 1, 10**(n-1) - 1, -2)))

#D
n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i*i
print(ans)

#E
n = int(input())
for i in range(n):
    print('+___', end=' ')
print()
for i in range(n):
    print('|', i+1, ' ', '/', sep='', end=' ')
print()
for i in range(n):
    print('|__\\', end=' ')
print()
for i in range(n):
    print('|   ', end=' ')

#F
n = int(input())
ans = 0
for i in range(n):
    tmp = int(input())
    if (tmp == 0):
        ans += 1
print(ans)

#G
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
ans = 0
for x in range(1001):
    if (x != e) and ((a*x*x*x + b*x*x + c*x + d) == 0):
        ans += 1
print(ans)

#H
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1, end='')
    print()

#I
for number in range(10, 100):
    if number == 2*(number//10)*(number%10):
        print(number)

#J
n = int(input())
ans = 0
pred_factorial = 1
for i in range(n):
    pred_factorial *= (i+1)
    ans += pred_factorial
print(ans)

#K
n = int(input())
cur_sum = 0
max_sum = 0
for i in range(n-1):
    max_sum += (i+1)
    num = int(input())
    cur_sum += num
print(max_sum + n - cur_sum)

#L
a = int(input())
b = int(input())
for num in range(a//100, b//100 + 1):
    ans = num*100 + (num%10)*10 + (num//10)
    if (a <= ans <= b):
        print(ans)
