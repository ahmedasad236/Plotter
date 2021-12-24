import matplotlib.pyplot as plt 
import numpy as np
from Validation import Validation
import re
import sys

class Plot:
    def __init__(self, exp, minVal, maxVal):
        self.validate = Validation()
        self.expression = self.validate.validateExpresion(exp)
        print(self.expression)
        self.minValue = self.validate.validateInteger(minVal)
        self.maxValue = self.validate.validateInteger(maxVal)
        self.validate.validateMaxMinValues(self.minValue, self.maxValue)
#-------------------------------------------------------------------------------------    
    def F(self, x):
        val = eval(self.expression)
        return val
#-------------------------------------------------------------------------------------
    def generateFunction(self):
        xList = []
        yList = []
        testZeroDiv = self.validate.validateDivisionByZero(self.expression, self.minValue)
        for i in range(self.minValue, self.maxValue):
            xList.append(i)
            if testZeroDiv == False and i == 0: #put the y-value with infinity if(x is a denominator and x == 0)
                yList.append(float('inf'))
            else:    
                yList.append(self.F(i))
        
        return xList, yList
#-------------------------------------------------------------------------------------
    def plotFunction(self):
        xList, yList = self.generateFunction()
        plt.plot(xList, yList, color="red", linewidth=1.5, label=self.expression)
        plt.xlabel("X")
        plt.ylabel("F(X)")
        plt.style.use("seaborn-dark")
        plt.show()
#-------------------------------------------------------------------------------------


