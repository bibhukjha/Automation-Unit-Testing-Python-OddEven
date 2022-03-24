import unittest

def biggestNumber(x,y):
    if x>y:
        print("Biggest number")
    else:
        print("Smallest number")

    def test_case_biggestNumber(self):
        x=99
        y=88
        result=biggestNumber(x,y)
        self.assertTrue(result)
if __name__ == '__main__':
    unittest.main()
