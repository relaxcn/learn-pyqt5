import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):
	"""this is a PyQt5 status bars example class"""
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		self.statusBar().showMessage("Ready")

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle("Status Bars")
		self.show()

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()