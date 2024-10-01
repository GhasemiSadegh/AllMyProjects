# nums = [1, 2, 3, 4, 5]
# odd_list = []
# for num in nums:
#     if num % 2 != 0:
#         odd_list.append(num)
# print(odd_list)

# def is_even(num):
#     if num % 2 == 0:
#         return False
#     return True
#
#
# is_even(2)


# integer = 1
# string = str(integer)
# flt = float(integer)
# print(type(flt))
# print(type(string))
# data = bool
# print(type(data()))

# nums = [1, 2]
# print(type(nums))
#
# dict = {"ali": 22, "sadegh": 33}
# print(type(dict))
# tpl = (1, 2, 3, 4)
# print(type(tpl))
# x = {1, 1, 2, 3}
# print(type(x))
# print(x)

# for i in range(0, 10):
#     print(i)
#
# x = [0, 1]
# for i in x:
#     print(i+i)
#     print(x[0])
#     print(x[1])


# def name_getter(name):
#     print(f"Your name is: {name}")
#
#
# the_name = input('Name?')
# name_getter(the_name)


class Cars:
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def welcome(self):
        print(f"This is the brand: {self.brand}")


car1 = Cars("BMW", 2024)
car1.welcome()
