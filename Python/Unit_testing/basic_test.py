import unittest

def random_function():
    return True

class MyTest(unittest.TestCase):
    def test_function(self):
        self.assertTrue(random_function())


unittest.main()