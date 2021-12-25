import re
import sys


    
def validateExpresion(expression):
    expression = expression.replace(" ", "")
    if expression == "":
        raise ValueError("Empty Function")
    
    toMatch = "(-)?(\d+$)|((\d+[+-])?(\d+[\*\/])?[xX](\^\d+)?([+-]\d+([\*\/][xX](\^\d+)?)?)*)*$"
    matched = re.match(toMatch, expression)
    if not matched:
        raise ValueError("Invalid Expression")
    
    expression = expression.replace('^', '**').replace('X', 'x')
    
    return expression
#-------------------------------------------------------------------------------------
def validateInteger(strNum):
    try:
        num = int(strNum)
        return num
    except:
        raise ValueError("Not a range")
#-------------------------------------------------------------------------------------    
def validateMaxMinValues(minValue, maxValue):
    if minValue >= maxValue:
        raise ValueError("Maximum must be greater than Minimum")
#-------------------------------------------------------------------------------------
def validateDivisionByZero(expression, minValue, maxValue):
    if expression.find('/X') != -1 or expression.find('/x') != -1 and minValue <= 0 and maxValue >= 0:
        return False
    return True


