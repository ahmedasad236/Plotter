import unittest
import unittest
import Validation as valid

class testUnit(unittest.TestCase):

#-------------------------------------------------------------------------------------------------------------------------------------    
    def testValidateExpresion(self):
        self.assertRaises(ValueError, valid.validateExpresion, "")
        self.assertRaises(ValueError, valid.validateExpresion, "x+1-")
        self.assertRaises(ValueError, valid.validateExpresion, "-1+2/x^")
        self.assertEqual("1+2*x-3*x**2+4/x**3", valid.validateExpresion("1+2*x-3*X^2 + 4 / X^3"))
#-------------------------------------------------------------------------------------------------------------------------------------
    def testValidateInteger(self):
        self.assertRaises(ValueError, valid.validateInteger, "")
        self.assertRaises(ValueError, valid.validateInteger, "xassa")
        self.assertRaises(ValueError, valid.validateInteger, "123x")
#-------------------------------------------------------------------------------------------------------------------------------------    
    def testValidateMaxMinValues(self):
        self.assertRaises(ValueError, valid.validateMaxMinValues,-10, -20)
        self.assertRaises(ValueError, valid.validateMaxMinValues, 10, 0)
#-------------------------------------------------------------------------------------------------------------------------------------        
    def testValidateDivisionByZero(self):
        self.assertAlmostEqual(False, valid.validateDivisionByZero("1/x", -5, 10), "Should return False")        
        self.assertAlmostEqual(False, valid.validateDivisionByZero("1/x^4", 0, 10), "Should return False")        
        self.assertAlmostEqual(False, valid.validateDivisionByZero("x^2+3*x-10/x^3", -10, 10), "Should return False")        
        self.assertAlmostEqual(True, valid.validateDivisionByZero("1/x", 1, 10), "Should return True")        
        self.assertAlmostEqual(True, valid.validateDivisionByZero("1+x-10*x^2", -100, 100), "Should return True")        


if __name__ == "__main__":
    testObject = testUnit()