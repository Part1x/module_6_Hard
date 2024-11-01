import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.filled = True
        self.__sides = sides

    def __len__(self):
        return sum(self.__sides)

    def __is_valid_color(self, r, g, b):
        if not all(isinstance(i, int) for i in [r, g, b]):
            return False
        if not all(0 <= i <= 255 for i in [r, g, b]):
            return False
        return True

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != len(self.__sides):
            return False
        if not all(isinstance(i, int) and i > 0 for i in new_sides):
            return False
        return True

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.sides_count == len(new_sides):
            self.__sides = list(new_sides)
            self.sides_count = len(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return self.get_sides()[0] ** 2 / (4 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        p = len(self) / 2
        return (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.set_sides(*sides * 12)
        else:
            self.set_sides(*((1,) * 12))


    def get_volume(self):
        return self.get_sides()[0] ** 3

    def __len__(self):
        return 12 * self.get_sides()[0]



circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
