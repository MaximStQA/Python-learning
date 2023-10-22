"""Создайте словарь, содержащий имена и возраста. Найдите и выведите средний возраст"""

# my_dick = {"Sasha": 108, "Maxim": 203, "Dunkan": 748}
# print(f'средний возраст джентельменов: {(my_dick["Sasha"] + my_dick["Maxim"] + my_dick["Dunkan"]) / 3}')
# print(f'{sum(my_dick.values()) / len(my_dick)}')


"""У вас есть словарь с именами и возрастами. Найдите имя человека с заданным возрастом"""

# my_dict = {"Sasha": 108, "Maxim": 108, "Dunkan": 748}
# age = int(input("возраст: "))
# names = []
# if age in my_dict.values():
#     for k, v in my_dict.items():
#         if v == age:
#             print(f"это {age} : {''.join(k)}")
#             names.append((k,v))
# else:
#     print("пока не воплащён")
# print(names)



"""Имеется словарь. Создайте новый словарь, в котором ключи становятся значениями и наоборот"""

# my_dict = {"Sasha": 108, "Maxim": 208, "Dunkan": 748}
# new_dict = {}
#
# for k,v in my_dict.items():
#     new_dict[v] = k
# print(new_dict)


"""Создайте словарь с числовыми значениями. Найдите ключ, который соответствует максимальному значению."""

# my_dict = {"a": 1, "Sasha": 108, "Maxim": 108, "Dunkan": 748}
# max_value = max(my_dict.values())
# for k,v in my_dict.items():
#     if v == max_value:
#         print(f"{max_value}: {''.join(k)}")


"""Имеются два словаря. Создайте третий словарь путем объединения двух, добавив значения для общих ключей."""

# my_dict = {"a": 1, "Sasha": 108, "Maxim": 108, "Dunkan": 748}
# my_dict_1 = {"a": 2, "Sasha": 10976, "Max": 10887567, "Dun": 749688}
# my_dict_2 = my_dict.copy()
# print(my_dict_2)
# for k,v in my_dict_1.items():
#     if k in my_dict_2:
#         my_dict_2 = my_dict_2 | {k + "1":v}
#     else:
#         my_dict_2 = my_dict_2 | {k:v}
# print(my_dict_2)


"""Создайте словарь. Удалите из словаря все элементы, значения которых числа со значением меньше 10."""
# my_dict = {"A": 10, "B": 5, "C": 20, "D": 15, "E": 25}
# my_dict_1 = my_dict.copy()
#
# for k,v in my_dict_1.items():
#     if v < 10:
#         del my_dict[k]
# print(my_dict)



"""Преобразуйте словарь в список кортежей, где первый элемент кортежа - ключ, а второй - значение."""

# my_dict = {"Sasha": 108, "Maxim": 108, "Dunkan": 748}
# a =[]
# for k, v in my_dict.items():
#     a.append((k,v))
# print(a)
