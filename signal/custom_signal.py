import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class Communicate(QObject):
	closeApp = pyqtSignal()

class Example(QMainWindow):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		self.c = Communicate()
		self.c.closeApp.connect(self.close)

		button = QPushButton('button', self)
		button.clicked.connect(self.clicked)

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle("Custom Signal")
		self.show()

	def mousePressEvent(self, event):
		self.c.closeApp.emit()

	def clicked(self):
		self.c.closeApp.emit()

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()

