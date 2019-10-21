'''
def modify_list(lst):
    while True:
        index_found = -1
        for i in range(len(lst)):
            if lst[i] % 2 != 0:
                index_found = i;
                break;
        if index_found >= 0:
            lst.pop(index_found)
        else:
            break

    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] // 2

def modify_list(l):
    r = []
    while l:
        x = l.pop()
        if not x % 2:
            r.append(x//2)
    while r:
        l.append(r.pop())
'''

def modify_list(numbers):
    numbers[:] = [i//2 for i in numbers if i%2 == 0]

lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
modify_list(lst)

print (lst)
