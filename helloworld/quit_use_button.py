import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMessageBox, QDesktopWidget
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):

		self.qbtn = QPushButton('Quit', self)
		self.qbtn.adjustSize()
		self.qbtn.move(200, 200)
		self.qbtn.clicked.connect(QCoreApplication.instance().quit)

		# self.setGeometry(300, 300, 400, 400)
		self.resize(300, 300)
		self.setWindowTitle("Quit Button")
		self.show()

	def closeEvent(self, event):
		reply = QMessageBox.warning(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().avaliableGeometry().center()
		qr = moveCenter(cp)
		self.move(qr.topLeft())
			
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()

	sys.exit(app.exec_())
