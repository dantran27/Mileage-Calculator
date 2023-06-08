import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout,QHBoxLayout,QComboBox,
                             QLabel,QTextEdit,QSpinBox,QPushButton)
from PyQt6.QtGui import QPalette, QColor, QFont, QFontDatabase

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
        label.setFont(QFont("Times new roman", 18))

        self.widget = QComboBox()
        self.widget.addItems(list(controller.mileage_chart.keys()))
        self.widget.setFont(QFont("Times new roman", 18))

        self.widget2 = QComboBox()
        self.widget2.addItems(list(controller.mileage_chart.keys()))
        self.widget2.setFont(QFont("Times new roman", 18))

    
        self.calculate_button = QPushButton(text="Calculate", parent=self)
        self.calculate_button.setFixedSize(100, 60)
        self.calculate_button.clicked.connect(self.calculate_miles)
        self.output=QTextEdit()
        self.calculate_button.setFont(QFont("Times new roman", 16))

        layout.addWidget(self.widget)
        layout.addWidget(self.widget2)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.output)

        self.setCentralWidget(gui)

    def calculate_miles(self):
        city1 = self.widget.currentText()
        city2 = self.widget2.currentText()
        # get miles 
        miles = controller.get_miles(city1, city2)
        result = f"From {city1} to {city2} the miles are {miles}."
        self.output.setText(result)
      
       
       



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()