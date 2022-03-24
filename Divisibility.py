import unittest
def divisibilityCheck7(x):
    if x%7 == 0:
        return True
    else:
        return False
class CheckDivisibility7(unittest.TestCase):
    def testCasedivisible(self):
        x =14
        result = CheckDivisibility7(x)
        self.assertTrue(result)





if __name__ == "__main__":
    unittest.main()