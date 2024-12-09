import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton

class ButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("QPushButton Widget")
        self.displayButton()
        self.show()
    
    def displayButton(self):
        name_label=QLabel(self)
        name_label.setText("Don't push the button.")
        name_label.move(60, 30)
        button=QPushButton("Push me!", self)
        button.clicked.connect(self.buttonClicked)
        button.move(80,70)
    
    def buttonClicked(self):
        self.close()

app=QApplication(sys.argv)
window=ButtonWindow()
sys.exit(app.exec())