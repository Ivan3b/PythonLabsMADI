# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QTableWidgetItem
import Warning_Ui
import Table_Ui


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(426, 396)
        self.Back_button = QtWidgets.QPushButton(Dialog)
        self.Back_button.setGeometry(QtCore.QRect(20, 330, 93, 28))
        self.Back_button.setObjectName("Back_button")
        self.Add_button = QtWidgets.QPushButton(Dialog)
        self.Add_button.setGeometry(QtCore.QRect(290, 330, 93, 28))
        self.Add_button.setObjectName("Add_button")
        self.Name_label = QtWidgets.QLabel(Dialog)
        self.Name_label.setGeometry(QtCore.QRect(80, 40, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Name_label.setFont(font)
        self.Name_label.setTextFormat(QtCore.Qt.AutoText)
        self.Name_label.setObjectName("Name_label")
        self.Name_line = QtWidgets.QLineEdit(Dialog)
        self.Name_line.setGeometry(QtCore.QRect(160, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Name_line.setFont(font)
        self.Name_line.setObjectName("Name_line")
        self.Weight_line = QtWidgets.QLineEdit(Dialog)
        self.Weight_line.setGeometry(QtCore.QRect(160, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Weight_line.setFont(font)
        self.Weight_line.setObjectName("Weigth_line")
        self.weight_label = QtWidgets.QLabel(Dialog)
        self.weight_label.setGeometry(QtCore.QRect(80, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.weight_label.setFont(font)
        self.weight_label.setTextFormat(QtCore.Qt.AutoText)
        self.weight_label.setObjectName("weight_label")
        self.Cost_line = QtWidgets.QLineEdit(Dialog)
        self.Cost_line.setGeometry(QtCore.QRect(160, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cost_line.setFont(font)
        self.Cost_line.setObjectName("Cost_line")
        self.Cost_label = QtWidgets.QLabel(Dialog)
        self.Cost_label.setGeometry(QtCore.QRect(80, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cost_label.setFont(font)
        self.Cost_label.setTextFormat(QtCore.Qt.AutoText)
        self.Cost_label.setObjectName("Cost_label")
        self.ErrorLable = QtWidgets.QLabel(Dialog)
        self.ErrorLable.setGeometry(QtCore.QRect(110, 270, 201, 20))
        self.ErrorLable.setText("")
        self.ErrorLable.setObjectName("ErrorLable")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Back_button.setText(_translate("Dialog", "Back"))
        self.Add_button.setText(_translate("Dialog", "Add"))
        self.Name_label.setText(_translate("Dialog", "Name:"))
        self.weight_label.setText(_translate("Dialog", "Weight:"))
        self.Cost_label.setText(_translate("Dialog", "Cost:"))

    def close_window(self):
        self.table = Table_Ui.MyDialog()
        # Получаем текст из строковых полей
        text1 = self.Name_line.text()
        text2 = self.Weight_line.text()
        text3 = self.Cost_line.text()

        # Если хотя бы одно поле не пустое, показываем предупреждение
        if text1 or text2 or text3:
            self.warning = Warning_Ui.MyDialog()
            self.warning.show()
            self.warning.Yes_button.clicked.connect(self.closing)
        else:
            self.table.show()
            self.close()
    def closing(self):
        self.table.show()
        self.close()

    def validateInput(self):
        # Проверяем, соответствует ли введенное значение типу float
        weight_text = self.Weight_line.text()
        cost_text = self.Cost_line.text()
        try:
            float(weight_text)
            # Если введенное значение является float, восстанавливаем стандартный стиль
            self.Weight_line.setStyleSheet("")
            self.ErrorLable.setText("Weight and cost must be a number")
            f1 = 0
        except ValueError:
            # Если введенное значение не является float, устанавливаем красный фон
            self.Weight_line.setStyleSheet("background-color: #FFBABA;")
            f1 = 1
        try:
            float(cost_text)
            # Если введенное значение является float, восстанавливаем стандартный стиль
            self.Cost_line.setStyleSheet("")
            f2 = 0
        except ValueError:
            # Если введенное значение не является float, устанавливаем красный фон
            self.Cost_line.setStyleSheet("background-color: #FFBABA;")
            self.ErrorLable.setText("Weight and cost must be a number")
            f2 = 1
        if f1 == 0 and f2 == 0 :
            self.ErrorLable.setText("New item added in list")
            self.writeToFile()
                                    
    def writeToFile(self):
        # Получаем текст из каждого line edit
        self.tbl = Table_Ui.MyDialog()
        text1 = self.Name_line.text()
        text2 = self.Weight_line.text()
        text3 = self.Cost_line.text()
        # Открываем файл для добавления данных в конец файла
        with open("C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\First_year\\Lab8\\items", 'a') as file:
            # Записываем данные из line edit в файл, разделяя их табуляцией
            file.write(f"{text1}\t{text2}\t{text3}\n")

        # Очищаем line edit после записи
        self.Name_line.clear()
        self.Weight_line.clear()
        self.Cost_line.clear()
      
    
class MyDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Back_button.clicked.connect(self.close_window)
        self.Add_button.clicked.connect(self.validateInput)

