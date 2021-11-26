from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
import sys

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle("Reimplement handler")
		self.show()

	def keyPressEvent(self, e):
		print(e.key)
		if e.key() == Qt.Key_Escape:
			print("got it")
			self.close()

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()