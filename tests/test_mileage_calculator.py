import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout,QHBoxLayout,QComboBox,
                             QLabel,QLineEdit,QSpinBox,QPushButton)
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        layout = QVBoxLayout()

        # set to main layout
        gui = QWidget()

        gui.setLayout(layout)
        self.setCentralWidget(gui)

        
        Calculate_button = QPushButton(text="Center", parent=self)
        Calculate_button.setFixedSize(100, 60)

        layout.addWidget(Calculate_button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()