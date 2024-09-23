import sys
from PyQt5 import QtWidgets

# Import your Ui_Dialog and MyDialog classes
from Table_Ui import Ui_Dialog, MyDialog

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    # Create an instance of MyDialog
    dialog = MyDialog()
    
    # Show the dialog as the main window
    dialog.show()
    
    # Execute the application
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
