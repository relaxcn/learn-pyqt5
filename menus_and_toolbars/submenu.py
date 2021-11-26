from PyQt5.QtWidgets import QApplication, QMenu, QMainWindow, QAction
import sys

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		# 开启状态栏
		self.statusBar()
		# 创建一个菜单栏
		menubar = self.menuBar()

		# 创建第一个File菜单
		fileMenu = menubar.addMenu('File')

		# 创建另一个import菜单
		impMenu = QMenu('import', self)
		# 在import 菜单上增加impAct动作
		impAct = QAction('Import mail', self)
		impAct.setStatusTip("import a mail.")
		impMenu.addAction(impAct)

		# 创建一个新的new动作
		newAct = QAction('New', self)
		# 设置状态提示字符
		newAct.setStatusTip('create a new file')

		# 向file菜单中添加一个动作和一个菜单，也就是子菜单
		fileMenu.addAction(newAct)
		fileMenu.addMenu(impMenu)

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle("submenu")
		self.show()

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()