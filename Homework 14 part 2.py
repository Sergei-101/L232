from Homework_14 import Rectangle
import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.rectangle_a = Rectangle(2, 3)
        self.rectangle_b = Rectangle(5, 10)
    def test_perimetr(self):
        self.assertEqual(10,self.rectangle_a.perimetr())
        self.assertEqual(30, self.rectangle_b.perimetr())
    def test_equality(self):
        self.assertEqual(False, self.rectangle_a == self.rectangle_b)
        self.assertEqual(False, self.rectangle_a > self.rectangle_b)
        self.assertEqual(True, self.rectangle_a < self.rectangle_b)


if __name__ == '__main__':
    unittest.main()





# print(rectangle_a.perimetr())
# print(rectangle_b.perimetr())
# rectangle_c = rectangle_a + rectangle_b
# rectangle_d = rectangle_a - rectangle_b
# print(rectangle_c.perimetr(), rectangle_c.width, rectangle_c.length)
# print(rectangle_d.perimetr(), rectangle_c.width, rectangle_c.length)
# print(rectangle_a == rectangle_b)
# print(rectangle_a != rectangle_b)
# print(rectangle_a > rectangle_b)
# print(rectangle_a < rectangle_b)
