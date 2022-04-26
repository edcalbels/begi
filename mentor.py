# while 1:
#     first = int(input('enter first number: '))
#     second = int(input('enter second number '))
#     operation = input('Choose operation(+,-,/,*,)')

#     if operation == '+':
#         print(first + second)
#     elif operation == '-':
#         print(first - second)
#     elif second == 0:
#         print('You can not divide by zero')      
#     elif operation == '/':
#         print(first / second)
#     elif operation == '*':
#         print(first * second)
#     elif second == 0:
#         print('You can not divide by 0')
#     else:
#         print('You can choose only - + / * ')             





# Написать функцию, которая возвращает первое слово из полученного предложения. 

# В качестве параметра по умолчанию указать строку “Hello World”
# Функция должна Вернуть False, если переданный аргумент не является строкой.
# Если в указанном предложении только одно слово, то вернуть это слово.

# Написать функцию, которая принимает неограниченное количество чисел и возвращает 
# их среднее арифметическое.

# Среднее арифметическое должно быть в виде целого числа.
# Использовать звёздочку для обозначения последовательности аргументов.

# Написать функцию, проверяющую надежность пароля.

# Возвращать True если пароль содержит не менее 6 символов, состоящих из цифр и букв, 
# в противном случае вернуть False


# Имена функций как и переменные должны соответствовать своему содержанию или поведению! 
# Постарайтесь придумать правильные  по смыслу названия, за непонятные названия функций будет снижен балл!



# ДЗ 5 сохранить в  файле под названием Имя_группа_HW_5.py
# и отправить мне в лс.     
# (В случае затруднений с дз, пишите в группу, также вы можете обратиться за помощью к вашим Менторам в лс)






# Написать функцию, которая возвращает первое слово из полученного предложения. 

# В качестве параметра по умолчанию указать строку “Hello World”
# Функция должна Вернуть False, если переданный аргумент не является строкой.
# Если в указанном предложении только одно слово, то вернуть это слово.




# Функции, создание функций, аргументы функций


# names = ['jack', 'sam', 'kate', 'steve', 'sam', 'sam', 'kate']
# names1 = ['ali', 'said', 'umar', 'bakr', 'bakr']

# # print(names.count('sam'))
#
# def frequently(obj):
#     c = 0
#     most_f = []
#     for i in obj:
#         if obj.count(i) > c:
#             c += 1
#             most_f.append(i)
#             # print(most_f)
#     return set(most_f)
#
# print(frequently(names))
# print(frequently(names1))


# word = 'python'
# word = word.title()
#
# print(word)
#
#
# def our_title(string: str):
#
#     changed = string[0].upper()
#     changed += string[1:]
#     return changed
#
# print(our_title('geektech'))

# keyword arguments = kwargs
# def menu(**kwargs):
#     return kwargs
#
# monday = menu(dessert='курут', drink='максым')
#
# print(monday)

# def plus(a, b=3, *args):
#     print(a, '- a')
#     print(b, '- b')
#     print(args, '- args')
#     return sum(args) - (a + b)
#
# print(plus(2, 4, 5, 6))


# numbers = [0, 1, 2, 3]
# other = [3, 4, 5, 6]
#
# def new(obj):
#     return obj ** 2
#
# def square_numbers(obj):
#     for i in obj:
#         print(new(i))
#
# print(square_numbers(numbers))
# print(square_numbers(other))



# lst = [1, 2, 3, 4, 5]
# print(lst.pop(0))

# definition - определение

# def menu(first, second, dessert, drink='чай'):
#     return {
#         'first': first,
#         'second': second,
#         'drink': drink,
#         'dessert': dessert
#     }
#
# lunch = menu('борщ', "котлеты", "брауни")
# dinner = menu("фанта", "мороженое", "каша", "омлет")
# dinner1 = menu(drink="фанта", dessert="мороженое", first="каша", second="омлет")
#
# print(lunch)
# print(dinner)
# print(dinner1)


# def get_total_price(length, width, price=200):
#     return length * width * price
#
# hall = get_total_price(5, 8, 150)
# kitchen = get_total_price(100, 3, 4)



# def get_plowad(length, width):
#     return length * width
#
# square_hall = get_plowad(4, 7)
# square_kitchen = get_plowad(3, 5)
#
# def get_price(square, price):
#     return square * price

# print(get_price(square_hall, 200))
# print(get_price(square_kitchen, 120))
#
# print('total: ', get_price(square_hall, 200) + get_price(square_kitchen, 120))


