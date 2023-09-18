from areas import circle_area, triangle_area
import unittest


class TestAreas(unittest.TestCase):
    def setUp(self):
        pass

    def test_circle(self):
        self.assertEqual(circle_area(1), 3.14)
        self.assertEqual(circle_area(5), 78.5)
        # self.assertEqual(circle_area(5), 3.14)
        # self.assertEqual(circle_area('1'), 3.14)

    def test_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6)
        # self.assertEqual(triangle_area('3', 4, 8), 6)
        # self.assertEqual(triangle_area(1, 1, 1), 6)
        # self.assertEqual(triangle_area(10, 15, 20), 6)


if __name__ == "__main__":
    unittest.main()
