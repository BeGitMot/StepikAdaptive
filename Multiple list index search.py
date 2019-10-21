n = input().split()
s = input()

for i, c in enumerate(n):
    print (i, end=" ") if c == s else print ("", end="")

