import sys
import math
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton, QApplication

class GridExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = [
            '7', '8', '9', '/', '',
            '4', '5', '6', '*', '',
            '1', '2', '3', '-', '',
            '0', '.', '=', '+', '',
            'sin', 'cos', 'exp', 'C'
        ]

        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0, 0, 1, 5)

        # Generate button positions
        positions = [(i, j) for i in range(1, 6) for j in range(5)]  # Adjusted for 5 rows
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(self.on_button_click)  # Connect to the same handler
            grid.addWidget(button, *position)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Grid Layout')
        self.show()

    def on_button_click(self):
        sender = self.sender().text()
        current_txt = self.textLine.text()

        if sender == 'C':
            self.textLine.clear()
        elif sender == '=':
            result = self.evaluate_expression(current_txt)
            self.textLine.setText(str(result))
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
                return eval(expression)  # Ensure you trust the input before using eval
        except Exception:
            return "Error"  # Handle any evaluation errors

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GridExample()
    sys.exit(app.exec_())
