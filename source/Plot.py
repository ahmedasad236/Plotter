import matplotlib.pyplot as plt 
import numpy as np
import Validation as valid
import re
import sys

class Plot:
    def __init__(self, exp, minVal, maxVal):
        self.expression = valid.validateExpresion(exp)
        print(self.expression)
        self.minValue = valid.validateInteger(minVal)
        self.maxValue = valid.validateInteger(maxVal)
        valid.validateMaxMinValues(self.minValue, self.maxValue)
#-------------------------------------------------------------------------------------    
    def F(self, x):
        val = eval(self.expression)
        return val
#-------------------------------------------------------------------------------------
    def generateFunction(self):
        xList = []
        yList = []
        testZeroDiv = valid.validateDivisionByZero(self.expression, self.minValue, self.maxValue)
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


