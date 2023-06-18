string = "Hello World !"
count = string.count("")
#print(count)

a = 379
astring = str(a)
#print(type(astring), astring)
sum = 0
for i in astring:
    #print(i)
    sum = sum + int(i)

#print("Сумма цифр", a, "равна:", sum)

a = [True]
b = False

result_not = not b
#print(result_not)
#print(type(a))

#name = input("Введите ваше имя: ")
#print("Привет, " + name + "!")



"""Напишите код, который рассчитывает объем цилиндра (V = πr²h), 
где r - радиус основания (может быть float), 
h - высота (может быть int). Попросите от пользователя ввод данных."""

P = 3.14
#r = float( input("Введите float r: "))
#h = int (input("Введите высоту int h: "))

#V = P * r**2 * h
#print(V)



"""Напишите код, который преобразует градусы по Фаренгейту 
в градусы по Цельсию (формула: (F - 32) * 5/9 = C). 
В качестве значения по Фаренгейту используйте переменную."""

F = int(input("F: "))
print( (F -32) * 5/9)
#C = (F -32) * 5/9
#print(C)

# сокращённая запись
"""a = 2
a = a + 3
print(a)
a += 3
print(a)
a -= 2
print(a)
a *= 2
print(a)"""

