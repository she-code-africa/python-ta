
import unittest

from src import app

class Test(unittest.TestCase):
    # def test_str_uppercase(self):
    #     """
    #     Test the string for uppercase
    #     """
    #     output = "foo".upper()
    #     expected = "FOO"
    #     self.assertEqual(output, expected)

    def test_case0(self):
        """
        Testcase 0
        """
        input = 2
        output = app.solution(input)
        self.assertEqual(output, True)

    def test_case1(self):
        """
        Testcase 1
        """
        input = 24
        output = app.solution(input)
        self.assertEqual(output, False)

    def test_case2(self):
        """
        Testcase 2
        """
        input = 37
        output = app.solution(input)
        self.assertEqual(output, True)


    def test_case3(self):
        """
        Testcase 3
        """
        input = 73
        output = app.solution(input)
        self.assertEqual(output, True)

    def test_case4(self):
        """
        Testcase 4
        """
        input = 56
        output = app.solution(input)
        self.assertEqual(output, True)

    def test_case5(self):
        "Testcase 5"
        input = 97
        output = app.solution(input)
        self.assertEqual(output, False)


if __name__ == "__main__":
    unittest.main()
