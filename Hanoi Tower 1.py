'''
Ханойская башня -- одна из широко известных головоломок, условие которой состоит в следующем:

Имеется три стержня (пронумеруем их числами 1, 2 и 3). На первом стержне находится
n
 колец с радиусами от 1 до
n
. Кольца отсортированы по радиусу, и наибольшее кольцо лежит ниже всех.

Вам требуется найти и записать алгоритм переноса всех
n
 колец с первого стержня на третий по следующим правилам:
за один ход можно переносить только одно кольцо;
нельзя класть большее кольцо на меньшее.

Программа должна вывести на экран кратчайшую последовательность действий, необходимую для того, чтобы перенести все кольца с первого стержня на третий.

Формат ввода:
Строка, содержащая положительное целое число
n
.

Формат вывода:
Порядок действий для решения головоломки. Каждое действие записывается на отдельной строке. Действие записывается в формате "номер стержня, с которого снимаем кольцо" - "номер стержня, на который надеваем кольцо" (см. пример работы программы).

Sample Input 1:

2
Sample Output 1:

1 - 2
1 - 3
2 - 3
'''
#towers = [[i for i in range(int(input()), 0, -1)], [], []]
towers = [[i for i in range(int(10), 0, -1)], [], []]
print(towers)

def top_index(tower_index):
    return len(towers[tower_index])-1

def top(tower_index):
    if isempty(tower_index):
        raise Exception('Tower {} is empty'.format(tower_index))

    return towers[tower_index][top_index(tower_index)]

def isempty(tower_index):
    return len(towers[tower_index]) == 0

def move(from_tower, to_tower):
    towers[to_tower] += top(from_tower)
    towers[from_tower] = towers[from_tower - 1][0: top_index(from_tower) - 1]

#def can_move(from_tower, to_tower):
#    if towers[to_tower - 1][]

print (top(1))

#print (towers)
'''
    

print (tower_1)
'''