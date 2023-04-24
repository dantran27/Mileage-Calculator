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
        self.setCentralWidget(gui)
        
        label = QLabel("Press here to calculate miles!")
        font = label.font()
        font.setPointSize(10)
        label.setFont(font)
        layout.addWidget(label)

        self.setCentralWidget(gui)
        
        Calculate_button = QPushButton(text="Calculate", parent=self)
        Calculate_button.setFixedSize(100, 60)

        layout.addWidget(Calculate_button)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()