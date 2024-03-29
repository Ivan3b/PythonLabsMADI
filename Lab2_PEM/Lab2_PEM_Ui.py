# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lab2_PEM.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(892, 560)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(500, 500, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.AddFileButton = QtWidgets.QPushButton(Dialog)
        self.AddFileButton.setGeometry(QtCore.QRect(40, 500, 93, 28))
        self.AddFileButton.setObjectName("AddFileButton")
        self.ChangeLocationButton = QtWidgets.QPushButton(Dialog)
        self.ChangeLocationButton.setGeometry(QtCore.QRect(150, 500, 93, 28))
        self.ChangeLocationButton.setObjectName("ChangeLocationButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 80, 811, 401))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(32, 30, 811, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.AddFileButton.setText(_translate("Dialog", "Add file"))
        self.ChangeLocationButton.setText(_translate("Dialog", "Change loc"))

class MyDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.AddFileButton.clicked.connect(self.open_dialog)  # Подключаем обработчик события к кнопке

    def open_dialog(self):
        # Открываем диалоговое окно для выбора файла
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Text files (*.txt)")
        file_dialog.setViewMode(QtWidgets.QFileDialog.List)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file_name in selected_files:
                print("Выбран файл:", file_name)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
