import unittest
def check(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

class EvenOddApp(unittest.TestCase):
    def testCaseEven(self):
        x = 10
        result = check(x)
        self.assertEqual("Even", result)

    def testCaseOdd(self):
        x = 15
        result = check(x)
        self.assertEqual("Odd", result)
if __name__ == "__main__":
    unittest.main()



