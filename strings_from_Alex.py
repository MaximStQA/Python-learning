# лексикографическое сравнение
a = ord('q')


name = 'SashaKomarov'
surname = '1234'

# print(name[1], name[2], name[3])
# print(name[0], name[-1], name[-2])

# print(name[5]) # несуществующий индекс вернёт ошибку

#print(name[-1:0:-1]) # [start:stop(не включительно):step]

# print(len(name) - 1) # получить последний индекс

# print(name.upper())
# print(name.lower())
# print(surname.count(''))
# print(name.count('ov'))
# print(name.find("a", 5, 10)) # find(obj, start index, end index(не включительно))
# print(name.rfind('a'))
# print(name.index('g')) index(obj, start index, end index(не включительно))
# print(name.replace('a', '!', 2))
# print(name.isalpha()) # состоит ли обьект только из букв
# print(surname.isalpha())
# print(surname.isdigit()) # состоит ли обьект только из цифр
# print(name.isalnum()) # состоит ли обьект только из цифр и букв
# print(name.rjust(15, '!')) # дополни до указанного количесва символами
# print(name.ljust(15, '!'))
# print(name.center(18, '!'))
ful_name = 'Komarov, Alex ander, Serge evich'
# print(ful_name.split(',')) # делит строку на части разделителем(параметром)
# h =', '.join('123') # соеденить элементы
# print(h)
# my_string = '|'.join(ful_name.split(',')[0])
""" возьми обьект full_name, раздели его методом 
split используя запятую как разделитель, из полученного 
списка возьми нуловой элемент, объедени его елементы 
символом '|' с помощью join """
# print(my_string)
