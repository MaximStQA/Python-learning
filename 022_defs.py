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


def get_sum(a, b):
    c = a + b
    print('lets go') # это выполняется т.к. перед ретурн
    return c
    print('I am here') # это не выполняется т.к. после ретурн

d = get_sum(7, 9)
print(get_sum(5, 7), d)

for i in range(5):
    print(get_sum(i, 10))

