
import unittest

from src import app

class Test(unittest.TestCase):
    def test_str_uppercase(self):
        """
        Test the string for uppercase
        """
        output = "foo".upper()
        expected = "FOO"
        self.assertEqual(output, expected)

    def test_case0(self):
        """
        Testcase 0
        """
        input = "wow"
        output = app.solution(input)
        self.assertEqual(output, True)

    def test_case1(self):
        """
        Testcase 1
        """
        input = "random string"
        output = app.solution(input)
        self.assertEqual(output, False)

    def test_case2(self):
        """
        Testcase 2
        """
        input = "wassamassaw"
        output = app.solution(input)
        self.assertEqual(output, True)


    def test_case3(self):
        """
        Testcase 3
        """
        input = "satanoscillatemymetallicsonatas"
        output = app.solution(input)
        self.assertEqual(output, True)

    def test_case4(self):
        """
        Testcase 4
        """
        input = "in girum imus nocte et consumimur igni"
        output = app.solution(input)
        self.assertEqual(output, True)

    def test_case5(self):
        "Testcase 5"
        input = "No lemoned, no melon"
        output = app.solution(input)
        self.assertEqual(output, False)


if __name__ == "__main__":
    unittest.main()
