"""Найдите сумму и произведение элементов списка."""

# my_list = [1, 2, 3, 4, 5]
# print(sum(my_list))
#
#
# x = 1
# for i in my_list:
#     x *= i
# print(x)

"""Найдите сумму четных чисел списка."""

# my_list = [1, 2, 3, 4, 5]
# my_list_sum = 0
# for i in my_list:
#     if i % 2 == 0:
#         my_list_sum += i
# print(my_list_sum)


"""Найдите сумму нечетных чисел списка, которые не больше 11"""

# my_list = [1, 2, 13, 4, 5]
# x = 0
# for i in my_list:
#     if i % 2 != 0 and i < 11:
#         x += i
# print(x)

# my_list = [1, 2, 13, 4, 5]
#
# x = 0
# flag = True
# while flag:
#     for i in my_list:
#         if i % 2 != 0:
#             x += i
#         else:
#             flag = False
# print(x)

# ind = 0
# result = 0
# flag = True
# while flag:
#     if my_list[ind] % 2 != 0 and my_list[ind] < 11:
#         result += my_list[ind]
#
#     ind += 1
#     if len(my_list) == ind:
#         flag = False
# print(result)







"""Найдите сумму чисел списка, которые стоят на нечетных местах и при этом больше суммы крайних элементов списка."""

# my_list = [1, 2, 3, 4, 5, 6, 7, 2]
# x = 0
# lenth = len(my_list)
# for i in range(lenth):
#     if i % 2 == 0 and my_list[i] > (my_list[0] + my_list[-1]):
#         x += my_list[i]
# print(x)


"""Дан список. Найдите два соседних элемента, сумма которых минимальна."""

# my_list = [1, 2, 3, 4, 5, 6, 7, 2]



"""Проверьте, является ли данный список возрастающим или убывающим."""

# my_list = [2, 1, 2, 3, 4, 5, 6, 7]
# my_list = [5, 4, 3]
#
# is_increase = True
# is_decrease = True
# for i in range(len(my_list) -1):
#     if my_list[i] >= my_list[i +1]:
#         is_increase = False
#
# for i in range(len(my_list) -1):
#     if my_list[i] <= my_list[i + 1]:
#         is_decrease = False
# if is_increase:
#     print("возрастающий")
# elif is_decrease:
#     print("убывающий")
# else:
#     print("ни то ни сё")



"""В списке заменить все числа, большие данного числа, на среднее арифметическое всех чисел списка."""

# my_list = [2, 1, 2, 3, 4, 5, 6, 7]
# x = 3
# my_list_sum = sum(my_list)
# lenth = len(my_list)
# midl = my_list_sum / lenth
# print(midl)
# for i in my_list:
#     if my_list[i] > x:
#         my_list[i] = midl
# print(my_list)


"""Дан список. Заменить все числа, меньшие последнего элемента списка, на первый элемент."""

# my_list = [2, 1, 2, 3, 4, 5, 6, 7]
# for i in my_list:
#     if my_list[i] != my_list[0] and my_list[i] < my_list[-1]:
#         my_list[i] = my_list[-1]
# print(my_list)

"""Поменять местами наибольший и наименьший элементы списка."""

# my_list = [2, 1, 2, 3, 4, 5, 6, 7]
# x = max(my_list)
# e = min(my_list)
# for i in my_list:
#     if my_list[i] == x:
#         my_list[i] = e
#     elif my_list[i] == e:
#         my_list[i] = x
# print(my_list)

# my_list = [2, 1, 2, 3, 4, 5, 6, 7]
# x = max(my_list)
# e = min(my_list)
# ind = 0


# while ind < len(my_list):
#     if my_list[ind] == x:
#         my_list[ind] = e
#     elif my_list[ind] == e:
#         my_list[ind] = x
#
#     ind += 1
#
# print(my_list)





"""Найти наибольший четный элемент списка и поменять его местами с наименьшим нечетным элементом."""

# my_list = [2, 3, 8, 4, 5, 6, 7]
# a = min(my_list)
# b = max(my_list)
# for i in my_list:
#      if i % 2 == 0 and i > a :
#         a = i
#      if i % 2 != 0 and i < b:
#         b = i
# e_ind_a = my_list.index(a)
# t_ind_b = my_list.index(b)
#
# my_list[e_ind_a] = b
# my_list[t_ind_b] = a
#
# print(my_list)


"""Найти в списке все серии подряд идущих одинаковых элементов и удалить из них все элементы кроме одного."""

# my_list = [2, 3, 3, 3, 8, 4, 4, 5, 6, 7]
#
# ind = 0
# flag = True
# while flag:
#     if my_list[ind] == my_list[ind + 1]:
#         my_list.pop(ind)
#         continue
#     ind += 1
#
#     if len(my_list) == ind +1:
#
#         flag = False
# print(my_list)



