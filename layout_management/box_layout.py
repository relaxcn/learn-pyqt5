import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QWidget

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):

		okButton = QPushButton('OK')
		cancelButton = QPushButton('Cancel')

		hbox = QHBoxLayout()
		hbox.addStretch(0)
		hbox.addWidget(okButton)
		hbox.addStretch(3)
		hbox.addWidget(cancelButton)

		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)

		self.setLayout(vbox)

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle('Box Layout')
		self.show()

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()
