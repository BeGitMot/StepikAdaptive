n = int(input())
res = [n]
while n != 1:
    n = n * 3 + 1 if n % 2 else n / 2
    res += [int(n)]

print (*res)

'''
#пример с генератором
def gen(a):
    yield a
    while a != 1:
        a = a * 3 + 1 if a % 2 else a // 2
        yield a
print(*list(gen(int(input()))))
'''