import unittest
def divisibilityCheck7(x):
    if x%7 == 0:
        return True
    else:
        return False
class CheckDivisibility7(unittest.TestCase):
    def testCasedivisible(self):
        x =14
        result = divisibilityCheck7(x)
        self.assertTrue(result)

    def testCasedivisible1(self):
        x = 15
        result = divisibilityCheck7(x)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()