

import unittest

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
      raise ValueError("it cant divide by zero")
    return a / b


class TestCalc(unittest.TestCase):
    
    # def setUp(self):
       
    
    def test_add(self):
        result = add(20, 10)  
        self.assertEqual(result, 30)
    
    def test_substract(self):
        result = substract(15, 5)
        self.assertEqual(result, 10)
        
    def test_multiply(self):
        result = multiply(4, 4)
        self.assertEqual(result, 16)
    
    def test_divide(self):
        result = divide(20, 4)
        self.assertEqual(result, 5)
        """ using the contact manager to raise the error"""
       # with self.assertRaises(ValueError):
       #calc.divide(10, 0)
        
            
            
            
    
if __name__ == "__main__":
    unittest.main()