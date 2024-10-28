# Grid Layout
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QApplication, \
    QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

class GridExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = [
            '7', '8', '9', '/', ''
            '4', '5', '6', '*', ''
            '1', '2', '3', '-', ''
            '0', '.', '=', '+', ''
            '', '', '', '', ''
        ]

        self.textLine =QLineEdit(self)
        grid.addWidget(self.textLine, 0 , 1, 1, 5)

        # using a loop to generate positions
        positions = [(i, j) for i in range(1, 7) for j in range(1, 5)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Grid Layout')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GridExample()
    sys.exit(app.exec_())