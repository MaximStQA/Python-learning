
"""1. Сокращенные операторы (+=, -=, *=, /=):
1.Создайте переменную x с начальным значением 10. 2
Прибавьте к ней 5, затем вычтите 3, затем умножьте на 2,
затем поделите на 3. Используйте сокращенные операторы и
выводите значение x после каждой операции."""
import math

"""x = int(input("x: "))
x +=5
print(x)
x -= 3
print(x)
x *= 2
print(x)
x /= 3
print(x)
y = ((x + 5) - 3) * 2 / 3
print(y)"""


"""2.Напишите программу, которая в цикле от 1 до 10 включительно 
умножает текущий номер итерации на предыдущее значение переменной. 
Используйте сокращенный оператор умножения.
(для написания цикла от 1 до 10 используйте следующий синтаксис: for i in range(1, 11):  ...)


b = 1
for i in range(1, 11):
    b *= i
    print(b)"""

"""Функции (abs, min, max, pow, round):
3.Напишите программу, которая запрашивает у пользователя три числа 
и выводит наибольшее и наименьшее из них с помощью функций max и min.
(внутри функций max и min можно перечислять элементы для нахождения через запятую)

A = [10, 17, 22, 112]
print(min(A))
print(max(A))"""

"""4.Создайте переменные a и b, присвойте им значения, 
а затем выведите абсолютное(т.е. по модулю) значение разности этих переменных.

a = 7.7
b = 4
print(abs(a - b))"""

"""5.Создайте две переменные base и exp 
и выведите результат возведения base в степень exp с помощью функции pow.

base = 5
exp = 3
c = pow(base, exp)
print(c)"""

"""6.Введите число с плавающей точкой и выведите его округленное значение с помощью функции round.

D = float(input("e: "))
print(round(D))"""

"""Модуль math (ceil, floor, factorial, sqrt, pi):
7.Введите число с плавающей точкой и выведите ближайшее большее 
и меньшее целые числа с помощью функций math.ceil и math.floor."""

# f = 3.14
# print(math.ceil(f))
# print(math.floor(f))

"""8.Введите положительное целое число и 
выведите его факториал с помощью функции math.factorial.

g = 5
print(math.factorial(g))"""

"""9.Введите число и выведите его квадратный корень с помощью функции math.sqrt.

h = 121
print(math.sqrt(h))"""

"""10.Напишите программу, которая запрашивает у пользователя радиус круга 
и вычисляет его площадь с использованием math.pi.

i = int(input("Радиус: "))
area = math.pi * i * 2
print(area)"""

"""Аргумент sep в функции print():
11.Напишите программу, которая выводит числа от 1 до 5 в одной строке, разделенные знаком "-".

a = 1
b = 2
c = 3
d = 4
e = 5
print(a, b, c, d, e, sep = '-')"""


"""12. Напишите программу, которая выводит каждое слово списка 
('Hello', 'world', 'I', 'am', 'learning', 'Python') в на новой строке.

a = "Hello World I am learn Python"
words = a.split()
for word in words:
    print(word)"""

"""Аргумент end в функции print():
13.Напишите программу, которая выводит две строки текста 
(или 2 вызова функции print()) в одной строке. 
Воспользуйтесь аргументом end в первом вызове print(), чтобы предотвратить перевод на новую строку.

a = "Hello World I am learn Python"
print("Hello World", end = '!')
print("I am learn Python")"""

"""14.Напишите программу, которая выводит числа от 1 до 5 в одной строке, 
причем после каждого числа, кроме последнего, стоит знак " - ", 
а после последнего числа стоит знак " ! ". """

a = 1
b = 2
c = 3
d = 4
e = 5
print(a, b, c, d, e, sep= '-', end='!')

"""15.Напишите программу, которая выводит три слова 
(например, "Hello", "world", "Python") в одной строке без пробелов. 
Используйте end, чтобы удалить пробел после первого и второго слов.

a = "Hello"
b = "World"
c = "Python"
print(a, end='')
print(b, end='')
print(c, end='!')"""



