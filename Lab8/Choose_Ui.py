# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Choose.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QDialog, QVBoxLayout, QTableWidgetItem, QCheckBox, QMessageBox
import sys, csv
import Table_Ui


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(728, 692)
        self.ChoosingItems_table = QtWidgets.QTableWidget(Form)
        self.ChoosingItems_table.setGeometry(QtCore.QRect(20, 20, 511, 651))
        self.ChoosingItems_table.setAccessibleName("")
        self.ChoosingItems_table.setRowCount(0)
        self.ChoosingItems_table.setColumnCount(4)
        self.ChoosingItems_table.setObjectName("ChoosingItems_table")
        item = QtWidgets.QTableWidgetItem()
        self.ChoosingItems_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ChoosingItems_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ChoosingItems_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ChoosingItems_table.setHorizontalHeaderItem(3, item)
        self.DeleteButton = QtWidgets.QPushButton(Form)
        self.DeleteButton.setGeometry(QtCore.QRect(580, 150, 121, 28))
        self.DeleteButton.setObjectName("DeleteButton")
        self.ChangeButton = QtWidgets.QPushButton(Form)
        self.ChangeButton.setGeometry(QtCore.QRect(580, 210, 121, 28))
        self.ChangeButton.setObjectName("ChangeButton")
        self.PutInBpButton = QtWidgets.QPushButton(Form)
        self.PutInBpButton.setGeometry(QtCore.QRect(580, 270, 121, 28))
        self.PutInBpButton.setObjectName("PutInBpButton")
        self.BackButton = QtWidgets.QPushButton(Form)
        self.BackButton.setGeometry(QtCore.QRect(590, 640, 93, 28))
        self.BackButton.setObjectName("Back")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.loadDataFromFile()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.ChoosingItems_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.ChoosingItems_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Weight"))
        item = self.ChoosingItems_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Cost"))
        item = self.ChoosingItems_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Choose"))
        self.DeleteButton.setText(_translate("Form", "Delete"))
        self.ChangeButton.setText(_translate("Form", "Change"))
        self.PutInBpButton.setText(_translate("Form", "Put into backpack"))
        self.BackButton.setText(_translate("Form", "BackButton"))
    
    def save_table_data_to_csv(self):
    # Открываем файл для записи
        with open(f"C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\First_year\\Lab8\\items", 'w', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file, delimiter='\t')
            
            # Получаем заголовки столбцов таблицы
            headers = [self.ChoosingItems_table.horizontalHeaderItem(i).text() for i in range(self.ChoosingItems_table.columnCount() - 1)]
            # Записываем заголовки в первую строку CSV файла
            writer.writerow(headers)
            
            # Записываем данные таблицы
            for row in range(self.ChoosingItems_table.rowCount()):
                row_data = [self.ChoosingItems_table.item(row, col).text() if self.ChoosingItems_table.item(row, col) else '' for col in range(self.ChoosingItems_table.columnCount())]
                writer.writerow(row_data)

    def close_window(self):
        self.table = Table_Ui.MyDialog()
        self.table.open()
        self.close()

    def read_data_from_file(self):
        try:
            with open(f"C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\First_year\\Lab8\\items", 'r', encoding='UTF-8') as file:
                lines = file.readlines()[1:]  # Пропускаем заголовок
                data = [line.strip().split() for line in lines]
            return data
        except FileNotFoundError:
            print("Файл не найден.")
            return []

    def write_data_to_file(self, data):
        try:
            with open(f"C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\First_year\\Lab8\\items", 'w', encoding='UTF-8') as file:
                file.write("Name\tWeight\tCoast\n")  # Заголовок
                for line in data:
                    file.write("\t".join(line) + "\n")
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")

    def loadDataFromFile(self):
        data = self.read_data_from_file()
        self.ChoosingItems_table.setRowCount(len(data))
        self.ChoosingItems_table.setColumnCount(4)  # Устанавливаем количество колонок

        for row_num, row_data in enumerate(data):
            for col_num, item in enumerate(row_data):
                self.ChoosingItems_table.setItem(row_num, col_num, QTableWidgetItem(item))

            # Добавляем флажок в четвертую колонку
            checkbox_item = QTableWidgetItem()
            checkbox_item.setFlags(checkbox_item.flags() | Qt.ItemIsUserCheckable)
            checkbox_item.setCheckState(Qt.Unchecked)
            self.ChoosingItems_table.setItem(row_num, 3, checkbox_item)




    def delete_selected(self):
        data = self.read_data_from_file()
        rows_to_delete = []

        for row in range(self.ChoosingItems_table.rowCount() - 1, -1, -1):
            item = self.ChoosingItems_table.item(row, 3)
            if item.checkState() == Qt.Checked:
                rows_to_delete.append(row)

        for row in rows_to_delete:
            self.ChoosingItems_table.removeRow(row)
            del data[row]

        self.write_data_to_file(data)

    def save_checked_rows_to_file(self):
        # Открываем файл для записи
        with open(f"C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\First_year\\Lab8\\Backpack", 'w', newline='', encoding='utf-8') as file:
            file.write("Name\tWeight\tCoast\n")
            writer = csv.writer(file, delimiter='\t')
            
            # Проходимся по строкам таблицы
            for row in range(self.ChoosingItems_table.rowCount()):
                # Проверяем, установлен ли чекбокс в четвертой колонке
                checkbox_item = self.ChoosingItems_table.item(row, 3)
                if checkbox_item.checkState() == Qt.Checked:
                    # Получаем данные из первых трех колонок
                    row_data = [
                        self.ChoosingItems_table.item(row, col).text() if self.ChoosingItems_table.item(row, col) else ''
                        for col in range(3)
                    ]
                    # Записываем данные в файл
                    writer.writerow(row_data)
                
    
class MyDialog(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BackButton.clicked.connect(self.close_window)
        self.DeleteButton.clicked.connect(self.delete_selected)
        self.ChangeButton.clicked.connect(self.save_table_data_to_csv)
        self.PutInBpButton.clicked.connect(self.save_checked_rows_to_file)
