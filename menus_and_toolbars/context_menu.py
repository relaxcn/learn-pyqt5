from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow, QMenu
import sys

class Example(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()
	def initUI(self):

		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle('Context Menu')
		self.show()

	# 重写 右键菜单
	def contextMenuEvent(self, event):

		cmenu = QMenu(self)

		newAct = cmenu.addAction('New')
		openAct = cmenu.addAction('Open')
		quitAct = cmenu.addAction('Quit')

		# 使用mapToGlobal把组件的坐标转换成为屏幕的坐标，exec_用来返回当前鼠标所处于的动作
		action = cmenu.exec_(self.mapToGlobal(event.pos()))

		if action == quitAct:
			qApp.quit()
def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
