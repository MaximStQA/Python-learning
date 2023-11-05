my_list = [5, 2, 3.4]
my_list_2 = list('123')
# print(my_list, my_list_2)
#
print(id(my_list))
my_list[-1] = 4
print(id(my_list))
print(my_list)

# print(len(my_list))
# print(max(my_list))
# print(min(my_list))
# print(sum(my_list))
# print(sorted(my_list, reverse=True)) # возвращает новый список
# my_list = my_list + my_list_2
# print(id(my_list))
# print(my_list * 2)
# print(5 in my_list)
# del(my_list[0])
# print(my_list)

#my_list_10 = [1, 2, 3, 4, 5]
# print(my_list_10[::-1])
# my_list_11 = my_list_10[:]
# my_list_12 = my_list_10.copy() # создает новый список копию
# print(my_list_11)
#
#my_list_10[2:5] = [7, 8]   # поменять несколько элементов списка
# print(id(my_list_10[0]))
# print(my_list_10)
# print(id(my_list_10))

# new = [1, 2, 5]
# old = [1, 2, 4, 509000000]
# print(new == old, new != old, new > old, new < old)

# my_list = [1, 1, 2, 3, 1, 2]
# my_list.append(4)
# print(my_list)
#
# my_list.extend([5, 6, 7])
# print(my_list)
#
# my_list.insert(1, '123')
# print(my_list)

# my_list.remove(2) # удаляет первое вхождение искомого элемента
# print(my_list)

# a = my_list.pop(1)
# print(my_list)
# print(a)
# if 1 in my_list:
#     b = my_list.index(1)
#     print(b)
#     a = my_list.pop(b)

# my_list.clear()
# print(my_list)

# print(bool(my_list))
# my_list.clear()
# print(bool(my_list))
# print(my_list)
# my_list.sort(reverse=True, key=lambda x: x == 2)
# print(my_list)

# my_list = [[1, 2, 3], [4, 5, 6, ['a', 'b', 'c']], [7, 8, 9]]
# for i in my_list:
#     print(i)
#
# print(my_list[1][3][2])
# print('b' in my_list[1][3])
#
# #my_list[1][2] = 10
# #my_list[1].pop()
# #del(my_list[1][2])
# print(my_list)
# #
# print(my_list[1][3][:2])

