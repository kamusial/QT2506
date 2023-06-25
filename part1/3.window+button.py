from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QPushButton
from PyQt6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja aplikcja')
        self.setFixedSize(QSize(600, 400))
        button = QPushButton('przycisk')
        button.setCheckable(True)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)
        button.clicked.connect(self.button_clicked)
        button.clicked.connect(self.button_toogle)
        self.setCentralWidget(button)

    def button_pressed(self):
        print('wcisniety')

    def button_released(self):
        print('Puszczony')

    def button_clicked(self):
        print('kliniety')

    def button_toogle(self, checked):
        print('Stan przycisku: ',checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

