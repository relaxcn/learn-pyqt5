from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QAction, QToolBar
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):

		# 返回一个工具栏对象
		toolbar = self.addToolBar('Exit')

		exitAct = QAction(QIcon('exit.png'), 'Exit', self)
		exitAct.setStatusTip("exit program.")
		exitAct.setShortcut('Ctrl+Q')
		exitAct.triggered.connect(self.close)


		self.statusBar()
		toolbar.addAction(exitAct)

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle('Tool Bar')
		self.show()

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()