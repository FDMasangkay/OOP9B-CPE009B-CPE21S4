import sys
import math
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QGridLayout, QWidget, QMessageBox, QFileDialog, QAction)

class GridExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")

        self.operations = []

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        self.initUI(central_widget)
        self.create_menu()

    def initUI(self, central_widget):
        grid = QGridLayout()
        central_widget.setLayout(grid)

        names = [
            '7', '8', '9', '/', '',
            '4', '5', '6', '*', '',
            '1', '2', '3', '-', '',
            '0', '.', '=', '+', '',
            'sin', 'cos', 'exp', 'C'
        ]

        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0, 0, 1, 5)

        positions = [(i, j) for i in range(1, 6) for j in range(5)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(self.on_button_click)
            grid.addWidget(button, *position)

        self.show()

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_to_file)
        file_menu.addAction(save_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        self.shortcut_exit = QAction("Exit", self)
        self.shortcut_exit.triggered.connect(self.close)
        self.addAction(self.shortcut_exit)
        self.shortcut_exit.setShortcut("Ctrl+Q")

    def save_operation(self, operation):
        self.operations.append(operation)

    def save_to_file(self):
        # Get the file path
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if filename:
            with open(filename, "w") as file:
                for operation in self.operations:
                    file.write(operation + "\n")

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)

    def on_button_click(self):
        sender = self.sender().text()
        current_txt = self.textLine.text()

        if sender == 'C':
            self.textLine.clear()
        elif sender == '=':
            result = self.evaluate_expression(current_txt)
            self.textLine.setText(str(result))
            self.save_operation(f"{current_txt} = {result}")
        elif sender == 'Backspace':
            self.textLine.setText(current_txt[:-1])
        else:
            self.textLine.setText(current_txt + sender)

    def evaluate_expression(self, expression):
        try:
            if expression.startswith('sin'):
                value = float(expression[3:])
                return math.sin(value)
            elif expression.startswith('cos'):
                value = float(expression[3:])
                return math.cos(value)
            elif expression.startswith('exp'):
                value = float(expression[3:])
                return math.exp(value)
            else:
                return eval(expression)  
        except Exception:
            return "Error"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GridExample()
    sys.exit(app.exec_())
