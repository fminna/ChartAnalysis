import unittest
from myapp.module1.service1 import svc1_hello


"""Testing class for module1.

"""

class TestModule1(unittest.TestCase):

    def test_print(self):
        self.assertEqual(svc1_hello(), True)


if __name__ == '__main__':
    unittest.main()
