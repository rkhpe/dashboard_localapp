import unittest

class SimplisticTest(unittest.TestCase):

    def test(self):
        print('Basic Unit Test case demo')
        print('Basic Unit 2 Test case demo')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
