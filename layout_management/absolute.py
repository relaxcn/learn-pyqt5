import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		label1 = QLabel('ZetCode', self)
		label1.move(15, 10)

		label2 = QLabel('tutorials', self)
		label2.move(35, 40)

		label3 = QLabel('for programers', self)
		label3.move(55, 70)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Absolute')
		self.show()

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()