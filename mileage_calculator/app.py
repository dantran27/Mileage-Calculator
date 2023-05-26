import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout,QHBoxLayout,QComboBox,
                             QLabel,QLineEdit,QSpinBox,QPushButton)
from PyQt6.QtGui import QPalette, QColor

import controller

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
        city1 = self.widget.currentText()
        city2 = self.widget2.currentText()
        # get miles 
        miles = controller.get_miles(city1, city2)
        print(miles)
       



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()