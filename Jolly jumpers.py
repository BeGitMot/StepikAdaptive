s = [int(n) for n in input().split()]

if {abs(s[i-1] - s[i]) for i in range(1, len(s))} == {i for i in range(1, len(s))}:
    print ('Jolly')
else:
    print ('Not jolly')
