from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow, QTextEdit
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		toolbar = self.addToolBar('Exit')

		exitAct = QAction(QIcon('exit.png'), 'Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.setStatusTip('exit program.')
		exitAct.triggered.connect(qApp.quit)

		fileMenu.addAction(exitAct)
		toolbar.addAction(exitAct)

		textEdit = QTextEdit()
		self.setCentralWidget(textEdit)

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle('Main Window')
		self.show()

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()