a1 = ' -- '
a2 = '|  |'
a3 = '    '
a4 = '   |'
a5 = '|   '

d = {'0': [a1, a2, a2, a3, a2, a2, a1],
     '1': [a3, a4, a4, a3, a4, a4, a3],
     '2': [a1, a4, a4, a1, a5, a5, a1],
     '3': [a1, a4, a4, a1, a4, a4, a1],
     '4': [a3, a2, a2, a1, a4, a4, a3],
     '5': [a1, a5, a5, a1, a4, a4, a1],
     '6': [a1, a5, a5, a1, a2, a2, a1],
     '7': [a1, a4, a4, a3, a4, a4, a3],
     '8': [a1, a2, a2, a1, a2, a2, a1],
     '9': [a1, a2, a2, a1, a4, a4, a1]
     }

n = input()

print ("X" + "-"*(len(n)*5 - 1) + "X")
for row in range(7):
    print ("|", end="")
    for i, c in enumerate(n):
        print (d[c][row], sep = "", end = "")
        if i != len(n)-1:
            print(" ", end="")
    print("|")
print ("X" + "-"*(len(n)*5 - 1) + "X")




