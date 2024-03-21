import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Мое окно с кнопкой")

        # Создаем кнопку
        self.button = QPushButton("Выбрать файл", self)
        self.button.clicked.connect(self.open_dialog)  # Подключаем обработчик события к кнопке

        # Размещаем кнопку на главном виджете
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_dialog(self):
        # Открываем диалоговое окно для выбора файла
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Text files (*.txt)")
        file_dialog.setViewMode(QFileDialog.List)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file_name in selected_files:
                print("Выбран файл:", file_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())