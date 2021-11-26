from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel
import sys

class Example(QMainWindow):
	"""docstring for Example"""
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):

		# 设置状态栏，并显示信息
		self.statusbar = self.statusBar()
		self.statusbar.showMessage("Ready")

		# 创建一个菜单栏
		menubar = self.menuBar()

		# 添加一个菜单，命名为 View
		viewMenu = menubar.addMenu('View')

		# 创建可勾选的Action， 设置状态提示信息，触发器， 起始选择状态
		viewStatAct = QAction('View statusbar', self, checkable = True)
		viewStatAct.setStatusTip("view statusbar")
		viewStatAct.setChecked(True)
		viewStatAct.triggered.connect(self.toggleMenu)

		newAct = QAction('another act', self)

		# 将 viewStatAct Action 添加进 File 菜单
		viewMenu.addAction(viewStatAct)
		viewMenu.addAction(newAct)

		self.label = QLabel(self)
		self.label.setText("hello")
		self.label.setGeometry(100, 100, 100, 100)

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle('check_menu')
		self.show()

	def toggleMenu(self, state):
		# state 是布尔值类型
		print(state)
		# 如果被选中
		if state:
			self.statusbar.show()
			self.label.show()
		else:
			self.statusbar.hide()
			self.label.hide()
def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

main()