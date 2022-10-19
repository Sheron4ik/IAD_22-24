#A
n = int(input())
k = int(input())
print(k // n)

#B
n = int(input())
k = int(input())
print(k % n)

#C
n = int(input())
print(2**n)

#D
n = int(input())
print(n % 10)

#E
n = int(input())
print(n // 10)

#F
n = int(input())
print((n // 10) % 10)

#G
n = int(input())
print((n // 100) + ((n // 10) % 10) + (n % 10))

#H
n = int(input())
print((n + 1) % 2)

#I
n = int(input())
n += 1
print(n + (n % 2))

#J
print('A'*100)

#K
n = int(input())
print('   _~_    ' *n)
print('  (o o)   ' *n)
print(' /  V  \  ' *n)
print('/(  _  )\ ' *n)
print('  ^^ ^^   ' *n)

#L
n = int(input())
print((int((str(n))*100))**2)

#M
name = input()
print("Hello, ", name, "!", sep='')

#N
n = int(input())
print("The next number for the number ", n, " is ", n + 1, ".", sep='')
print("The previous number for the number ", n, " is ", n - 1, ".", sep='')

#O
v = int(input())
t = int(input())
print((v*t) % 109)

#P
n = int(input())
print((n // 60) % 24, n % 60)

#Q
n = int(input())
print((n // 3600) % 24, ':', ((n // 60) % 60) // 10, ((n // 60) % 60) % 10, ':', (n % 60) // 10, (n % 60) % 10, sep='')

#R
a = int(input())
b = int(input())
n = int(input())
print((a * n) + ((b * n) // 100), (b * n) % 100)

#S
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
print((h2*3600 + m2*60 + s2) - (h1*3600 + m1*60 + s1))

#T
n = int(input())
m = int(input())
print((m + n - 1) // n)

#U
h = int(input())
a = int(input())
b = int(input())
print((((h - a) + (a - b) - 1) // (a - b)) + 1)

#V
n = int(input())
print((n // 100) - (((n % 100) % 10) * 10) - ((n % 100) // 10) + 1)

#W
a = int(input())
b = int(input())
print((a // b * a + b // a * b) // (a // b + b // a))

#X
a = int(input())
b = int(input())
print('YES'*(1 - a % b) + ((a % b + 2) // (a % b + 1) % 2)*'NO')
