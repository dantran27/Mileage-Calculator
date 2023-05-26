import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout,QHBoxLayout,QComboBox,
                             QLabel,QLineEdit,QSpinBox,QPushButton)
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        
        self.setWindowTitle("MIlaeage Calculator")
        layout = QVBoxLayout()



        # set to main layout
        gui = QWidget()

        gui.setLayout(layout)
        
        label = QLabel("Calculate miles!")
        font = label.font()
        font.setPointSize(10)
        label.setFont(font)
        layout.addWidget(label)

        self.widget = QComboBox()
        self.widget.addItems(["Albany", "Baker City", "Beaverton"])

        self.widget2 = QComboBox()
        self.widget2.addItems(["Albany", "Baker City", "Beaverton"])
        
        self.calculate_button = QPushButton(text="Calculate", parent=self)
        self.calculate_button.setFixedSize(100, 60)
        self.calculate_button.clicked.connect(self.calculate_miles)
        
        layout.addWidget(self.widget)
        layout.addWidget(self.widget2)
        layout.addWidget(self.calculate_button)

        self.setCentralWidget(gui)

    def calculate_miles(self):
        pass



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()