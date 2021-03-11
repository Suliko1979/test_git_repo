# Задание 1. Нужно найти дубликаты и вывести их на экран.
num_list = [1,1,2,3,3,5,6,7]

def dup_finder():
    for i in num_list:
        if num_list.count(i) > 1:
            print(i)

dup_generator = set([i for i in num_list if num_list.count(i)>1])

dup_lambda = tuple(filter(lambda i: num_list.count(i)>1, num_list))

# Задание 2. Найти сумму от 1 до 100
a = 1
b = 0
while a<101:
    b = b+a
    a = a+1
print(b)

sum_of_numbers = [i for i in range(1,101)]

print(sum(sum_of_numbers))

from functools import reduce
sum_reduce = reduce(lambda acc, i: acc + i, sum_of_numbers)
print(sum_reduce)

# Задание 3. Найти четные числа от 1 до 497
a = 1
b = 497
for i in range(a,b):
    if i % 2==0:
        print(i)

evens_generator = list([i for i in range(1,498) if i%2 == 0])
print(evens_generator)

evens_filter = list(filter(lambda i: i % 2 == 0, range(1,498)))
print(evens_filter)

# Задание 4. Перемножить все нечетные значения от 1 до 4987
from functools import reduce
odd_multiple = int (reduce((lambda x, y: x * y), [x for x in range(1, 4987, 2)]))
print(odd_multiple)

#Записать в массив все числа в диапазон от 54 до 9184 кратные 5
mass_generator = list([i for i in range(54,9185) if i%5 == 0])
print(mass_generator)

# Удалить пустые строки из строк
str_list = ("Я помню чудно мнгновение, передо мной явилась ты")
str_1 = list(filter(lambda item: item.strip(), str_list))


