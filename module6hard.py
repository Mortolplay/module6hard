class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = list(sides)
        self.filled = True
    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True:
            self.__color = [r, g, b]
    def __is_valid_sides(self, *args):
        for i in self.__sides:
            if len(self.__sides) == self.sides_count and i > 0 and type(i) == int:
                return True
            else:
                return False
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        a = []
        for i in new_sides:
            a.append(new_sides)
        if len(a) == self.sides_count:
            self.__sides = new_sides
class Circle(Figure):
    sides_count = 1
    __radius = 0
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
    def __radius(self):
        self.__radius = self.__len__() / (2*pi)
        return self.__radius
    def get_square(self):
        return 2*pi*self.__radius**2
class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        return sqrt((self.__len__()) / 2 * ((self.__len__()) / 2 - (self.__sides[0]))*((self.__len__()) / 2 - (self.__sides[1]))*((self.__len__()) / 2 - (self.__sides[2])))
class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__(color, *sides * 12)
        if len(sides) == 1:
            sides = [1]
    def neum(self, *sides):
        if len(sides) == 1:
            super().set_sides(*sides * 12)
    #def um(self):
    #    if len(self.__sides) == 1:
    #        b = []
    #        for i in range(sides_count):
    #            b.append(self.__sides[0])
    #        self.__sides = b
    #    else:
    #        self.__sides = [1*self.sides_count]
    #    return self.__sides
    def get_volume(self):
        return self.get_sides()[0]**3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

