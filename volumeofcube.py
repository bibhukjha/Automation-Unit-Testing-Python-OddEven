import unittest

def vol_cube(x):
    return x*x*x

class VolumeCeckTest(unittest.TestCase):
    def testCasevol(self):
        x = 5.556
        result = vol_cube(x)
        self.assertAlmostEqual(result,x*x*x)

if __name__ == "__main__":
    unittest.main()