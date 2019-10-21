n = int(input())
print("".join([(str(i) + " ")*i for i in range(n+1)])[0:n*2])