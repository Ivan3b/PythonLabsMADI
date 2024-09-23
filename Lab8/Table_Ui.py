from PyQt5 import QtCore, QtGui, QtWidgets
import importlib
import time
import csv


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1120, 704)
        self.Items_table = QtWidgets.QTableWidget(Dialog)
        self.Items_table.setGeometry(QtCore.QRect(30, 60, 411, 601))
        self.Items_table.setAccessibleName("")
        self.Items_table.setRowCount(0)
        self.Items_table.setColumnCount(3)
        self.Items_table.setObjectName("Items_table")
        item = QtWidgets.QTableWidgetItem()
        self.Items_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Items_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Items_table.setHorizontalHeaderItem(2, item)
        self.New_item_in_table = QtWidgets.QPushButton(Dialog)
        self.New_item_in_table.setGeometry(QtCore.QRect(450, 80, 221, 28))
        self.New_item_in_table.setObjectName("New_item_in_table")
        self.ChooseItemButton = QtWidgets.QPushButton(Dialog)
        self.ChooseItemButton.setGeometry(QtCore.QRect(450, 140, 221, 28))
        self.ChooseItemButton.setObjectName("ChooseItemButton")
        self.BackpackTable = QtWidgets.QTableWidget(Dialog)
        self.BackpackTable.setGeometry(QtCore.QRect(680, 60, 411, 601))
        self.BackpackTable.setAccessibleName("")
        self.BackpackTable.setRowCount(0)
        self.BackpackTable.setColumnCount(3)
        self.BackpackTable.setObjectName("BackpackTable")
        item = QtWidgets.QTableWidgetItem()
        self.BackpackTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.BackpackTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.BackpackTable.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 20, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(830, 20, 55, 16))
        self.label_2.setObjectName("label_2")
        self.ChooseBackpackItemButton = QtWidgets.QPushButton(Dialog)
        self.ChooseBackpackItemButton.setGeometry(QtCore.QRect(450, 200, 221, 28))
        self.ChooseBackpackItemButton.setObjectName("ChooseBackpackItemButton")
        self.WeightLabelChange = QtWidgets.QLabel(Dialog)
        self.WeightLabelChange.setGeometry(QtCore.QRect(810, 670, 51, 19))
        self.WeightLabelChange.setText("")
        self.WeightLabelChange.setObjectName("WeightLabelChange")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(860, 670, 16, 19))
        self.label_3.setObjectName("label_3")
        self.WeeightLine = QtWidgets.QLineEdit(Dialog)
        self.WeeightLine.setGeometry(QtCore.QRect(870, 670, 41, 25))
        self.WeeightLine.setObjectName("WeeightLine")
        self.GreedyAlgorithButton = QtWidgets.QPushButton(Dialog)
        self.GreedyAlgorithButton.setGeometry(QtCore.QRect(450, 260, 221, 28))
        self.GreedyAlgorithButton.setObjectName("GreedyAlgorithButton")
        self.DynamicMethodButton = QtWidgets.QPushButton(Dialog)
        self.DynamicMethodButton.setGeometry(QtCore.QRect(450, 320, 221, 28))
        self.DynamicMethodButton.setObjectName("DynamicMethodButton")
        self.RecursiveMethodButton = QtWidgets.QPushButton(Dialog)
        self.RecursiveMethodButton.setGeometry(QtCore.QRect(450, 380, 221, 28))
        self.RecursiveMethodButton.setObjectName("RecursiveMethodButton")
        self.TGAruningtimeLabel = QtWidgets.QLabel(Dialog)
        self.TGAruningtimeLabel.setGeometry(QtCore.QRect(470, 450, 191, 16))
        self.TGAruningtimeLabel.setObjectName("TGAruningtimeLabel")
        self.DMruningtimeLabel = QtWidgets.QLabel(Dialog)
        self.DMruningtimeLabel.setGeometry(QtCore.QRect(480, 510, 171, 16))
        self.DMruningtimeLabel.setObjectName("DMruningtimeLabel")
        self.TRMruningtileLabel = QtWidgets.QLabel(Dialog)
        self.TRMruningtileLabel.setGeometry(QtCore.QRect(460, 570, 201, 16))
        self.TRMruningtileLabel.setObjectName("TRMruningtileLabel")
        self.TGAtime = QtWidgets.QLabel(Dialog)
        self.TGAtime.setGeometry(QtCore.QRect(500, 470, 131, 20))
        self.TGAtime.setText("")
        self.TGAtime.setObjectName("TGAtime")
        self.DMtime = QtWidgets.QLabel(Dialog)
        self.DMtime.setGeometry(QtCore.QRect(500, 530, 131, 20))
        self.DMtime.setText("")
        self.DMtime.setObjectName("DMtime")
        self.TRMtime = QtWidgets.QLabel(Dialog)
        self.TRMtime.setGeometry(QtCore.QRect(500, 590, 131, 20))
        self.TRMtime.setText("")
        self.TRMtime.setObjectName("TRMtime")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.Items_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.Items_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Weight"))
        item = self.Items_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Cost"))
        self.New_item_in_table.setText(_translate("Dialog", "Add new item in table"))
        self.ChooseItemButton.setText(_translate("Dialog", "Choose item"))
        item = self.BackpackTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.BackpackTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Weight"))
        item = self.BackpackTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Cost"))
        self.label.setText(_translate("Dialog", "Items"))
        self.label_2.setText(_translate("Dialog", "Backpack"))
        self.ChooseBackpackItemButton.setText(_translate("Dialog", "Choose item from backpack"))
        self.label_3.setText(_translate("Dialog", "/"))
        self.WeeightLine.setText(_translate("Dialog", "100"))
        self.GreedyAlgorithButton.setText(_translate("Dialog", "The greedy algorithm"))
        self.DynamicMethodButton.setText(_translate("Dialog", "Dynamic method"))
        self.RecursiveMethodButton.setText(_translate("Dialog", "The recursive method"))
        self.TGAruningtimeLabel.setText(_translate("Dialog", "The greed algorithm runing time: "))
        self.DMruningtimeLabel.setText(_translate("Dialog", "Dynamic method runing time: "))
        self.TRMruningtileLabel.setText(_translate("Dialog", "The recursive method runing time: "))

class MyDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect buttons to their respective slot methods
        self.New_item_in_table.clicked.connect(self.open_new_item_dialog)
        self.ChooseItemButton.clicked.connect(self.open_choose_item_dialog)
        self.ChooseBackpackItemButton.clicked.connect(self.open_choose_backpack_item_dialog)
        self.GreedyAlgorithButton.clicked.connect(self.process_files)
        self.DynamicMethodButton.clicked.connect(self.dynamic_alg)
        self.RecursiveMethodButton.clicked.connect(self.recursive)

        self.load_data_to_table()
        

    def load_data_to_table(self,file_path = 'C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\First_year\\Lab8\\items'):
        
        try:
            with open(file_path , newline='', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter='\t')
                
                # Очистите таблицу перед добавлением новых данных
                self.Items_table.setRowCount(0)
                
                for row_data in reader:
                    row_position = self.Items_table.rowCount()
                    self.Items_table.insertRow(row_position)
                    
                    for column, data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(data)
                        self.Items_table.setItem(row_position, column, item)
        
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Ошибка', f'Не удалось загрузить данные: {e}')

    def load_data_to_table_backpack(self,file_path = 'C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\First_year\\Lab8\\Backpack'):
        
        try:
            with open(file_path , newline='', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter='\t')
                
                # Очистите таблицу перед добавлением новых данных
                self.BackpackTable.setRowCount(0)
                
                for row_data in reader:
                    row_position = self.BackpackTable.rowCount()
                    self.BackpackTable.insertRow(row_position)
                    
                    for column, data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(data)
                        self.BackpackTable.setItem(row_position, column, item)
        
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Ошибка', f'Не удалось загрузить данные: {e}')

    def open_new_item_dialog(self):
        self.close()
        self.open_dialog('Add_item_Ui')
        self.load_data_to_table()
        self.open()
        

    def open_choose_item_dialog(self):
        self.close()
        self.open_dialog('Choose_Ui')
        self.load_data_to_table_backpack()
        self.open()

    def open_choose_backpack_item_dialog(self):
        self.close()
        self.open_dialog('Choose_backpack_Ui')
        self.load_data_to_table_backpack()
        self.open()

    def open_dialog(self, dialog_name):
        # Import the module dynamically based on button clicked
        try:
            module = importlib.import_module(dialog_name)
            dialog_class = getattr(module, 'MyDialog')
            dialog = dialog_class()
            dialog.exec_()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Error', str(e))
    
    def process_files(self):
        start_time = time.perf_counter()
        input_file_path = "C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\First_year\\Lab8\\items"
        output_file_path = "C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\First_year\\Lab8\\Backpack"
        max_weight = int(self.WeeightLine.text())
        with open(input_file_path, 'r') as file:
            lines = file.readlines()

        # Пропускаем заголовок
        header = lines[0]
        data = [line.strip().split('\t') for line in lines[1:]]

        # Преобразуем данные в удобный формат
        items = [(line[0], int(line[1]), int(line[2])) for line in data]

        # Динамическое программирование для решения задачи
        n = len(items)
        dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            name, weight, cost = items[i - 1]
            for w in range(max_weight + 1):
                if weight <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + cost)
                else:
                    dp[i][w] = dp[i - 1][w]

        # Восстановление лучшего набора предметов
        w = max_weight
        best_combination = []
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                name, weight, cost = items[i - 1]
                best_combination.append((name, weight, cost))
                w -= weight

        # Расчет суммы веса и цены
        total_weight = sum(item[1] for item in best_combination)
        total_cost = sum(item[2] for item in best_combination)

        # Сортировка для записи
        sorted_lines = [header] + ['\t'.join(map(str, line)) + '\n' for line in reversed(best_combination)]


        # Запись в файл
        with open(output_file_path, 'w') as file:
            file.writelines(sorted_lines)
        self.WeightLabelChange.setText(str(total_weight))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        self.TGAtime.setText(str(elapsed_time))
        self.load_data_to_table_backpack()
    
    def dynamic_alg(self):
        start_time = time.perf_counter()
        input_file_path = "C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\First_year\\Lab8\\items"
        output_file_path = "C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\First_year\\Lab8\\Backpack"
        max_weight = int(self.WeeightLine.text())
        
        try:
            with open(input_file_path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("Input file not found.")
            return

        # Пропускаем заголовок
        header = lines[0]
        data = [line.strip().split('\t') for line in lines[1:]]

        # Преобразуем данные в удобный формат
        items = [(line[0], int(line[1]), int(line[2])) for line in data]

        # Динамическое программирование для решения задачи
        n = len(items)
        dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            name, weight, cost = items[i - 1]
            for w in range(max_weight + 1):
                if weight <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + cost)
                else:
                    dp[i][w] = dp[i - 1][w]

        # Восстановление лучшего набора предметов
        w = max_weight
        best_combination = []
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                name, weight, cost = items[i - 1]
                best_combination.append((name, weight, cost))
                w -= weight

        # Расчет суммы веса и цены
        total_weight = sum(item[1] for item in best_combination)
        total_cost = sum(item[2] for item in best_combination)

        # Сортировка для записи
        sorted_lines = [header] + ['\t'.join(map(str, line)) + '\n' for line in reversed(best_combination)]

        # Запись в файл
        try:
            with open(output_file_path, 'w') as file:
                file.writelines(sorted_lines)
        except IOError:
            print("Error writing to output file.")
        
        self.WeightLabelChange.setText(str(total_weight))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        self.DMtime.setText(str(elapsed_time))
        self.load_data_to_table_backpack()

    def recursive(self):
        start_time = time.perf_counter()
        input_file_path = "C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\First_year\\Lab8\\items"
        output_file_path = "C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\First_year\\Lab8\\Backpack"
        max_weight = int(self.WeeightLine.text())
        
        try:
            with open(input_file_path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("Input file not found.")
            return

        # Пропускаем заголовок
        header = lines[0]
        data = [line.strip().split('\t') for line in lines[1:]]

        # Преобразуем данные в удобный формат
        items = [(line[0], int(line[1]), int(line[2])) for line in data]

        # Рекурсивный метод с мемоизацией
        memo = {}

        def knapsack(index, remaining_weight):
            if (index, remaining_weight) in memo:
                return memo[(index, remaining_weight)]
            
            if index == 0 or remaining_weight == 0:
                return 0, []
            
            name, weight, cost = items[index - 1]
            
            if weight > remaining_weight:
                result = knapsack(index - 1, remaining_weight)
            else:
                without_item = knapsack(index - 1, remaining_weight)
                with_item_value, with_item_combination = knapsack(index - 1, remaining_weight - weight)
                with_item_value += cost
                with_item_combination = with_item_combination + [(name, weight, cost)]
                
                if with_item_value > without_item[0]:
                    result = (with_item_value, with_item_combination)
                else:
                    result = without_item
            
            memo[(index, remaining_weight)] = result
            return result

        total_cost, best_combination = knapsack(len(items), max_weight)

        # Расчет суммы веса
        total_weight = sum(item[1] for item in best_combination)

        # Сортировка для записи
        sorted_lines = [header] + ['\t'.join(map(str, line)) + '\n' for line in reversed(best_combination)]

        # Запись в файл
        try:
            with open(output_file_path, 'w') as file:
                file.writelines(sorted_lines)
        except IOError:
            print("Error writing to output file.")
        
        self.WeightLabelChange.setText(str(total_weight))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        self.TRMtime.setText(str(elapsed_time))
        self.load_data_to_table_backpack()


    
    