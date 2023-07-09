# if True:
#     print('Say hi')

# if not 1 > 0 and 3 != 0 or 2 == 2:
#     print('yes')
#     a= 1
#     b = 3
#     c = 'asd'
# else:
#     a = 2
#     b = 4
#     c = 6
#
#
# if 0 > 1:
#     print('yes')
#     print('yes')
#     a = 1
#     b = 3
#     c = 'asd'
"""
1. Саша
2. Петя
3. Максим
"""
# inp = input('Choose the name ')
# if inp == '1':
#     print('Саша')
# if inp == '2':
#     print('Петя')
# if inp == '3':
#     print('Максим')

# a = 6
# b = 2
# c = 5
# if a > b:
#     if a > c:
#         print('a наибольшее')
#     else:
#         print('с наибольшее')
# if b > a:
#     if b > c:
#         print('b наибольшее')
#     else:
#         print('с наибольшее')



# inp = input('Choose the name ')
# if inp == '1':
#     print('Sasha')
#
# elif inp == '2':
#     print('Petia')
#
# elif inp == '3':
#     print('Maxim')
#
# else:
#     print('There is no you choise')

# Тернарный оператор возвращает <что-угодно> if <условие> else <что-угодно>
a = 10 if 2 > 0 else 20
print(a)

my_list = [1, 2, 10 if 2 < 0 or 3 > 0 else 20, 0]
print(my_list)

string = 'abc' + ('10' if 2 < 0 or 3 > 0 else '20') + 'rty'
print(string)


print(max(1, 2, 10 if 2 < 0 or 3 > 0 else 20, 0))
