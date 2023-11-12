a = 'Sahsa'
b = a
# print(b)

pechatat = print

# pechatat(b)

# print = 'какое-то говно'

# pechatat(print)

# print(a)

my_list = [1, 2, 3, 4]
# send_email = my_list
# print(send_email)

my_list_1 = ['a', 'b']


# send_email = my_list_1
# print(send_email)


# DRY - don't repeat yourself
# def send_email():  # () -> сюда передаём какие-то параметры
#     email = 'Саня нихера не понятно обьясни ещё раз!!!'
#     print(email)
#
#
# send_email()
# Супер комбо клавиш для редактирования кода по PEP 8 - Ctrl + Alt + L

# def greetings(name, surname): # > name - параметр
#     print(f'Hello {name} {surname}')
#
#
# greetings('Max', 'Stulov') # 'Max' - > аргумент

# greetings() - вернёт ошибку т.к. не передал агументов


# def get_sum(a, b):
#     c = a + b
#     print('lets go') # это выполняется т.к. перед ретурн
#     return c
#     print('I am here') # это не выполняется т.к. после ретурн
#
# d = get_sum(7, 9)
# print(get_sum(5, 7), d)
#
# for i in range(5):
#     print(get_sum(i, 10))



# def vot_3_znachenia(a, b, c):
#     d = a
#     v = c
#     y = b
#     return d**2, v, y+2 # можно возвращать более одного объекта
#
# print(vot_3_znachenia(2, 2, 2)[0])


# def get_max(x, y):
#     return x if x > y else y # тернарный оператор
#
#
# def get_max_1(a, b, c):
#     d = get_max(a, get_max(b, c))
#     return d
#
# x = 5
# y = 7
# z = 10
#
# # a = get_max(x, get_max(y, z))
# a = get_max_1(x, y, z)
# print(a)


# def fn(x, y, z, s = 'Pasha'): # s - параметр по умолчанию
#     print(f'Hello {x}')
#     print(y)
#     print(z)
#     print(s)
#
# v = 'Olec'
# fn('Sasha', z = 'Max', y = v, s = 'Zina') # z = 'Max' - именованный аргумент
#
# """Вначале позиционные аргументы, затем именованные
# те аргументы параметры которых определены по умолчанию можно не передавать"""


# def cmp_str(str1, str2, registr = True, trim = True): # если первая больше второй
#     if registr:
#         str1 = str1.lower()
#         str2 = str2.lower()
#     if trim:
#         str1 = str1.strip()
#         str2 = str2.strip()
#     return True if str1 >= str2 else False
#
#
# print(cmp_str('  Sasha', 'sasha', trim=False))
#
# print('123','333', sep = '\n', end = '\t')
# print('456')




