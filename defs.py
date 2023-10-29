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
def send_email(): # () -> сюда передаём какие-то параметры
    email = 'Саня нихера не понятноб обьясни ещё раз!!!'
    print(email)

send_email()
send_email()
send_email()
