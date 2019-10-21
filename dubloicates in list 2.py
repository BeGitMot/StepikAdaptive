import collections

c = collections.Counter()

for n in [int(i) for i in input().split()]:
    c[n] += 1

print(*[x for x in c if c[x] > 1])
