import unittest

class SimplisticTest(unittest.TestCase):

    def test(self):
        print('Basic Unit Test case')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
