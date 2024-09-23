import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import csv

class TableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Name', 'Weight', 'Cost'])

        # Sample data
        data = [
            ('Item1', 2, 10),
            ('Item2', 1, 20),
            ('Item3', 3, 15),
            ('Item4', 4, 5),
            ('Item5', 2, 30),
        ]
        
        for row, (name, weight, cost) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(str(weight)))
            self.table.setItem(row, 2, QTableWidgetItem(str(cost)))
        
        layout.addWidget(self.table)
        self.setLayout(layout)

    def save_optimal_items_to_file(self, filename):
        items = []
        for row in range(self.table.rowCount()):
            name = self.table.item(row, 0).text()
            weight = float(self.table.item(row, 1).text())
            cost = float(self.table.item(row, 2).text())
            items.append((name, weight, cost))

        max_weight = 7
        n = len(items)

        # Memoization dictionary
        memo = {}

        def knapsack_recursive(i, w):
            if (i, w) in memo:
                return memo[(i, w)]

            if i == 0 or w == 0:
                result = 0
            elif items[i - 1][1] > w:
                result = knapsack_recursive(i - 1, w)
            else:
                temp1 = knapsack_recursive(i - 1, w)
                temp2 = knapsack_recursive(i - 1, w - int(items[i - 1][1])) + items[i - 1][2]
                result = max(temp1, temp2)

            memo[(i, w)] = result
            return result

        # Finding the maximum value we can achieve
        max_value = knapsack_recursive(n, max_weight)

        # Finding the items that make up this value
        selected_items = []
        w = max_weight
        for i in range(n, 0, -1):
            if knapsack_recursive(i, w) != knapsack_recursive(i - 1, w):
                selected_items.append(items[i - 1])
                w -= int(items[i - 1][1])

        selected_items.reverse()  # Reverse to maintain original order

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file, delimiter='\t')
            writer.writerow(['Name', 'Weight', 'Cost'])
            for item in selected_items:
                writer.writerow(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    table_widget = TableWidget()
    window.setCentralWidget(table_widget)
    window.resize(400, 300)
    window.show()

    # Save optimal items to file
    table_widget.save_optimal_items_to_file('C:\\Users\\Mrgor\\Desktop\\Programs\\For_study\\Python_labs\\Lab8\\optimal_items.tsv')

    sys.exit(app.exec_())
