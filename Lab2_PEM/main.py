import sys
from Lab2_PEM_Ui import MyDialog
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