# a = 5
# b = 7
# s = a * b
# print(s, "зал")
#
# price = 150
#
# result = s * price
# print(result)
#
# a = 4
# b = 3
# s = a * b
# print(s, "кухня")
#
# price = 120
#
# result = s * price
# print(result)
# --------------------------------------





# Функции, создание функций, аргументы функций

# data = ['aza', 'tema', 'aika', 'aza']
# data2 = ['uri', 'beka', 'vadya', 'beka', 'temka', 'temka', 'temka']

# def get_frequently(obj):
#     c = 1
#     most_f = None
#     for i in obj:
#         # print(i, obj.count(i))
#         if obj.count(i) > c:
#             c += obj.count(i)
#             most_f = i
#             return most_f

# print(get_frequently(data2))
# # print(get_frequently(data))

# print(get_frequently(data))
# get_frequently(data2)
# print(get_frequently(data2))

# keyword arguments
# def menu(**chetoponyatnoe):
#     return chetoponyatnoe
#
# monday = menu(dinner="каша", lunch="шаурма", drink='максым')
# tuesday = menu(dinner="каша", lunch="шаурма", drink='кымыз')
# print(monday)
# print(tuesday)

# def plus(a, *args, b=0):
#     print('a - ', a)
#     print('b - ', b)
#     print('args - ', args)
#     return sum(args) - (a + b)
#
# print(plus(1, 3, 4, 5))


# def plus(a, b, c=2):
#     return round(float(a + b * c), 2)
#
# print(plus(3, 4, ))
# print(plus(4, 2, ))
# print(plus(a=3, b=4, c=5))


# # definition - определение
# name = 'azamat'
#
#
# def menu(breakfast, lunch, dinner):
#     '''Cоставляем график трапезы на неделю.'''
#     return {
#         'breakfast': breakfast,
#         'lunch': lunch,
#         'dinner': dinner
#     }
#
#
# print(menu.__doc__)
#
# print(menu('яичница', "плов", "пельмени"))
# print(menu('шашлык', "творог", "каша"))
# print(menu(dinner='шашлык', breakfast="творог", lunch="суп"))




# def get_total_price(length, width, price):
#     return (length * width) * price
#
# price = int(input('number: '))
# hall = get_total_price(4, 6, price)
# print(hall)




# def get_square(length, width):
#     return length * width
    # price = int(input('Введите сумму за квадрат: '))

# def get_price(square, price):
#     return square * price


# badroom = get_price(get_square(3, 5), 150)


# print(badroom, '- за спальню \n',
#       hall, 'за зал')

#
# s = get_square(5, 4)
#
# _l = 150

# result = s * price_l
# print(result)


# print(type(s))
# print(s)


# length = 7
# width = 4
# s = length * width
# lenoleum = 150
# result = s * lenoleum
#
# print(s)
# print(result)
#
# length = 5
# width = 4
# s = length * width
#
# print(s)
#
# a = 5
# b = 4
# c = a + b
# print(c)
#
#
# a = 6
# b = 7
# c = a + b
# print(c)


# Написать функцию, которая возвращает первое слово из полученного предложения. 

# В качестве параметра по умолчанию указать строку “Hello World”
# Функция должна Вернуть False, если переданный аргумент не является строкой.
# Если в указанном предложении только одно слово, то вернуть это слово.


# def first_word(*args,anyway = 'Hello world'):
#     words = input('enter here any words').split()
#     for i in words:
#         print(words[0])

# first_word()        
# # query = tuple(input('Colors with space: ').split())


# def first_word(a = input('enter any words')):
#     print(first_word.split()[0])
# first_word()    






# Написать функцию, которая принимает неограниченное количество чисел
#  и возвращает их среднее арифметическое.

# Среднее арифметическое должно быть в виде целого числа.
# Использовать звёздочку для обозначения последовательности аргументов.


# def gpa():
#     a = input


# 
# реализовать операцию над дробью, то есть создать класс Fraction у него будет 2 атрибута (numertor, denumerator)
# сделать add, sub, mul, floordiv (Dunder Methods)
# по правилам математики!)

# #ExtraTask:

# Учитывая целое число x, вернуть, true если x это целое число палиндрома.

# К сведению: Целое число является палиндромом , если оно читается так же, как в прямом, так и в обратном порядке.

# Например, 121 есть палиндром, а 123 нет.