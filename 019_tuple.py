korteg = (1, 2, 3, 4, '123')
""" Упорядоченная но НЕ изменяемая колекция данных """

kort = 5, 6, 7
print(kort)

kor = (1,)
print(kor)

ko = ()
print(type(ko))

k = tuple('1,2,3')
print(k)
v = 'a', 'b', 'c'
x, y, z = v
print(v)
print(x, y, z)

print(len(korteg))
print(korteg[0], korteg[4])

print(korteg[1:-1])

g = 7, 8, 9 # В отличии от списка срез [:] не сздаёт копию,
            # а ссылается на тот же обьект
n = g[:]
print(id(g), id(n), sep='\n')

ko = ko + kor
print(ko)

print(g, list(g), sep='\n')
print((1,) * 10)

"""Самый важный момент"""
strange = (1, "234", [1,2,3]) # strange[0], strange[1]....
print(strange)
strange[2].append(4)
print(strange)
"""Tuple - это набор ссылок на обьекты в памяти"""