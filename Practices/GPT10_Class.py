class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        perimeter = 2*(self.width + self.length)
        print(perimeter)

    def area(self):
        area = self.width * self.length
        print(area)

    def __str__(self):
        """Return a string representation of the rectangle."""
        print(f"Rectangle(length: {self.length}, width: {self.width})")


rectangle = Rectangle(10, 15)
rectangle.perimeter()
rectangle.area()
rectangle.__str__()


# Q1-5 6
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    def get_count(self):
        print(Person.count)


p1 = Person('john')
p2 = Person('HH')
p2.get_count()

# Q 6
class Person:
    def __init__(self, age: int):
        self.age = age


class Employee(Person):
    def __init__(self, age: int, salary: float):
        super().__init__(age)
        self.salary = salary

    def display_salary(self):
        print(f'Salary: {self.salary}')


# Creating an Employee object
e1 = Employee(29, 50000)
e1.display_salary()

# Q7


class Person:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int):
        age = 2024 - birth_year
        return cls(name, age)

    def display(self):
        print(f'{self.name} is {self.age}')


p1 = Person.from_birth_year('Ali', 1988)
p1.display()

# Q8 percentage increase in salary
class Employee:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def salary_increase(self, percentage: int):
        self.percentage = percentage
        new_salary = (self.salary * self.percentage/100) + self.salary
        print(f'You new salary is {new_salary}')


employee_1 = Employee('ali', 22, 3300)
employee_1.salary_increase(4)

# Exercise
class Food:
    def __init__(self, calorie, color):
        self.calorie = calorie
        self.color = color

    def show(self):
        print(f'this {self.color} food has {self.calorie} calories')


class FastFood(Food):
    def __init__(self, calorie, color, time):
        super().__init__(calorie, color)
        self.time = time


class SonatiFood(Food):
    def __init__(self, calorie, color, portion: int):
        super().__init__(calorie, color)
        self.portion = portion

    def double_portion(self):
        new_portion = self.portion * 2
        print(new_portion)


kebab = SonatiFood(1000, "kebabi", 3)
kebab.double_portion()
kebab.show()

# Exercise
class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return Point(self.x * p.x, self.y * p.y)

    def __str__(self):
        return '(' + str(self.x) + "," + str(self.y) + ')'

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, point2):
        return self.length() > point2.length()

    def __ge__(self, point2):
        return self.length() >= point2.length()

    def __lt__(self, point2):
        return self.length() < point2.length()

    def __le__(self, point2):
        return self.length() <= point2.length()

    def __eq__(self, point2):
        return self.length() == point2.length()


p1 = Point(1, 3)
p2 = Point(10, 20)
print(p1 > p2)
print(p1 < p2)
print(p1 == p2)
print(p1 >= p2)
