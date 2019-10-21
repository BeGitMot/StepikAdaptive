def three_n_plus_one(n):
    if n == 1:
        res = [1]
        return res;

    res = []
    while n != 1:
        n = n * 3 + 1 if n % 2 else n / 2
        res += [int(n)]
    return res;

n = int(input())

print(three_n_plus_one(n))
