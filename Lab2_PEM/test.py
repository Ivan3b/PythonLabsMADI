import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Dialog Example")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.button = QPushButton("Open File Dialog")
        self.button.clicked.connect(self.open_dialog)
        self.layout.addWidget(self.button)

        self.file_info_label = QLabel()
        self.layout.addWidget(self.file_info_label)

    def open_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Text files (*.txt)")
        file_dialog.setViewMode(QFileDialog.List)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            file_path = selected_files[0] if selected_files else ""
            file_size = os.path.getsize(file_path)
            with open(file_path, "r", encoding='utf-8') as file:
                file_text = file.read()
            self.file_info_label.setText(f"File: {file_path}\nSize: {file_size} bytes\nText:\n{file_text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
