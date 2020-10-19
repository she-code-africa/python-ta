import unittest
import app

testcase_input_folder = "./testcase/input/"
testcase_output_folder = "./testcase/output/"


def get_testcase_file(file):
    if "input" in file:
        return testcase_input_folder + str(file)
    else:
        return testcase_output_folder + str(file)


def get_testcase_data(fd):
    f = open(get_testcase_file(fd), "r+")
    out = f.read()
    f.close()

    return out


class TestAppSolution(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_testcase_0(self):
        n = get_testcase_data("input0.txt")
        output = get_testcase_data("output0.txt")

        solution_output = app.solution(int(n))

        self.assertEqual(str(solution_output), str(output))


if __name__ == "__main__":
    unittest.main()
