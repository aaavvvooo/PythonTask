from abc import ABC, abstractmethod
from math import sqrt


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        try:
            if not isinstance(self.radius, (int, float)):
                raise ValueError("wrong type of arguments")
            return 3.14 * self.radius ** 2
        except Exception as e:
            print(f"Error: {e}")


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        try:
            if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float))\
                    or not isinstance(self.c, (int, float)):
                raise ValueError("Wrong argument type")
            side_list = sorted([self.a, self.b, self.c])
            if side_list[2] >= side_list[1] + side_list[0]:
                raise ValueError("Invalid arguments: It's an impossible triangle")
            if side_list[2] ** 2 == side_list[1] ** 2 + side_list[0] ** 2:
                return (side_list[1] * side_list[0]) / 2
            else:
                semi_p = (self.a + self.b + self.c) / 2
                return sqrt(semi_p * (semi_p - self.a) * (semi_p - self.b) * (semi_p - self.c))
        except Exception as e:
            print(f"Error: {e}")
