import matplotlib.pyplot as plt 
import numpy as np
import re
import sys



class Plot:
    def __init__(self, exp, minVal, maxVal):
        self.expression = self.validateExpresion(exp)
        self.minValue = self.validateInteger(minVal)
        self.maxValue = self.validateInteger(maxVal)
        self.validateMaxMinValues()
        self.plotFunction()
    
    def validateExpresion(self, expression):
        expression.replace(' ', '')
        if expression == "":
            raise ValueError("Error: Empty Function")
        
        toMatch = "(-)?((\d+[\*+-\/])?[xX](\^\d+)?([+-]\d([\*\/][xX](\^\d+)?)?)*)*$"
        matched = re.match(toMatch, expression)
        
        if not matched:
            raise ValueError("Invalid Expression")
        
        expression = expression.replace('^', '**').replace('X', 'x')
        return expression
    
    def validateInteger(self, strNum):
        try:
            num = int(strNum)
            return num
        except:
            raise TypeError("Error: Not integer")
    
    def validateMaxMinValues(self):
        if self.minValue >= self.maxValue:
            raise ValueError("Maximum must be greater than Minimum")
    
    def F(self, x):
        val = eval(self.expression)
        return val
        
        
    def generateFunction(self):
        xList = []
        yList = []
        for i in range(self.minValue, self.maxValue):
            xList.append(i)
            yList.append(self.F(i))
        
        return xList, yList
        
    def plotFunction(self):
        xList, yList = self.generateFunction()
        plt.plot(xList, yList)
        #plt.title("F(X) = ", self.expression)
        plt.xlabel("X")
        plt.ylabel("F(X)")
        plt.style.use("seaborn-whitegrid")
        plt.show()


# fun = input("Enter the input equation: ")
# mn= int(input("Enter min val: "))
# mx = int(input("Enter max val: "))


# def f(x):
#     val= (eval(fun.replace('^', '**'))); 
#     return val
# x= []
# y = []
# for i in range(mn, mx):
#     x.append(i)
#     y.append(f(i))
    
# plt.plot(x, y);
# plt.show();


