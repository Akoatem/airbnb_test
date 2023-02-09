import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    
  def setUp(self):
      
      print("SETUP CALL...")
      
      #Arrange
      self.emp_1 = Employee("Ako", "Atem", 3400)
      self.emp_2 = Employee("Akon", "Atm",6000)
        
  def tearDown(self):
      print("TEARDOWN CALL...")
    
  def test_email(self):
      print("test_email")
     # emp_1 = Employee("Ako", "Atem", 3400)
     # emp_2 = Employee("Akon", "Atm",6000)
      
      self.assertEqual(self.emp_1.email, 'Ako.Atem@gmail.com')
      self.assertEqual(self.emp_2.email, 'Akon.Atm@gmail.com')
      
      # change email address
      
      self.emp_1.first = 'Ben'
      self.emp_2.first = 'Sam'
      
      self.assertEqual(self.emp_1.email, 'Ben.Atem@gmail.com')
      self.assertEqual(self.emp_2.email, 'Sam.Atm@gmail.com')
 
 
  def test_full_name(self):
      print("test_full_name")
      #emp_1 = Employee("Ako", "Atem", 3400)
      #emp_2 = Employee("Akon", "Atm",6000)
      
      self.assertEqual(self.emp_1.full_name, 'Ako Atem')
      self.assertEqual(self.emp_2.full_name, 'Akon Atm')
      
      #change names
      
      self.emp_1.first = 'Ben'
      self.emp_2.first = 'Sam'
      
      self.assertEqual(self.emp_1.full_name, 'Ben Atem')
      self.assertEqual(self.emp_2.full_name, 'Sam Atm')
      
  def test_apply_raise(self):
      print("test_apply_raise")
      #emp_1 = Employee("Ako", "Atem", 3400)
      #emp_2 = Employee("Akon", "Atm",6000)
      
      #Act 
      self.emp_1.apply_raise()
      self.emp_2.apply_raise()
      
      #Assert
      self.assertEqual(self.emp_1.pay, 3570)
      self.assertEqual(self.emp_2.pay, 6300)
        
    

if __name__ == "__main__":
    unittest.main()





    unittest.main()