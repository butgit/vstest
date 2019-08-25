import unittest
from PythonApplication import my_var
class Test_test1(unittest.TestCase):
    def test_A(self):
       self.assertEqual('CODE Magazine', my_var)
if __name__ == '__main__':
    unittest.main()