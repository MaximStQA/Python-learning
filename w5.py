"""Замените в строке все вхождения 'word' на 'letter'."""

# a = "wordXXwordXXword"
# print(a.replace("word", "letter"))


"""Удалите в строке все буквы 'x'. за которыми следует 'abc'."""

# a = "xabcwwwxabcwwwxyabc"
# print(a.replace("xabc", "abc", a.count("xabc")))

"""Удалите в строке все 'abc', за которыми следует цифра."""

a = "abcabc1abc2abc3abc4abc"
lenth = len(a)
#1 b = ["abc0", "abc1","abc2", "abc3", "abc4", "abc5", "abc6", "abc7", "abc8", "abc9"]

b = a.split("abc")
print(b)
c = 0
#1 for i in b:
    # a = a.replace(i, f"{c}")
    # c += 1
#1print(a)


    ######if a[i:i+3] == "abc" and i + 3 < lenth and a[i+3].isdigit():

"""Найдите количество вхождения 'aba' в строку."""

# a = "aba1aba2aba3abb4"
# print(a.count("aba"))

"""Удалить в строке все лишние пробелы, 
то есть серии подряд идущих пробелов заменить на одиночные пробелы. 
Крайние пробелы в строке удалить."""

"""Дан текст. Найдите наибольшее количество идущих подряд цифр."""

"""Дан текст. Найти сумму имеющихся в нем цифр."""

# a = "uhuu1ubuy2uhbuvug3"
# sum_digit = 0
# for i in a:
#         if i.isdigit():
#                 digit = int(i)
#                 sum_digit += digit
# print(sum_digit)


"""Дан текст. Найти слова, состоящие из цифр, и сумму чисел, которые образуют эти слова.

Дан текст. Найдите наибольшее количество подряд идущих пробелов в нем.

Даны два слова. Найдите только те символы слов, которые встречаются в обоих словах только один раз."""