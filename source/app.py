from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QWidget, QDialog
from Plot import Plot
from ShowError import showErrorMessage
import sys

class UI(QDialog ):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('plotter.ui', self)        
        self.plotButton.clicked.connect(self.sketch)
#-------------------------------------------------------------------------------------    
    def sketch(self):
        try:
            plotObj = Plot(self.expression.text(), 
                                self.minValue.text(),
                                self.maxValue.text())
            
            plotObj.plotFunction()
        
        except ValueError as err:
            err_message = err.args[0]
            showErrorMessage(self, err_message)
            self.emptyEntries()
            return
#-------------------------------------------------------------------------------------
    def emptyEntries(self):
        self.expression.setText("")
        self.minValue.setText("")
        self.maxValue.setText("") 
#-------------------------------------------------------------------------------------


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    currWindow = UI()
    currWindow.show()
    sys.exit(application.exec_())