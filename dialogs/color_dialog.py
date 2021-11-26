import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow, QFrame, QColorDialog
from PyQt5.QtGui import QColor

class Exmaple(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		col = QColor(0, 0, 0)

		self.btn = QPushButton("Dialog", self)
		self.btn.move(20, 20)

		self.btn.clicked.connect(self.showDialog)

		self.frm = QFrame(self)
		self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
		self.frm.setGeometry(130, 22, 200, 200)

		self.setGeometry(300, 300, 450, 350)
		self.setWindowTitle('Color Dialog')
		self.show()

	def showDialog(self):
		col = QColorDialog.getColor()
		print(col)
		print(col.name())
		if col.isValid():
			print(col.name())
			self.frm.setStyleSheet("QWidget {background-color: %s }" % col.name())

def main():
	app = QApplication(sys.argv)
	ex = Exmaple()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()