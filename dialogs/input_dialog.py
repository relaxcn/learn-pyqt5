import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QGridLayout, QLabel

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		grid = QGridLayout()
		self.setLayout(grid)

		self.bt = QPushButton('Dialog')
		self.bt.clicked.connect(self.showDialog)
		# self.le = QLineEdit(self)

		self.label = QLabel("click the button!")

		grid.addWidget(self.bt, 0, 0)
		grid.addWidget(self.label, 0, 1)

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle("input Dialog")
		self.show()

	def showDialog(self):
		text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

		if ok:
			self.label.setText(f"your name is {text}")

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
if __name__ == '__main__':
	main()
