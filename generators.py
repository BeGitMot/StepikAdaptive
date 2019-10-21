'''
a = [1, 2, 3]
a = [i+10 for i in a]
print (a)

#В генератор списка можно добавить условие
from random import randint
nums = [randint(1, 2000) for i in range(10)]
nums = [i for i in nums if i%2 == 0]
print (nums)

#Генераторы списков могут содержать вложенные циклы:
a = "12"
b = "3"
c = "456"
comb = [i+j+k for i in a for j in b for k in c]
print(comb)

#Если в выражении генератора списка заменить квадратные скобки на фигурные, то можно получить не список, а словарь:
a = {i:i**2 for i in range(11,15)}
print (a)

#генератор
a = (i for i in range(2, 8))
for i in a:
 print(i)
'''

def gen(n):
   for i in range(n):
      yield i**2

for x in gen(100):
 print (x)

