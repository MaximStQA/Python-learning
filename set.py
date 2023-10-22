my_set = {1, 2, 3, 3} # сожержит только неизменяемые обьекты
print(my_set, id(my_set))

my_set_1 = set('Sasha') # функция set() создаёт множество из итерируемого обьекта
print(my_set_1)

for i in my_set_1:
    print(i)

if 2 in my_set:
    print('есть')

my_set.add(1.4) # добавить только 1 элемент
print(my_set, id(my_set))

my_set.update((1, 3, 4)) # добавить все элементы из итерируемого обьекта
print(my_set)

my_set.discard(5) # удалить только 1 элемент без вывода ошибки
print(my_set)

my_set.remove(2) # удалить только 1 элемент с выводом ошибки
print(my_set)

a = my_set_1.pop() # удаляет случайно
print(a)

my_set.clear()
print(my_set)

my_list = [1, 1, 1, 1, 3, 4, 5, 1, 1, 5, 6, 7]
my_set = list(set(my_list))
print(my_set)