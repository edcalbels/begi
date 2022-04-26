

# DUNDER - DOUBLE UNDERSCORES


# Dunder -   Двойное подчеркивание

# __init__
# __add__
# __sub__
# __mult__

# магические методы заменяют сами методы



# class Num:
#     def __init__(self,num):
#         self.num = num

#     def _get_num(self):
#         print(self.num)


#     def __add__(self,other):
#         print('Is Dunder method __add__ ')
#         self.num  += other
#         self._get_num()   

#     def __sub__(self,other):
#         print('Is dunder method __sub__ ')
#         self.num  -= other
#         self._get_num()


#     def __mul__(self,other):
#         print('Is Dunder method __mul__ ')
#         self.num  *= other
#         self._get_num() 

#     def __floordiv__(self,other):
#         print('Is Dunder method __floordiv__ ')
#         self.num  //= other
#         self._get_num()  

#     def __truediv__(self,other):
#         print('Is Dunder method __floordiv__ ')
#         self.num  /= other
#         self._get_num()               


     

# num = Num(10)

# num + 10


# class Num2:
#     def __init__(self,num):
#         self.num = num

# num2 = Num2(20)
# num2 / 10


# class Num3(Num):
#     pass

# num3 = Num3(10)
# num3 + 20

# магические методы на самом деле не магические ,они вызываются в определенный момент

#  with - менеджер  контекста используется с методами у которых есть два магическихметода enter и exit








# MULTIPLE INHERITANCE





# class Builder:
#     def build(self):
#         print('Build')


# class Doctor:
#     def help(self):
#         print('Help')



# class Programmer:
#     def coding(self):
#         print('Python best language!')



# class People(Builder,Doctor):
#     pass



# jack = People()
# jack.build()


# в множественном наследовании методы не предопределяются 




# Diamond Inheritance - методы предопределяются  




class HomoSapiens:
    def cook(self):
        print('Homo sapiens Cook!')

class Father(HomoSapiens):
    def drive(self):
        print('Drive')

class Mother(HomoSapiens):
    def cook(self):
        print('Cooking!')

class Son(Father,Mother):
    def love(self):
        print('Love parrents')

jack = Son()
jack.drive()   
jack.cook()                
jack.love()                             





# миксин - это классы у которых нет данных

# миксины - множественное наследование

class Mixin:

    def build(self):
        print('Build program')

class Interpeter:

    def start(self):
        print('Started')

class Programming:
    def coding(self):
        print('Programmer write code')

class Designer:

    def desigh(self):
        print('Design program!')


class Project(Designer,Programming,Interpeter,Mixin):
    print("Hello")

    
