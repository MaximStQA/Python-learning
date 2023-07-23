# for i in range(5): # range(от(0 по умолчанию), до(не включая), шаг)
#     print('say hi')
#     print(i)

# summ = 0
# i = 1
# N = 10
# while i < N: # while(пока) <условие истинно(True)>: действие
#     summ += i
#     i += 1
#
# print(summ)

# login = 'Sasha'
# password = '123'
# in_log = input('Введите логин: ')
# while True:
#     if in_log != login:
#         print('Вы ввели неверный логин')
#         in_log = input('Введите логин: ')
#         continue
#     else:
#         pasw = input('Введите пароль: ')
#         if pasw != password:
#             print('Вы ввели неверный пароль')
#             in_log = ''
#             continue

my_list = [1, 2, 3, 3, 3, 4, 5, 6, 6, 7]

flag = True
while flag:
    for i in range(len(my_list) - 1):
        if my_list[i] == my_list[i + 1]:
            my_list.pop(i)
            break
    else:
        flag = False
print(my_list)





# while input('Введите пароль: ') != password:
#     print('Вы ввели неверный пароль')

# print('Вход разрешен!')
# x = 0
#
# while x < 10:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print(f'printing{x}')
#     # if x == 7:
#     #     break
#     print('++++')
# else:
#     print('Done')





