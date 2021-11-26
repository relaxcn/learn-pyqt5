import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget , QToolTip, QPushButton
from PyQt5.QtGui import QFont, QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip("This is a <b>QWidget</b> widget")

        self.btn = QPushButton(self)
        self.btn.setText("Click me")
        self.btn.setToolTip("This is a <b>Button</b> widget.")
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 100)
        self.btn.clicked.connect(self.clicked)
        
        self.label = QtWidgets.QLabel(self)
        self.label.setText("this is a lable.")
        self.label.move(50, 50)

        self.setGeometry(300, 300, 500, 220)
        self.setWindowTitle("ToolTip")
        self.setWindowIcon(QIcon('C:\\Users\\easechen\\Documents\\myDocumnets\\Learning\\pyqt5/firstprogram/icon.png'))

        self.show()
    def clicked(self):
        self.label.setText("xiu huo!\nxiu huo")
        print("clicked!")
        self.update()
    def update(self):
        self.label.adjustSize()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
