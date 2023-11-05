"""Заполнить список нулями, кроме первого и последнего элементов, которые должны быть равны единице."""

# # my_list = [2, 2, 2, 2, 2, 2]
# print(my_list)
# my_list[:] = [1, 0, 0, 0, 0, 1]
# print(my_list)

"""Заполнить список нулями и единицами, при этом данные значения чередуются, начиная с нуля."""

# my_list = [1, 2, 3, 4, 5]
#
# for i in range(len(my_list)):
#     if i % 2 == 0:
#         my_list[i] = 0
#
#     else:
#         my_list[i] = 1
#
# print(my_list)


# size = 5
# my_list = []
#
# for i in range(size):
#     if i % 2 == 0:
#         my_list.append(0)
#     else:
#         my_list.append(1)
#
# print(my_list)

"""Заполнить список последовательными нечетными числами, начиная с единицы."""

# size= 20
# my_list = []
# for i in range(size):
#     if i % 2 != 0:
#         my_list.append(i)
# print(my_list)

"""Сформировать убывающий список из чисел, которые делятся на 3."""

# size = 30
# my_list = []
# for i in range(size):
#     if i % 3 == 0:
#         my_list.append(i)
# print(my_list[::-1])