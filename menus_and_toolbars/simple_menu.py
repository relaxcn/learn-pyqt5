from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
import sys
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
	def __init__(self):
		super().__init__()	
		self.initUI()


	def initUI(self):
		# 创建各种动作，这些动作是菜单栏的子项目
		exitAct = QAction(QIcon('exit.png'), '&Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.setStatusTip('Exit Application')
		exitAct.triggered.connect(qApp.quit)


		openAct = QAction(QIcon('open.png'), '&Open', self)
		openAct.setShortcut('Ctrl+N')
		openAct.setStatusTip('Open a file.')


		copyAct = QAction(QIcon('copy.png'), '&Copy', self)
		copyAct.setShortcut('Ctrl+C')
		copyAct.setStatusTip("Copy a file")
		# 创建一个状态栏	
		self.statusBar()

		# 返回一个菜单栏对象
		menubar = self.menuBar()
		# 向对象添加菜单栏 
		fileMenu = menubar.addMenu('&File')
		# 使用 addAction 方法向菜单栏中添加动作
		fileMenu.addAction(exitAct)
		fileMenu.addAction(openAct)

		editMenu = menubar.addMenu('&Edit')
		editMenu.addAction(copyAct)	

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle("menuBar")
		self.show()

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()