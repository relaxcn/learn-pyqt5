import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFontDialog, QSizePolicy

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		vbox = QVBoxLayout()
		self.setLayout(vbox)

		btn = QPushButton('Dialog', self)
		btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		btn.clicked.connect(self.showDialog)
		btn.move(20, 20)

		vbox.addWidget(btn)

		self.label = QLabel("knowledge only master", self)
		self.label.move(130, 20)

		vbox.addWidget(self.label)

		self.setGeometry(300, 300, 450, 350)
		self.setWindowTitle("Font Dialog")
		self.show()
	def showDialog(self):
		font, ok = QFontDialog.getFont()
		if ok :
			print(font)
			self.label.setFont(font)
def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
if __name__ == '__main__':
	main()

