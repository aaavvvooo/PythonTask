from Figures import Triangle, Circle


def circle_area(radius):
    return Circle(radius).area()


def triangle_area(a, b, c):
    return Triangle(a, b, c).area()
