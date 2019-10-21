import math
n = [int(i) for i in input().split("/")]
n = n[0] / n[1]

a = math.floor(n)
x = n - a
while x > 1e-10:
    print (a, end=' ')
    a = math.floor(1/x)
    x = 1/x - a
    #print(x, end=' ')

print (a)



#while True:
#    a =
#239/30
#print (n)



