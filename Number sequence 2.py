n = int(input())

def gen(n):
    s = "".join([(str(i))*i for i in range(n+1)])
    for i in range(n):
        yield s[i]

a = gen(n)
for k in a:
    print(*k, end=' ')