# Возьмите class Rectangle. Напишите к нему тесты.
# 2-5 тестов на задачу в трёх вариантах: doctest, unittest, pytest.



class Rectangle:
    """Calculating the perimeter and area of rectangles"""

    def __init__(self, width, length):
        """Added the name parameter."""
        self.width = width
        self.length = length

    def __str__(self):
        """printout for user"""
        return f"Прямоугольник: Ширина{self.width}, Длинна {self.length}, Периметр {self.perimetr()}, Площадь {self.area()}"

    def __repr__(self):
        """printout for programmer"""
        return f"Прямоугольник: Ширина{self.width}, Длинна {self.length}, Периметр {self.perimetr()}, Площадь {self.area()}"

    def area(self):
        """counts the area"""
        return self.width * self.length

    def perimetr(self):
        """counts the perimetr
        >>> rectangle_a = Rectangle(2, 3)
        >>> print(rectangle_a.perimetr())
        10

        """
        return 2 * (self.width + self.length)

    def __add__(self, other):
        """rectangle addition operation"""
        summary_perimetr = self.perimetr() + other.perimetr()
        width_rectangle_c = self.width
        length_rectangle_c = summary_perimetr / 2 - width_rectangle_c
        return Rectangle(width_rectangle_c, length_rectangle_c)

    def __sub__(self, other):
        """rectangle subtraction operation"""
        summary_perimetr = abs(self.perimetr() - other.perimetr())
        width_rectangle_c = min(self.width, other.width, self.length, other.length)
        length_rectangle_c = summary_perimetr / 2 - width_rectangle_c
        return Rectangle(width_rectangle_c, length_rectangle_c)

    def __eq__(self, other):
        """comparison of rectangles
        >>> rectangle_a = Rectangle(2, 3)
        >>> rectangle_b = Rectangle(5, 10)
        >>> print(rectangle_a == rectangle_b)
        False
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """comparison of rectangles"""
        return self.area() != other.area()

    def __lt__(self, other):
        """comparison of rectangles"""
        return self.area() < other.area()

    def __le__(self, other):
        """comparison of rectangles"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """comparison of rectangles"""
        return self.area() > other.area()

    def __qe__(self, other):
        """comparison of rectangles"""
        return self.area() >= other.area()



if __name__ == '__main__':
    import doctest
    doctest.testmod()