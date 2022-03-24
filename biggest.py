import unittest
def check(a,b):
    if a >= b:
        return "The number is greater"
    else:
        return "The number is smaller"

class BiggerNo(unittest.TestCase):

    def test_case_check(self):
        a = 40
        b = 30
        result = check(a,b)
        self.assertEqual("The number is greater",result)
    def test_case_check1(self):
        a = 20
        b = 30
        result = check(a,b)
        self.assertEqual("The number is smaller",result)


if __name__ == "__main__":
    unittest.main()