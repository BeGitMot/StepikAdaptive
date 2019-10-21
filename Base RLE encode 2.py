import collections

def split_encode_series(s):
    c = collections.Counter()
    for a in s:
        c[a] += 1

    return {c[i] : i for i in c.keys()}

def split_encode_series_gen(s):
    c = collections.Counter()
    for a in s:
        c[a] += 1

    for i in c.keys():
        yield (c[i], i)

def encode_series(series):
    return ''.join([(str(i[0]) if i[0] > 1 else "") + i[1] for i in series])



#aaabccccCCaB


series = split_encode_series_gen("aabbbB")
print(encode_series(series))


