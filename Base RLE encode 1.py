from itertools import groupby
#aaabccccCCaB

a = [list(g) for k, g in groupby(input())]

res = [(str(len(x)) if len(x) > 1 else "") + x[0] for x in a]

print (*res, sep = "")










