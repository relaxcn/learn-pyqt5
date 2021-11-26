import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMainWindow

class Example(QMainWindow):
	"""docstring for Example"""
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		wid = QWidget()

		grid = QGridLayout(wid)

		grid.setSpacing(10)

		self.statusBar()

		but1 = QPushButton()
		but2 = QPushButton()
		but1.setText("Button1")
		but2.setText("Button2")

		grid.addWidget(but2)
		grid.addWidget(but1)

		but1.clicked.connect(self.clicked)
		but2.clicked.connect(self.clicked)

		self.setCentralWidget(wid)

		self.setLayout(grid)
		self.move(300, 300)
		self.setWindowTitle("Event Sender")
		self.show()

	def clicked(self):

		sender = self.sender()
		# print(sender)
		self.statusBar().showMessage(sender.text() + ' was pressed.')

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()


		