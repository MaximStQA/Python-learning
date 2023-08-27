# for i in [1, 2, 3]:
#     print(i)
# Итератор - конструкция для перебора элементов итеррируемого объекта

# функция iter() - для вызова обьекта итератора для однократного
# перебора элементов
# my_list = [4, 10, 3]
# i = iter(my_list) # или range()
#
# функция next() - для перхода к следующему элементу - возвращает
# следующий элемент
# print(next(i))
# if next(i) > 0:
#     print('ok')
#
#
# print(next(i) * 20)
# # print(next(i))
#
# try:
#     print(next(i))
# except:
#     print('конец итераций')

# [(<операция над x>, <операция над> y)
# for x in <итерируемый обьект> if ...
# for y in <итерируемый обьект> if ...]

for i in range(3):
    for j in range(3):
        print(i, j)

# вложенный генератор списка
my_list = [(x, y) for x in range(3) if x < 2
                for y in range(3)]
print(my_list)