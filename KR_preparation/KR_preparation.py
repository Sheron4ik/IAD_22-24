#A
a, b, n = map(int, input().split())
print(a*n +(b*n) // 100, (b*n) % 100)

#B
n = int(input())
m = int(input())
print((m + n - 1) // n)

#C
n, m = map(int, input().split())
k, p = map(int, input().split())
for i in range(k, n+1, k):
    for j in range(p, m+1, p):
        print(i, j//10, j%10, sep='')

#D
n = int(input())
inp = list(map(int, input().split()))
cur = 0
ans = inp
while (ans != ans[::-1]):
    cur += 1
    ans = inp + inp[:cur][::-1]
print(cur)
print(*inp[:cur][::-1])

#E
def fib_str(i):
    if i == 1:
        return 'a'
    if i == 2:
        return 'b'
    return fib_str(i-2)+fib_str(i-1)

i = int(input())
print(fib_str(i))

#F
n = int(input())
inp = []
for i in range(n):
    inp.append(input())
inp.sort(key = lambda word: len(word))
inp.sort(key = lambda word: word.count('a')+word.count('e')+word.count('i')+word.count('o')+word.count('u'), reverse=True)
for word in inp:
    print(word)
