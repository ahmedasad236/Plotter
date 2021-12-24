from PyQt5.QtWidgets import QMessageBox

def showErrorMessage(UIObject, err_mess):
    QMessageBox.critical(UIObject, "Error", err_mess)